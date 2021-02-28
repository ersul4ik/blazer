from celery.result import AsyncResult
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.base import View

from factories.forms import LoginForm, DataFixtureForm, DataFixtureColumnFormSet
from factories.models import DataFixture, DataSet
from factories.tasks import generate_data_set


class LoginView(View):
    template_name = 'factories/login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})
        user = authenticate(**form.cleaned_data)
        if user is not None:
            login(request, user)
            return redirect(reverse('fixture-list'))
        return render(request, self.template_name, {'form': form})


def user_logout(request):
    logout(request)
    return redirect(reverse('login'))


class DataFixtureView(View):
    template_name = 'factories/fixtures.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        fixtures = DataFixture.objects.only('id', 'name', 'modified')
        return render(request, self.template_name, {'records': fixtures})


class DataFixtureUpdate(UpdateView):
    model = DataFixture
    template_name = 'factories/fixture_create.html'
    form_class = DataFixtureForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['columns'] = DataFixtureColumnFormSet(self.request.POST, instance=self.object)
        else:
            data['columns'] = DataFixtureColumnFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        columns = context['columns']
        with transaction.atomic():
            self.object = form.save()
            if columns.is_valid():
                columns.instance = self.object
                columns.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('fixture-list')


class DataFixtureCreate(CreateView):
    model = DataFixture
    template_name = 'factories/fixture_create.html'
    form_class = DataFixtureForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['columns'] = DataFixtureColumnFormSet(self.request.POST)
        else:
            data['columns'] = DataFixtureColumnFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        columns = context['columns']
        with transaction.atomic():
            self.object = form.save()
            if columns.is_valid():
                columns.instance = self.object
                columns.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('fixture-update', kwargs={'pk': self.object.pk})


class DataFixtureDelete(DeleteView):
    model = DataFixture
    template_name = 'factories/confirm_delete.html'
    success_url = reverse_lazy('fixture-list')


class DataSetView(View):
    template_name = 'factories/datasets_list.html'

    def get(self, request, *args, **kwargs):
        datasets = DataSet.objects.filter(fixture_id=kwargs['pk'])
        return render(request, self.template_name, {'records': datasets})

    def post(self, request, *args, **kwargs):
        rows_count = int(request.POST['rows-count'])
        filename = f'{timezone.now().strftime("%Y-%m-%d %H:%M:%S")}.xlsx'
        task = generate_data_set.delay(kwargs['pk'], rows_count, filename)
        DataSet.objects.create(fixture_id=kwargs['pk'], task_id=task.id, filename=filename, status=task.status)
        return redirect(reverse('dataset-list', args=(kwargs['pk'], )))


class TaskDetailView(View):
    def get(self, request, *args, **kwargs):
        task = AsyncResult(str(kwargs['pk']))
        if not task:
            return JsonResponse({'task_status': 'UNKNOWN'}, status=404)
        return JsonResponse({'task_status': task.status})

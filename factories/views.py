from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from factories.forms import LoginForm, DataFixtureForm
from factories.models import DataFixture


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
        return render(request, self.template_name, {'records': DataFixture.objects.only('id', 'name', 'modified')})


class DataFixtureDetailsView(View):
    template_name = 'factories/fixture_details.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        query = get_object_or_404(DataFixture, pk=kwargs['pk'])
        query.delete()
        return HttpResponse('Deleted')


class DataFixtureCreateView(View):
    template_name = 'factories/fixture_create.html'
    form_class = DataFixtureForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.is_valid()
        form.save()
        return render(request, self.template_name, {'form': form})

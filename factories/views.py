from django.shortcuts import render
from django.views.generic.base import View

from factories.forms import LoginForm


class LoginView(View):
    template_name = 'factories/login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.is_valid()
        return render(request, self.template_name, {'form': form})

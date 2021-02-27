from django import forms

from factories.models import DataFixture


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class DataFixtureForm(forms.ModelForm):
    class Meta:
        model = DataFixture
        fields = (
            'name',
            'column_separator',
            'string_character',
        )

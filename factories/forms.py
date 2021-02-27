from django import forms

from factories.models import DataFixture


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class DataFixtureForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['column_separator'].widget.attrs['class'] = 'form-control'
        self.fields['string_character'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = DataFixture
        fields = (
            'name',
            'column_separator',
            'string_character',
        )

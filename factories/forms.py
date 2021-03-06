from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, HTML, ButtonHolder, Submit, Fieldset
from django import forms
from django.forms import inlineformset_factory

from factories.models import DataFixture, DataFixtureColumn
from factories.utils import Formset


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class DataFixtureColumnForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['extra'].widget.attrs['class'] = 'col-md-3'
        self.fields['extra'].widget.attrs['min'] = 1

    class Meta:
        model = DataFixtureColumn
        exclude = ()


DataFixtureColumnFormSet = inlineformset_factory(
    DataFixture, DataFixtureColumn, form=DataFixtureColumnForm,
    fields=['name', 'sample', 'extra', 'order'], extra=3, can_delete=True
)


class DataFixtureForm(forms.ModelForm):
    class Meta:
        model = DataFixture
        exclude = [
            'created',
            'modified',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-group'
        self.helper.layout = Layout(
            Div(
                Field('name'),
                Field('column_separator'),
                Field('string_character'),
                HTML('<br>'),
                Fieldset(
                    'Add columns',
                    Formset('columns'),
                ),
                ButtonHolder(Submit('submit', 'save')),
                )
            )

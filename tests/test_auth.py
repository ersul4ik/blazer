from django.urls import reverse

from factories.forms import LoginForm


def test_should_contain_login_form(client):
    url = reverse('login')

    response = client.get(url)

    assert response.status_code == 200
    assert response.context['form'] == LoginForm

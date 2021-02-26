from django.urls import path

from factories.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login-details'),
    path('logout/', LoginView.as_view(), name='logout-details'),
]

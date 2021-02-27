from django.urls import path

from factories.views import LoginView, FixtureView, user_logout

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('fixtures/', FixtureView.as_view(), name='fixture-list'),
]

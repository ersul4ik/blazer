from django.urls import path

from factories.views import LoginView, DataFixtureView, user_logout, DataFixtureDetailsView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('fixtures/', DataFixtureView.as_view(), name='fixture-list'),
    path('fixtures/<int:pk>/', DataFixtureDetailsView.as_view(), name='fixture-details'),
]

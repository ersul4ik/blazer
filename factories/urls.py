from django.urls import path

from factories import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('fixtures/', views.DataFixtureView.as_view(), name='fixture-list'),
    path('fixtures/<int:pk>/', views.DataFixtureDetailsView.as_view(), name='fixture-details'),
    path('fixtures/add/', views.DataFixtureCreateView.as_view(), name='fixture-add'),
]

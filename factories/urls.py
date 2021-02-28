from django.urls import path

from factories import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('fixtures/', views.DataFixtureView.as_view(), name='fixture-list'),
    path('fixtures/add/', views.DataFixtureCreate.as_view(), name='fixture-add'),
    path('fixtures/<int:pk>/update/', views.DataFixtureUpdate.as_view(), name='fixture-update'),
    path('fixtures/<int:pk>/delete/', views.DataFixtureDelete.as_view(), name='fixture-delete'),
]

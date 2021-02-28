from django.urls import path

from factories import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.DataFixtureView.as_view(), name='fixture-list'),
    path('add/', views.DataFixtureCreate.as_view(), name='fixture-add'),
    path('<int:pk>/update/', views.DataFixtureUpdate.as_view(), name='fixture-update'),
    path('<int:pk>/delete/', views.DataFixtureDelete.as_view(), name='fixture-delete'),
    path('<int:pk>/datasets/', views.DataSetView.as_view(), name='dataset-list'),
    path('tasks/<uuid:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
]

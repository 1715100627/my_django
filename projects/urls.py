# from .views import index
from django.urls import path
from projects import views

urlpatterns = [
    # path('', views.IndexView.as_view())
    path('projects/', views.ProjectsViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }),name='projects-list'),

    path('projects/<int:pk>/', views.ProjectsViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),

    path('projects/names/', views.ProjectsViewSet.as_view({
        'get': 'names',
    }),name='project-names')
]

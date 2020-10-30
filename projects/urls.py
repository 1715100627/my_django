# from .views import index
from django.urls import path
from projects import views

urlpatterns = [
    # path('', views.IndexView.as_view())
    path('projects/', views.ProjectsList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view())
]

from django.urls import path
from .views import ProjectListCreateView, ProjectRetrieveUpdateDestroyView, UserProjectListView

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyView.as_view(), name='project-detail'),
    path('user-projects/', UserProjectListView.as_view(), name='user-projects'),
]

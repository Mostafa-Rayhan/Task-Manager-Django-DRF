from django.urls import path
from .views import TaskListView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView
from .api_views import TaskListAPIView, TaskDetailAPIView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('task/new/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),

    path('api/tasks/', TaskListAPIView.as_view(), name='task-list-api'),
    path('api/tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail-api'),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/tasks/', TaskListAPIView.as_view(), name='task-list-api'),
    path('api/tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail-api'),
]

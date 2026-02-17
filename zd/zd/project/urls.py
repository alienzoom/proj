from django.urls import path
from . import views

urlpatterns = [
    # Проекты
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('projects/<int:project_id>/edit/', views.project_edit, name='project_edit'),
    path('projects/<int:project_id>/delete/', views.project_delete, name='project_delete'),
    path('projects/<int:project_id>/status/', views.project_change_status, name='project_change_status'),
    
    # Приглашения
    path('projects/<int:project_id>/invite/', views.invite_to_project, name='invite_to_project'),
    path('invitations/<int:invitation_id>/respond/', views.respond_to_invitation, name='respond_to_invitation'),
    path('invitations/<int:invitation_id>/cancel/', views.cancel_invitation, name='cancel_invitation'),
    
    # Участники
    path('projects/<int:project_id>/participants/<int:participant_id>/remove/', 
         views.remove_participant, name='remove_participant'),
    
    # Комментарии
    path('projects/<int:project_id>/comments/add/', views.add_comment, name='add_comment'),
    
    # Файлы
    path('projects/<int:project_id>/files/upload/', views.upload_file, name='upload_file'),
    path('projects/<int:project_id>/files/<int:file_id>/delete/', views.delete_file, name='delete_file'),
]
from django.urls import path, include
from . import views
from project.views import project_create, project_list

urlpatterns = [
    path('', views.hub, name='home'),
    path('hub/', views.hub, name='hub'),
    path('profile/', views.profile, name='profile'),
    path('form_page/', views.form_page, name='form_page'),
    path('create_team/', views.create_team, name='create_team'),
    path('projects/', include('project.urls')),
    path('projects/create/', project_create, name='project_create'),
    path('projects/list/', project_list, name='project_list'),
    path('logout/', views.logout_view, name='logout'),
    path('validate-email/', views.validate_email, name='validate_email'),
    path('validate-phone/', views.validate_phone, name='validate_phone'),
]
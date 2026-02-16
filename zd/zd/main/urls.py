from django.urls import path
from . import views

urlpatterns = [
    path('', views.hub, name='home'),
    path('hub/', views.hub, name='hub'),
    path('profile/', views.profile, name='profile'),
    path('form_page/', views.form_page, name='form_page'),
    path('create_team/', views.create_team, name='create_team'),
    path('logout/', views.logout_view, name='logout'),
    path('validate-email/', views.validate_email, name='validate_email'),
    path('validate-phone/', views.validate_phone, name='validate_phone'),
]
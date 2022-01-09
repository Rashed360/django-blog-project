from django.urls import path
from . import views

app_name = 'app_login'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update/', views.profile_update, name='update'),
    path('extra/', views.profile_extra, name='extra'),
    path('modify/', views.profile_extra_update, name='modify'),
    path('password/', views.password_change, name='password'),
]
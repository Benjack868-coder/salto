from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='system_index'),
    path('login/', views.Login.as_view(), name='system_login'),
    path('register/', views.Register.as_view(), name='system_register'),
    path('recover/', views.Recover.as_view(), name='system_recover_account'),
    path('logout/', views.signout, name='system_logout'),
]
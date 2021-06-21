from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='member_index'),
    path('<int:member_id>/profile/', views.Profile.as_view(), name='member_profile'),
    path('all/', views.ViewMembers.as_view(), name='member_view_all'),#ajax request only

]
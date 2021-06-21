from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='derby_index'),
    path('<int:derby_id>/entry', views.DerbyEntry.as_view(), name='derby_add_entry'),
    path('<int:derby_id>/entry/<int:entry_id>/fight/', views.DerbyFight.as_view(), name='derby_add_fight'),
    path('<int:derby_id>/profile', views.DerbyProfile.as_view(), name='derby_profile'),
]
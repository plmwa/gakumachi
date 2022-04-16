from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('event_list', views.EventListView.as_view(), name='event_list'),
    path('member_list',views.MemberListView.as_view(), name='member_list'),
    path('event_detail/<int:pk>/',  views.EventDetailView.as_view(), name='event_detail'), 
]
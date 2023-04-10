from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.BabyList.as_view(), name='baby_list'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('diapers/', views.DiaperList.as_view(), name='diaper_list'),
    path('feedings/', views.FeedingList.as_view(), name='feeding_list'),
    path('affirmations/', views.AffirmationList.as_view(), name='affirmation_list'),

    path('babies/<int:pk>', views.BabyDetail.as_view(), name='baby_detail'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('diapers/<int:pk>', views.DiaperDetail.as_view(), name='diaper_detail'),
    path('feedings/<int:pk>', views.FeedingDetail.as_view(), name='feeding_detail'),
    path('affirmations/<int:pk>', views.AffirmationDetail.as_view(),
         name='affirmation_detail'),
]

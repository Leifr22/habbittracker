from django.contrib import admin
from django.urls import path, include, re_path

from habits import views
from habits.views import mark_habit_complete, HabitAPIView, HabitDetailView

urlpatterns = [
    path('',views.HabitsList.as_view(),name='home'),
    path('habit_form/',views.HabitCreationView.as_view(),name='habit_add'),
    path('update/<int:pk>',views.UpdateHabitsView.as_view(),name='update_habit'),
    path('habit/delete/<int:pk>/', views.HabitDeleteView.as_view(), name='delete_habit'),
    path('habit/mark/<int:pk>/<str:date>/', mark_habit_complete, name='mark_habit_complete'),
    path('api/habits/',HabitAPIView.as_view(),name='habit_list_create'),
    path('api/habits/<int:pk>/',HabitDetailView.as_view(),name='habit-details'),
    path('api/habits/drf-auth/',include('rest_framework.urls')),
    path('api/habits/auth/',include('djoser.urls.authtoken')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

]
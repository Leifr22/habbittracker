from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework import generics, permissions

from habits.forms import HabitForm
from habits.models import Habit, HabitTracker
from habits.serializers import HabitSerializers


# Create your views here
def mark_habit_complete(request, habit_id, date):
    habit=get_object_or_404(Habit,pk=habit_id)
    HabitTracker.objects.create(habit=habit, date=date, completed=True)
    return redirect('home')
class HabitCreationView(CreateView):
    model = Habit
    form_class =HabitForm
    template_name = 'habit/habit_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form): #Обработка данных в форме
        form.instance.user = self.request.user
        return super().form_valid(form)


class HabitsList(LoginRequiredMixin,ListView):
    model = Habit
    template_name = 'habit/homepage.html'
    context_object_name = 'habits'

    def get_queryset(self):
        queryset = super().get_queryset()
        today = date.today()
        for habit in queryset:
            habit.is_completed_today = HabitTracker.objects.filter(habit=habit, date=today, completed=True).exists()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today_date'] = date.today()
        return context


def mark_habit_complete(request, pk, date):
    habit = get_object_or_404(Habit, pk=pk)
    HabitTracker.objects.create(habit=habit, date=date, completed=True)
    return redirect('home')
class UpdateHabitsView(UpdateView):
    model=Habit
    form_class = HabitForm
    template_name = 'habit/habit_form.html'
    success_url = reverse_lazy('home')
class HabitDeleteView(DeleteView):
    model = Habit
    form_class = HabitForm
    template_name = 'habit/habit_form.html'
    success_url = reverse_lazy('home')
class HabitAPIView(generics.ListCreateAPIView):
    serializer_class = HabitSerializers
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class HabitDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializers
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

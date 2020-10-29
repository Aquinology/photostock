from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Picture
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class PictureList(ListView):
    model = Picture
    context_object_name = "picture_list"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["date"] = timezone.now()
    #     return context


class PictureDetail(DetailView):
    model = Picture


class PictureCreate(LoginRequiredMixin, CreateView):
    model = Picture
    fields = ["title", "picture", "desc"]
    success_url = reverse_lazy("picture_list")


class PictureDelete(LoginRequiredMixin, DeleteView):
    model = Picture
    success_url = reverse_lazy("picture_list")


class PictureUpdate(LoginRequiredMixin, UpdateView):
    model = Picture
    fields = ["title", "picture", "desc"]
    success_url = reverse_lazy("picture_list")

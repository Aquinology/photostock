from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Picture
from django.utils import timezone


class PictureList(ListView):
    model = Picture
    context_object_name = "picture_list"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["date"] = timezone.now()
    #     return context


class PictureDetail(DetailView):
    model = Picture

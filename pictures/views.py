from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Picture, TypePicture
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class PictureList(ListView):
    model = Picture
    context_object_name = "picture_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type_picture_list"] = TypePicture.objects.all()
        return context


class TypePictureList(ListView):
    model = Picture

    def get_queryset(self):
        picture_type = get_object_or_404(TypePicture, pk=self.kwargs['pk'])
        return Picture.objects.filter(type=picture_type)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type_picture_list"] = TypePicture.objects.all()
        return context


class PictureOwnerList(LoginRequiredMixin, ListView):
    model = Picture
    template_name = "pictures/my_picture_list.html"
    context_object_name = "my_picture_list"

    def get_queryset(self):
        return Picture.objects.filter(user=self.request.user)


class PictureDetail(DetailView):
    model = Picture


class PictureCreate(LoginRequiredMixin, CreateView):
    model = Picture
    fields = ["type", "title", "picture"]
    success_url = reverse_lazy("picture_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PictureDelete(LoginRequiredMixin, DeleteView):
    model = Picture
    success_url = reverse_lazy("picture_list")

    def dispatch(self, request, *args, **kwargs):
        if self.request.user != self.get_object().user:
            raise Http404("Вы не можете удалять чужие добавления")
        return super(PictureDelete, self).dispatch(request, *args, **kwargs)


class PictureUpdate(LoginRequiredMixin, UpdateView):
    model = Picture
    fields = ["title", "picture"]
    success_url = reverse_lazy("picture_list")

    def dispatch(self, request, *args, **kwargs):
        if self.request.user != self.get_object().user:
            raise Http404("Вы не можете редактировать чужие добавления")
        return super(PictureUpdate, self).dispatch(request, *args, **kwargs)

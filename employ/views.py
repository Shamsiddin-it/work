from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import *
from django.urls import reverse_lazy
from django.http import HttpResponseBadRequest

class HomeView(TemplateView):
    template_name = "home.html"

class UserCreateView(CreateView):
    model = User
    template_name = "user_create.html"
    fields = ['fullname', 'age', 'image', 'phone', 'email', 'password']
    success_url = reverse_lazy("home")

class WorkCreateView(CreateView):
    model = Work
    template_name = "work_create.html"
    fields = ['title', 'description', 'category', 'image', 'video', 'user', 'region', 'address']
    success_url = reverse_lazy("work_list")

class WorkListView(ListView):
    model = Work
    template_name = "work_list.html"
    context_object_name = "works"

class WorkDetailView(DetailView):
    model = Work
    template_name = "work_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["application_work"] = Application.objects.filter(work=self.kwargs["pk"])
        return context

    context_object_name = "work"

class WorkUpdateView(UpdateView):
    model = Work
    template_name = "work_update.html"
    fields = ['title', 'description', 'category', 'image', 'video', 'user', 'region', 'address']
    success_url = reverse_lazy("work_list")

class WorkDeleteView(DeleteView):
    model = Work
    template_name = "work_delete.html"
    success_url = reverse_lazy("work_list")

class ApplicationCreateView(CreateView):
    model = Application
    template_name = "application_create.html"
    fields = ['user', 'message', 'price', 'duration', 'status']
    def form_valid(self, form):
        work = Work.objects.filter(id=self.kwargs["pk"]).first()
        if work:
            form.instance.work = work
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
    
    # def get_success_url(self):
    #     if self.object.work:
    #         return reverse_lazy('work_detail', kwargs={'pk': self.object.work.pk})
    #     else:
    #         return reverse_lazy('work_list')
    success_url = reverse_lazy("home")


class ApplicationListView(ListView):
    model = Application
    template_name = "application_list.html"
    context_object_name = "applications"

class ApplicationDetailView(DetailView):
    model = Application
    template_name = "application_deatil.html"
    context_object_name = "application"

class ApplicationUpdateView(UpdateView):
    model = Application
    template_name = "application_update.html"
    fields = ['user', 'message', 'price', 'duration', 'status']

    def get_success_url(self):
        return reverse_lazy('work_detail', kwargs={'pk': self.object.pk})

class ApplicationDeleteView(DeleteView):
    model = Application
    template_name = "application_delete.html"
    
    def get_success_url(self):
        return reverse_lazy('work_detail', kwargs={'pk': self.object.pk})

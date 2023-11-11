from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Note
from .forms import CreateViewForm, UpdateViewForm



class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/home.html'
    context_object_name = 'notes' # the name of a context variable with the queryset results
    ordering = ['-date_posted']
    paginate_by = 1


    def get_queryset(self):
        search_query = self.request.GET.get('q', '')
        queryset = Note.objects.filter(Q(content__icontains=search_query) | Q(title__icontains=search_query), author=self.request.user).order_by('-date_posted')
        return queryset


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = CreateViewForm 
    template_name = 'notes/note_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        note = form.save()
        success_url = reverse('note_detail', kwargs={'pk': note.pk})
        return HttpResponseRedirect(success_url)
    



class NoteDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Note

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False
    

class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    template_name = 'notes/note_update.html'
    form_class = UpdateViewForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        note = form.save()
        success_url = reverse('note_detail', kwargs={'pk': note.pk})
        return HttpResponseRedirect(success_url)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    template_name = 'notes/note_delete.html'

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False
    
    def get_success_url(self):
        return reverse('home')
    

# defining actions when the CSRF error occurs
# the reason parameter here is optional and will only be displayed in logs
def csrf_failure(request, reason=""):
    current_page = request.path
    # iterating through all the pages that contain forms where the user can potentially encounter the CSRF error
    # and calling respective functions again
    try:
        if '/post/new' in current_page:
            return NoteCreateView.as_view()(request)
        elif '/update' in current_page:
            return NoteUpdateView.as_view()(request)
        elif '/delete' in current_page:
            return NoteDeleteView.as_view()(request)
        # redirect to the homepage in any other case, e.g. after login
        else:
            return HttpResponseRedirect('/')
    # if there was any error in calling the respective function, then redirect to the homepage
    except:
        return HttpResponseRedirect('/')

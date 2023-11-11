from django.forms.models import BaseModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView
from .models import CustomUser,Profile
from .forms import UserUpdateViewForm

class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'account/account.html'  # Change this to the template name you want to use

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = self.request.user  # Assumes a one-to-one relationship between CustomUser and Profile
        return context



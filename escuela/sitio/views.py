from django.shortcuts import render
from urllib import request
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView,UpdateView,DeleteView,ListView,TemplateView
from user.models import defaultUser

class home(TemplateView,LoginRequiredMixin,UserPassesTestMixin):
    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if hasattr(user, 'defaultuser'):
            context['user'] = user.defaultuser
        else:
            context['user'] = user
        return context

# class perfilUsuario(TemplateView,LoginRequiredMixin):
#     model = defaultUser
#     template_name = "base.html"
#     context_object_name = 'user' 
     
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user = self.request.user
#         if hasattr(user, 'defaultuser'):
#             context['user'] = user.defaultuser
#         else:
#             context['user'] = user
#         return context



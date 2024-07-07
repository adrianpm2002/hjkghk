from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from .models import Area, defaultUser as User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import UsuarioModelForm, UsuarioUpdateModelForm,login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import logout
from django.contrib import messages
# Create your views here.



#
# Gestion de usuarios
#

class UserLoginView(LoginView):
    template_name = 'login.html'
    
    def get_success_url(self):
        
        user = self.request.user     
        if user.is_authenticated and not user.is_staff:
            if  not User.objects.get(id = user.id):     
              return reverse_lazy('index')
            else:
              return reverse_lazy('index')
        return reverse_lazy('index')
    
class listUserView(LoginRequiredMixin ,ListView):
    model = User
    template_name = 'user_list.html'  
    context_object_name = 'users'  
    
    

    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if hasattr(user, 'defaultuser'):
            context['user'] = user.defaultuser
        else:
            context['user'] = user
        return context
    

class UserCreateView(CreateView):
    model = User
    template_name = 'default_create.html'
    form_class = UsuarioModelForm
    success_url = reverse_lazy('login')
    # def get_success_url(self):
    #     return reverse_lazy('list_actividad')
    # success_url = reverse_lazy('listar_usuario_rol')
    def form_valid(self, form):
        # Resto del código de la vista
        self.object = form.save()
        # Agregar mensaje de éxito
        messages.success(self.request, 'Registro satisfactorio')

        # Redirigir al usuario a la URL de éxito
        return redirect(self.get_success_url())
    
    
    def test_func(self):
        return self.request.user.is_staff
    def handle_no_permission(self):
        return redirect('login')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Usuario'
        return context
    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user

class userUpdateview(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'default_edit.html'
    form_class = UsuarioUpdateModelForm
    success_url = reverse_lazy('listar_usuario_rol')
    def form_valid(self, form):
        # Resto del código de la vista
        self.object = form.save()
        # Agregar mensaje de éxito
        messages.success(self.request, 'Modificación satisfactoria')

        # Redirigir al usuario a la URL de éxito
        return redirect(self.get_success_url())
    
    
    def test_func(self):
        return self.request.user.is_staff 
    def handle_no_permission(self):
        return redirect('login')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Usuario'
        return context
    
class userDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'default_delete.html'
    success_url = reverse_lazy('listar_usuario_rol')
    def form_valid(self, form):
        # Resto del código de la vista
        self.object = form.save()
        # Agregar mensaje de éxito
        messages.success(self.request, 'Eliminación satisfactoria')

        # Redirigir al usuario a la URL de éxito
        return redirect(self.get_success_url())
    
    
      
        
        
    
    def test_func(self):
        return self.request.user.is_staff
    def handle_no_permission(self):
        return redirect('login')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Usuario'
        return context
    

def salir(request):
    logout(request)
    return redirect("login")
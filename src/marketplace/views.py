from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Item, MarketCommunication
from .forms import ItemForm, MarketCommunicationForm
from django.http import JsonResponse
from profiles.models import Profile
# Lista de Items
class ItemListView(ListView):
    model = Item
    template_name = 'market/item_list.html'
    context_object_name = 'items'

# Detalles del Item
class ItemDetailView(DetailView):
    model = Item
    template_name = 'market/item_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = self.get_object()
        user = self.request.user.profile

        # Obtener los comentarios existentes para este usuario y artículo
        comments = MarketCommunication.objects.filter(user=user, item=item)

        # Si se envió el formulario, procesar los datos
        if self.request.method == 'POST':
            form = MarketCommunicationForm(self.request.POST)
            if form.is_valid():
                # Agregar el usuario y artículo al formulario antes de guardar
                instance = form.save(commit=False)
                instance.user = user
                instance.item = item
                instance.save()
                form = MarketCommunicationForm()
        else:
            form = MarketCommunicationForm()

        context['communication_form'] = form
        context['comments'] = comments
        return context
    
# Nuevo Item
class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'market/item_form.html'
    success_url = reverse_lazy('market:item-list')

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        form.instance.condition = form.cleaned_data['condition']
        form.instance.category = form.cleaned_data['category']
        form.instance.location = form.cleaned_data['location']
        return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['conditions'] = Item.CONDITION_CHOICES
    #     context['categories'] = Category.objects.all()
    #     context['locations'] = Location.objects.all()
    #     return context

# Actualizar Item
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'market/item_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

# Eliminar Item
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = 'market/item_confirm_delete.html'
    success_url = reverse_lazy('market:item-list')

# Comunicación con el vendedor
class MarketCommunicationCreateView(LoginRequiredMixin, CreateView):
    model = MarketCommunication
    form_class = MarketCommunicationForm
    template_name = 'market/communication_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user.profile
        form.instance.item = Item.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        item_pk = self.kwargs['pk']
        messages.success(self.request, 'Your message was sent successfully')
        return reverse_lazy('market:item-detail', kwargs={'pk': item_pk})
    
# GPT


from traceback import format_exc
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import logout, login
from django.urls import reverse, reverse_lazy
from .models import *
from .form import ingredient_form, menuItem_form, recipies_form, purcharse_form
# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView,self).get_context_data(**kwargs)
        #context['MenuItem']= MenuItem.objects.all() 
        #context['Ingredient'] = Ingredient.objects.all()
        context['Recepes'] = Recepes.objects.all()
        return context
        
class singUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("home")
    template_name = "registration/singup.html"

# Ingredientes


class IngredientListView(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "inventory/ingredient_list.html"


class CreateIngredientView(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = "inventory/add_ingredient.html"
    form_class = ingredient_form


class DeleteIngredientView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "inventory/delete_ingredient.html"

    def get_success_url(self):
        return reverse('ingredient')


class UpdateIngredientView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = "inventory/update_ingredient.html"
    form_class = ingredient_form

class MenuListView(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "inventory/menuItem_list.html"
   

class CreateMenuView(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = "inventory/add_menuItem.html"
    form_class = menuItem_form


class DeleteMenuView(LoginRequiredMixin, DeleteView):
    model = MenuItem
    template_name = "inventory/delete_menuItem.html"

    def get_success_url(self):
        return reverse('menu')


class CreateRecipie(LoginRequiredMixin, CreateView):
    model = Recepes
    template_name = "inventory/add_recipe.html"
    form_class = recipies_form


class PurcharseListView(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/purcharse_list.html"


class CreatePurcharseView(LoginRequiredMixin, CreateView):
   model = Purchase
   template_name ="inventory/add_purcharse.html"
   form_class = purcharse_form

   #def post(self,request):
   #  id_menu = request.POST["menu_item_id"]
   #  menu_item = MenuItem.objects.get(pk = id_menu)
   #  recepe_name = Recepes.objects.filter(menu_item_id = menu_item).first()
   #  ingredient = Ingredient.objects.filter(id = recepe_name.ingredient_id).first()
   #  ingredient.available_quantity -= ingredient


#Deberia mostrar todas las compras,
#agregar un form para que se pueda comprar 
#a partir del form modificar las cosas 

# 
#
#    for requirement in requirements.all():
#        required_ingredient = requirement.ingredient
#        required_ingredient.quantity -= requirement.quantity
#        required_ingredient.save()
#
#    purchase.save()
#    return redirect("/purchases")
#
# 
#
#
# Cua#ndo un cliente compra un artículo del menú, el inventario debe
# modificarse para acomodar lo sucedido,
# así como registrar la hora en que se realizó la compra.


class report(LoginRequiredMixin, ListView):
    ...

# el coste total
# del inventario, los ingresos totales del día, las diferentes
# compras que se han realizado y la cantidad de inventario que se
# necesita para reponer (como ejemplo inicial) para plasmarlos en una
# vista de Django.

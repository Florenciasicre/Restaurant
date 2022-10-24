from django import forms
from .models import Ingredient, MenuItem, Recepes, Purchase

class ingredient_form(forms.ModelForm):
  class Meta: 
    model = Ingredient
    fields = '__all__'

class menuItem_form(forms.ModelForm):
  class Meta: 
    model = MenuItem
    fields = '__all__'
  

class recipies_form(forms.ModelForm):
  class Meta: 
    model = Recepes
    fields = '__all__'

class purcharse_form(forms.ModelForm):
  class Meta:
    model = Purchase
    fields = '__all__'
    
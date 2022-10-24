from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('singUp/', views.singUp.as_view(), name='singup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ingredient/',views.IngredientListView.as_view(), name= 'ingredient'),
    path('ingredient/new/',views.CreateIngredientView.as_view(), name= 'add_ingredient'),
    path('ingredient/<pk>/delete',views.DeleteIngredientView.as_view(), name= 'delete_ingredient'),
    path('menu/', views.MenuListView.as_view(), name= 'menu'),
    path('menu/new/', views.CreateMenuView.as_view(), name='add_menu'),
    path('recipie/new/', views.CreateRecipie.as_view(), name='add_recipe'),
    path('purcharse/list/', views.PurcharseListView.as_view(), name='purcharse_list'),
    path('purcharse/new/', views.CreatePurcharseView.as_view(), name='new_purcharse'),
    

]
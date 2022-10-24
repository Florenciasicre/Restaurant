from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length= 20)
    available_quantity = models.FloatField()
    unit = models.CharField(max_length=15)
    price = models.FloatField()
    
    def __str__(self) -> str:
       return f"""{self.name}"""
       
    def get_absolute_url(self):
      return "/ingredient"

class MenuItem(models.Model):
    name_item = models.CharField(max_length= 20)
    price = models.FloatField()

    def available(self):
      return all(X.enough() for X in self.recipe_set.all())

    def get_absolute_url(self):
      return "/menu"
    def __str__(self):
        return f"""{self.name_item}"""

class Recepes(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete= models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete= models.CASCADE)
    quantity = models.FloatField()

    def enough(self):
      return self.quantity <= self.ingredient.available_quantity
    def __str__(self):
        return f"menu_item=[{self.menu_item.__str__()}]; ingredient={self.ingredient.name}; qty={self.quantity}"
    def get_absolute_url(self):
      return "/menu"
      
class Purchase(models.Model):
     menu_item = models.ForeignKey(MenuItem, on_delete= models.CASCADE)
     timestamp = models.DateTimeField(auto_now_add=True)
     
     def __str__(self) -> str:
      return f"menu_item=[{self.menu_item.__str__()}]; time={self.timestamp}"
     
     def get_absolute_url(self):
      return "/purcharse/list/"
     
     


from django.db import models

# Create your models here.


class Menu(models.Model):
    SECTION_CHOICES = [
        ('own_pizza', 'Create Your Own Pizza'),
        ('8_pizza', '8 Inch Specialty Pizza'),
        ('12_pizza', '12 Inch Thin Crust Specialty Pizza'),
        ('14_pizza', '14 Inch Specialty Pizza'),
        ('10_pizza', '10 Inch Gluten Free Specialty Pizza'),
        ('wing', 'Wings & Bites'),
        ('vegan', 'Vegan Variations'),
        ('bread_stick', 'Cheesy Bread Sticks'),
        ('healthy', 'Healthier Options'),
        ('sweet', 'Sweet Creations'),
        ('beverage', 'Beverages'),
        ('fryer', 'Out of the Fryer'),
        ('grill', 'Out of the Grill'),
        ('flatbread', 'Flatbread'),
        ('other', 'Others')
    ]
    section = models.CharField(
        max_length=15,
        choices=SECTION_CHOICES,
        default='other'
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    vegan = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    organic = models.BooleanField(default=False)
    kosher = models.BooleanField(default=False)
    halal = models.BooleanField(default=False)
    egg = models.BooleanField(default=False)        # Allergy
    peanut = models.BooleanField(default=False)     # Allergy
    treenut = models.BooleanField(default=False)    # Allergy
    fish = models.BooleanField(default=False)       # Allergy
    shellfish = models.BooleanField(default=False)  # Allergy
    soy = models.BooleanField(default=False)        # Allergy
    wheat = models.BooleanField(default=False)      # Allergy
    alcohol = models.BooleanField(default=False)
    glutenfree = models.BooleanField(default=False)

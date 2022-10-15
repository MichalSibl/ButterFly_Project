from email.policy import default
from itertools import product
from pyexpat import model
from statistics import quantiles
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Product(models.Model):
    CATEGORY_ACTION_FIGURES_AND_STATUES = "Action_Figures_and_Statues"
    CATEGORY_BOARD_GAMES = "Board_Games"
    CATEGORY_BUILDING_TOYS = "Building_Toys"
    CATEGORY_OUTDOOR_TOYS = "Outdoor_Toys"
    CATEGORY_PUZZLES_AND_BRAIN_TEASERS = "Puzzles_and_Brain_Teasers"
    CATEGORY_RPG_FIGURES = "RPG_Figures"
    CATEGORY_VEHICLES = "Vehicles"
    CATEGORY_OTHER_TOYS_AND_GAMES = "Other_Toys_and_Games"

    CATEGORY_CHOICES = (
        (CATEGORY_ACTION_FIGURES_AND_STATUES, "Action_Figures_and_Statues"),
        (CATEGORY_BOARD_GAMES, "Board_Games"),
        (CATEGORY_BUILDING_TOYS, "Building_Toys"),
        (CATEGORY_OUTDOOR_TOYS, "Outdoor_Toys"),
        (CATEGORY_PUZZLES_AND_BRAIN_TEASERS, "Puzzles_and_Brain_Teasers"),
        (CATEGORY_RPG_FIGURES, "RPG_Figures"),
        (CATEGORY_VEHICLES, "Vehicles"),
        (CATEGORY_OTHER_TOYS_AND_GAMES, "Other_Toys_and_Games")
    )
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=256)
    price = models.FloatField(default=20, blank=True)
    release_data = models.DateField()
    quantity = models.IntegerField(default=1)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} : {self.id}"
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = '/static/images/placeholder.png'
        return url

    @property
    def get_total(self):
        total = self.price * self.quantity
        return total

    @property
    def get_cart_total(self):
        orderitems = self.cart.product.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class Cart(models.Model):
        products = models.ManyToManyField(
            Product, related_name="carts"
        )
        user = models.OneToOneField(
            get_user_model(),
            related_name="cart",
            on_delete=models.CASCADE
        )

        class Meta:
            permissions = (
                ("add_product_to_cart", "Add product to cart"),
            )



class ProductReview(models.Model):
    product = models.ForeignKey(
        Product, related_name="reviews",
        on_delete=models.CASCADE
    )
    score = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    user = models.ForeignKey(
        get_user_model(), related_name="user_reviews",
        on_delete=models.CASCADE
    )
    text = models.TextField()


class HelpdeskContact(models.Model):
    email = models.EmailField()
    title = models.CharField(max_length=512)
    text = models.TextField()
    solved = models.BooleanField(default=False)


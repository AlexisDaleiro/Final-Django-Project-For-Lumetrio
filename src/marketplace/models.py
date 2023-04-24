from django.db import models
from profiles.models import Profile
from django.core.validators import  FileExtensionValidator
from django.urls import reverse
# Create your models here.


STATUS_CHOICES = (
    ('sold','sold'),
    ('available','available'),
)

class Item(models.Model):
    item_name = models.CharField(max_length=200)
    desc = models.TextField(max_length=500)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='market')
    image = models.ImageField(upload_to='market', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    created = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    market_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    condition = models.CharField(max_length=20, default='no se especifica')
    category = models.CharField(max_length=20, default='no se especifica')
    location = models.CharField(max_length=40, default='indefinida')

    def __str__(self):
        return f"{self.item_name}-{self.get_author_name()}"

    def get_author_name(self):
        # Obtenemos el nombre de usuario del autor sin la fecha
        return f"{self.author.user.username}"

    def get_absolute_url(self):
        return reverse("market:item-detail", kwargs={"pk": self.pk})

    def get_price_display(self):
        return f"${self.price}"

    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/static/images/default-image.jpg'

    def is_available(self):
        return self.market_status == 'available'

    def is_sold(self):
        return self.market_status == 'sold'

    def mark_as_sold(self):
        self.market_status = 'sold'
        self.save()

INTEREST_CHOICES = (
    ('Im interested', 'Im Interested'),
    ('Im not interested', 'Im not interested'),
)

class MarketCommunication(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    comment = models.TextField(default='')
    email = models.EmailField(max_length=80, blank=True)
    name = models.CharField(max_length=50, blank=True)
    value = models.CharField(choices=INTEREST_CHOICES, max_length=25, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}-{self.item}-{self.value}"
    

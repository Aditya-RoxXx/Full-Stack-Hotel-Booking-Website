from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name
    
class Room(models.Model):
    category = models.ForeignKey(Category, related_name='rooms', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='room_images', blank=True, null=True)
    is_booked = models.BooleanField(default=False)
    rented_by = models.ForeignKey(User, related_name='rooms', on_delete=models.CASCADE)
    rented_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Payment(models.Model):
    user = models.ForeignKey(User, related_name='payments', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='payments', on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50, choices=[
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
    ])

    def __str__(self):
        return f'{self.user} - {self.room.name} - {self.amount}'



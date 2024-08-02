from django.db import models
 
class Vegetable(models.Model):
    CATEGORY_CHOICES = [
        ('domestic', 'Domestic'),
        ('commercial', 'Commercial'),
    ]
    image_url = models.URLField(max_length=500)  # Store the URL of the image
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)  # Weight in grams
    # cutting_type = models.CharField(max_length=20, choices=[
    #     ('slice', 'Slice'),
    #     ('cube', 'Cube'),
    #     ('rectangle', 'Rectangle'),
    # ])
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
 
    def __str__(self):
        return self.name

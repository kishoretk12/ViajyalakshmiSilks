from django.db import models

class Saree(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class SareeImage(models.Model):
    saree = models.ForeignKey(Saree, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='saree_images/')

    def __str__(self):
        return f"Image for {self.saree.name}"


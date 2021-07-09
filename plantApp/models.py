
from django.db import models
from django.urls import reverse

# Create your models here.

class Plant(models.Model):
    name                =   models.CharField(max_length = 100)
    created_at          =   models.DateTimeField(auto_now_add = True)
    picture             =   models.ImageField(upload_to = 'uploaded_plant_images')
    disease_identified  =   models.CharField(max_length = 100, editable = False)

    def get_absolute_url(self):
        return reverse("plant-detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Plant'
        verbose_name_plural = 'Plants'
        ordering = ('-created_at',)

    def __str__(self):
        return (self.name +" "+self.disease_identified)
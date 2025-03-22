from django.db import models

from cloudinary.models import CloudinaryField


class Categorie(models.Model):
  nom = models.CharField(max_length=50)
  image = CloudinaryField('image')
  
  
  
  class Meta:
    verbose_name = ('Categorie')
    verbose_name_plural = ('Categories')
    
  def __str__(self):
      return self.nom

    
class Place(models.Model):
  nom_lieu = models.CharField(max_length=100)
  ville = models.CharField(max_length=100)
  date_ajout = models.DateTimeField(auto_now=True)
  localisation = models.CharField(max_length=200)
  categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=False, related_name='places')
  
  class Meta:
    verbose_name = ('Place')
    verbose_name_plural = ('Places')
    
  def __str__(self):
      return self.nom_lieu
# Create your models here.

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone


class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom
class Article(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    auteur = models.CharField(max_length=100)  # ✅ Champ manuel
    contenu = models.TextField()
    nombre_vues= models.PositiveSmallIntegerField(default=0)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('article_detail', args=[self.id, self.slug])
    
class ImageService(models.Model):
    image = models.ImageField(upload_to='services/gallery/')
    
class Service(models.Model):
    titre = models.CharField(max_length=100)
    Description = models.TextField()
    image_principale = models.ImageField(upload_to='services/',null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.titre
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.titre
 
from django.db import models

class ServiceCategorie(models.Model):
    nom= models.CharField(max_length=100)
    def __str__(self):
        return self.nom



class MessageContact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    date_envoye = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.sujet}"



from django.db import models
  # Assurez-vous que c'est le bon chemin d'import
class FAQ(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='faq')
    question = models.CharField(max_length=255)
    reponse = models.TextField()
    ordre = models.PositiveIntegerField(default=0, help_text="Ordre d'affichage (plus petit en premier)")
    class Meta:
        ordering = ['ordre', 'id']
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
    def __str__(self):
        return f"FAQ pour {self.service.titre}: {self.question}"


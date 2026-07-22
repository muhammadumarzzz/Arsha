from django.db import models

# Create your models here.

class Type(models.Model):
    nomi = models.CharField(max_length=30)
    def __str__(self):
        return self.nomi

class Portfolio(models.Model):
    nomi = models.CharField(max_length=30)
    company_name = models.CharField(max_length=50)
    date = models.DateField()
    url = models.URLField()
    malumot = models.TextField()
    tur = models.ForeignKey(Type, on_delete=models.CASCADE)
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media', null=True, blank=True)
    rasm3 = models.ImageField(upload_to='media', null=True, blank=True)

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Xizmat sarlavhasi")
    description = models.TextField(verbose_name="Xizmat tavsifi")
    icon_class = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        help_text="Masalan: bi bi-dribbble, bi bi-file-earmark-text, bi bi-speedometer2, bi bi-layers",
        verbose_name="Ikonka classi"
)
    order = models.IntegerField(default=0, verbose_name="Tartib raqami")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Xizmat"
        verbose_name_plural = "Xizmatlar"

    def __str__(self):
        return self.title


class TeamMember(models.Model):

    full_name = models.CharField(max_length=150, verbose_name="Ismi va familiyasi")

    position = models.CharField(max_length=100, verbose_name="Lavozimi")
    
    bio = models.TextField(verbose_name="Qisqacha ma'lumot")
    
    image = models.ImageField(upload_to='team/', verbose_name="Rasmi")

    twitter_url = models.URLField(blank=True, null=True, verbose_name="Twitter linki")
    facebook_url = models.URLField(blank=True, null=True, verbose_name="Facebook linki")
    instagram_url = models.URLField(blank=True, null=True, verbose_name="Instagram linki")
    linkedin_url = models.URLField(blank=True, null=True, verbose_name="LinkedIn linki")
    
    order = models.IntegerField(default=0, verbose_name="Tartib raqami")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Jamoa a'zosi"
        verbose_name_plural = "Jamoa a'zolari"

    def __str__(self):
        return f"{self.full_name} - {self.position}"

class Murojaat(models.Model):
    name = models.CharField(max_length=30)
    mail = models.EmailField(max_length=40)
    title = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
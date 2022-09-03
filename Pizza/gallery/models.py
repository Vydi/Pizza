from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify
from transliterate import translit


class Pizza(models.Model):
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='pizza/photos/%Y/%m/%d/', verbose_name='Фото', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(translit(self.title, 'ru', reversed=True))
        super(Pizza, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('details', kwargs={"slug": self.slug})  # построение ссылки

    def __str__(self):
        return self.title

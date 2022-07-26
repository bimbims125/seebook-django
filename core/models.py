from django.db import models
from django.forms import SlugField
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=55, blank=False)
    slug = models.SlugField(max_length=55)

    def __str__(self):
        return self.name

    # def save(self):
    #     self.slug = slugify(self.name)
    #     super(Category, self).save()


class Books(models.Model):
    title = models.CharField(max_length=55, blank=False)
    slug = models.SlugField(max_length=55)
    author = models.CharField(max_length=55, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    cover = models.ImageField(upload_to='cover')
    file = models.FileField(upload_to='pdf')

    def __str__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super(Books, self).save()
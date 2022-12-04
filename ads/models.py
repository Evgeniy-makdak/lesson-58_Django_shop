from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from users.models import User


class Category(models.Model):
    slag = models.CharField(max_length=10, validators=[MinLengthValidator(5)], unique=True)
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=200, validators=[MinLengthValidator(10)], blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    description = models.TextField(max_length=1500, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to="ads/", null=True, blank=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name


class Selection(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ad)

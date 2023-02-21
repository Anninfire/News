from django.db import models
from django.core.validators import MinValueValidator


# Товар для нашей витрины
class New(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True, # названия товаров не должны повторяться
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
    )
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news', # все продукты в категории будут доступны через поле products
    )

#    date = models.ForeignKey(
#        to='Date',
#        on_delete = models.CASCADE,
#        related_name = 'news',  # все продукты в категории будут доступны через поле products,
#    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:100]}'

#: {self.price}

# Категория, к которой будет привязываться товар
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=True)

#class Date(models.Model):
    # названия категорий тоже не должны повторяться
#    time = models.DateField(auto_created=True)


    def __str__(self):
        return self.name.title()
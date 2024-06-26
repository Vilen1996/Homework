from django.db import models

Drafts = (('Electric', 'Electric Urban Commuter'),
          ('Off-Road', 'Off-Road Adventure SUV'),
          ('Luxury', 'Luxury Autonomous Sedan'),
          ('Hybrid', 'Hybrid Family Crossover'),
          ('Performance', 'Performance Electric Sports Car'))

Colors = (('silver', 'Silver'),
          ('white', 'White'),
          ('black', 'Black'),
          ('blue', 'Blue'),
          ('red', 'Red'))


class Manufacture(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=30, unique=True)
    address = models.CharField(max_length=30,
                               default='Armenia')
    photo = models.ImageField(upload_to='media/cars/')
    draft = models.CharField(max_length=15, choices=Drafts)

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=30, unique=True)
    email = models.EmailField()
    phone = models.BigIntegerField()
    date = models.DateField
    draft = models.CharField(max_length=15, choices=Drafts)
    colors = models.CharField(max_length=15, choices=Colors)
    photo = models.ImageField(upload_to='media/cars/')

    def __str__(self):
        return self.name

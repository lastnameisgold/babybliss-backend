from django.db import models
from datetime import date


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Baby(models.Model):
    GENDER_CHOICES = (
        (1, 'Boy'),
        (2, 'Girl'),
    )
    name = models.CharField(max_length=100)
    dob = models.DateField(default=date.today)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Diaper(models.Model):
    DIAPER_CHOICES = (
        (1, 'Wet 💦'),
        (2, 'Dirty 💩'),
    )
    log = models.DateTimeField()
    diaper = models.IntegerField(choices=DIAPER_CHOICES, default=1)
    rash = models.BooleanField()
    notes = models.TextField(blank=True, default='')
    # baby = models.ForeignKey(Baby, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_diaper_display()} - {self.log.strftime('%Y-%m-%d %H:%M:%S')}"


class Feeding(models.Model):
    FEEDING_CHOICES = (
        (1, 'Bottle'),
        (2, 'Breast'),
    )
    log = models.DateTimeField()
    amount = models.PositiveIntegerField()
    method = models.IntegerField(choices=FEEDING_CHOICES, default=1)
    notes = models.TextField(blank=True, default='')

    def __str__(self):
        return f"{self.log.strftime('%Y-%m-%d %H:%M:%S')}"


class Affirmation(models.Model):
    message = models.TextField()

    def __str__(self):
        return self.message

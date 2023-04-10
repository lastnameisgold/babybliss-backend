from django.db import models

# Create your models here.


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
    age = models.PositiveIntegerField()
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
    notes = models.TextField()
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)

    def __str__(self):
        return self.type


class Feeding(models.Model):
    date = models.DateField()
    time = models.DateTimeField()
    duration = models.DurationField()
    amount = models.IntegerField()
    breastFed = models.BooleanField()
    bottleFed = models.BooleanField()
    notes = models.TextField()
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)

    def __str__(self):
        return self.type


class Affirmation(models.Model):
    date = models.DateField()
    message = models.TextField()

    def __str__(self):
        return self.message

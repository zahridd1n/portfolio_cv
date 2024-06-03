from django.db import models
from PIL import Image


class Home(models.Model):
    image = models.ImageField(upload_to='home/')
    icon1 = models.ImageField(upload_to='home/icon/')
    icon2 = models.ImageField(upload_to='home/icon/')
    title = models.CharField(max_length=155)
    description = models.CharField(max_length=255, blank=True, null=True)
    cv = models.FileField(upload_to='home/cv', null=True, blank=True)

    def __str__(self):
        return self.title


class AboutMe(models.Model):
    image = models.ImageField(upload_to='aboutme/')
    title = models.CharField(max_length=155)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    age = models.IntegerField()
    nationality = models.CharField(max_length=200)
    language = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class SocialMedia(models.Model):
    image = models.ImageField(upload_to='social/')
    url = models.URLField()
    title = models.CharField(max_length=155, blank=True, null=True)

    def __str__(self):
        return self.url


class Education(models.Model):
    major = models.CharField(max_length=233)
    university = models.CharField(max_length=233)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.university


class Experience(models.Model):
    position = models.CharField(max_length=233)
    company = models.CharField(max_length=233)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    body = models.TextField()


class Skills(models.Model):
    skill = models.CharField(max_length=100)
    percentage = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.percentage > 100:
            self.percentage = 100
        super(Skills, self).save(*args, **kwargs)


class Services(models.Model):
    icon = models.CharField(max_length=255, null=True, blank=True)  # font awsame yoki boshqasidan iconka clasi yoziladi
    title = models.CharField(max_length=155)
    body = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    title = models.CharField(max_length=155)
    body = models.TextField(blank=True)
    url = models.URLField(blank=True, null=True)
    language = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Blog(models.Model):
    image = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=48)
    description = models.CharField(max_length=255)
    tag = models.CharField(max_length=18)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)

            # Qirqish va o'lchamini o'zgartirish
            img = img.resize((370, 254), Image.Resampling.LANCZOS)
            img.save(self.image.path)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


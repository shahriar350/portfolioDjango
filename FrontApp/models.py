from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200, verbose_name="Your name")
    image = models.ImageField(verbose_name="Your profile image")
    profession = models.CharField(max_length=200)
    profile = HTMLField()
    cv = models.FileField(null=True, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    icon = models.TextField(verbose_name="SVG icon <svg></svg>",
                            help_text="Please height and width 25px is good. Change in svg tag.")

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    technology = models.CharField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    description = HTMLField()

    def __str__(self):
        return self.name


class Research(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.name


class Education(models.Model):
    type = models.CharField(max_length=200)
    institute = models.CharField(max_length=250)
    year = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    result = models.CharField(max_length=6)

    def __str__(self):
        return self.type + " " + self.year


class Training(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    topic = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    year = models.CharField(max_length=11)

    def __str__(self):
        return self.name


class MySkill(models.Model):
    name = models.CharField(max_length=200)
    icon = models.TextField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class LearningMap(models.Model):
    date = models.DateField()
    technology = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.date)


class BlogCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(BlogCategory, related_name="category_blog", on_delete=models.CASCADE)
    description = HTMLField()

    def __str__(self):
        return self.title


class KeyFocus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

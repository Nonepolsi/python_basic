from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from .utils import convert_ru_chars



class User(models.Model):

    name = models.CharField(max_length=30)
    bio = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True)


    class Meta:
        ordering = ["name"]


    def __str__(self):

        return self.name
    

    def get_absolute_url(self):

        return reverse("user", kwargs={"user_slug": self.slug})
    


class Quiz(models.Model):

    title = models.CharField(max_length=99, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True)


    class Meta:
        ordering = ["title"]


    def __str__(self):

        return self.title
    

    def get_absolute_url(self):

        return reverse("title", kwargs={"title_slug": self.slug})
    


class QuizQuestion(models.Model):

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    result = models.TextField(blank=True)


    def __str__(self):

        return self.text
    


class Result(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    num_correct = models.IntegerField(blank=True)
    num_wrong = models.IntegerField(blank=True)
    total = models.FloatField(blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True) # юзер + тест + время? Или оставить по праймери ки...


    class Meta:
        ordering = ["-date_time"]


    def __str__(self):

        return self.total
    

    def get_absolute_url(self):

        return reverse("result", kwargs={"result_slug": self.slug})
    

    def save(self, *args, **kwargs):
        
        if not self.id:
            temp_slug = str(self.date_time) + "-" + self.user.slug + "-" + convert_ru_chars(self.quiz.title)
            self.slug = slugify(temp_slug)
        
        super().save(*args, **kwargs)
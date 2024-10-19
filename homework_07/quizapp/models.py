from django.db import models



class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    bio = models.TextField()


    def __str__(self):
        return self.name
    


class Quiz(models.Model):
    title = models.CharField(max_length=99)


    def __str__(self):
        return self.title
    


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()
    result = models.TextField()


    def __str__(self):
        return self.text
    


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    num_correct = models.IntegerField()
    num_wrong = models.IntegerField()
    total = models.FloatField()


    def __str__(self):
        return self.total
    


#       User------------( )Result( )-------------Quiz--------------( )QuizQuestion
#     [results]           [user_id,        [quiz__questions,           [quiz_id]
#                          quiz_id]            results]
#
# Приложение для проверки знания слов
# Идея берет свое начало давно, когда я активно изучал иностранный язык (сейчас не хватает времени)
# Я выписывал слова из тем/уроков/заданий, и мне нужно было приложение, чтобы повторять эти слова
# Т.е. у меня есть список слов из какого-то урока (таких списков много)
# Я их каждый раз перемешиваю внутри списка (чтобы исключить заучивание последовательности)
# Мне надо по переводу (слову/выражению на русском) восстановить оригинал на иностранном
# Я реализовал это в виде корявого оффлайн приложения
# Теперь есть возможность релизовать это приложение, но уже в вебе
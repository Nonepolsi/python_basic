from django.contrib import admin

from .models import User, Result, Quiz, QuizQuestion


admin.site.register(User)
admin.site.register(Result)
admin.site.register(Quiz)
admin.site.register(QuizQuestion)

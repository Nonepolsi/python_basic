from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from quizapp.models import User, Result, Quiz, QuizQuestion



def index(request):
    context = {
        "body": "Я - главная страница :)"
    }
    return render(request, "quizapp/index.html", context=context)



class UserListView(ListView):
    model = User
    template_name = "quizapp/users.html"
    context_object_name = "users"



class UserDetailView(DetailView):
    model = User
    template_name = "quizapp/user.html"
    context_object_name = "user"



class ResultListView(ListView):
    model = Result
    template_name = "quizapp/results.html"
    context_object_name = "results"



class ResultDetailView(DetailView):
    model = Result
    template_name = "quizapp/result.html"
    context_object_name = "result"



class QuizListView(ListView):
    model = Quiz
    template_name = "quizapp/quiz_list.html"
    context_object_name = "quiz_list"



class QuizDetailView(DetailView):
    model = Quiz
    template_name = "quizapp/quiz.html"
    context_object_name = "quiz"



class QuizQuestionListView(ListView):
    model = QuizQuestion
    template_name = "quizapp/questions.html"
    context_object_name = "questions"



class QuizQuestionDetailView(DetailView):
    model = QuizQuestion
    template_name = "quizapp/question.html"
    context_object_name = "question"
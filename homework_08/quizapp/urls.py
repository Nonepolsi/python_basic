from django.urls import path

from . import views



urlpatterns = [
    path('', views.index, name="index"),
    path('users/', views.UserListView.as_view(), name="users"),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name="user"),
    path('results/', views.ResultListView.as_view(), name="results"),
    path('result/<int:pk>/', views.ResultDetailView.as_view(), name="result"),
    path('quiz_list/', views.QuizListView.as_view(), name="quiz_list"),
    path('quiz/<int:pk>/', views.QuizDetailView.as_view(), name="quiz"),
    path('quiz_questions_all/', views.QuizQuestionListView.as_view(), name="questions"),
    path('question/<int:pk>/', views.QuizQuestionDetailView.as_view(), name="question")
]
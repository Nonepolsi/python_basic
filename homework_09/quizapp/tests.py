from django.test import TestCase
from django.urls import reverse

from .models import User, Result, Quiz, QuizQuestion



class TestQuizApp(TestCase):

    def setUp(self) -> None:

        self.user = User.objects.create(
            name="Test_ser",
            email="test_user@mail.com",
            bio="Test_bio"
        )
    
        self.quiz = Quiz.objects.create(
            title="test_title",
            description="test_description"
        )

        self.question_1 = QuizQuestion.objects.create(
            text="test_text_1",
            result="test_result_1",
            quiz=self.quiz
        )
        
        self.question_2 = QuizQuestion.objects.create(
            text="test_text_2",
            result="test_result_2",
            quiz=self.quiz
        )

        self.question_3 = QuizQuestion.objects.create(
            text="test_text_3",
            result="test_result_3",
            quiz=self.quiz
        )

        self.result = Result.objects.create(
            quiz=self.quiz,
            user=self.user,
            num_correct = 2,
            num_wrong = 1,
            total = 0.667,
            date_time = "2024-11-04"
        )

        return super().setUp()
    

    def test_users_view(self):
        response = self.client.get(reverse("users"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "quizapp/users.html")
        self.assertIn("users", response.context)
        self.assertEqual(len(response.context['users']), User.objects.count())


    def test_user_view(self):
        response = self.client.get(reverse("user", kwargs={'pk': self.user.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "quizapp/user.html")
        self.assertIn("user", response.context)
        self.assertContains(response, self.user.bio)


    def test_quiz_list_view(self):
        response = self.client.get(reverse("quiz_list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "quizapp/quiz_list.html")
        self.assertIn("quiz_list", response.context)
        self.assertEqual(len(response.context['quiz_list']), Quiz.objects.count())


    def test_quiz_view(self):
        response = self.client.get(reverse("quiz", kwargs={'pk': self.quiz.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "quizapp/quiz.html")
        self.assertIn("quiz", response.context)
        self.assertContains(response, self.quiz.description)

    
    def test_quiz_questions_view(self):
        response = self.client.get(reverse("questions"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "quizapp/questions.html")
        self.assertIn("questions", response.context)
        self.assertEqual(len(response.context['questions']), QuizQuestion.objects.count())


    def test_quiz_question_view(self):
        response = self.client.get(reverse("question", kwargs={'pk': self.question_1.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "quizapp/question.html")
        self.assertIn("question", response.context)
        self.assertContains(response, self.question_1.result)


    def test_results_view(self):
        response = self.client.get(reverse("results"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "quizapp/results.html")
        self.assertIn("results", response.context)
        self.assertEqual(len(response.context['results']), Result.objects.count())


    def test_result_view(self):
        response = self.client.get(reverse("result", kwargs={'pk': self.result.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "quizapp/result.html")
        self.assertIn("result", response.context)
        self.assertContains(response, self.result.num_correct)


    def tearDown(self) -> None:

        Result.objects.all().delete()
        QuizQuestion.objects.all().delete()
        Quiz.objects.all().delete()
        User.objects.all().delete()

        return super().tearDown()
from quizapp.utils import navigation_bar


def get_quizapp_context(request):
    return {'navbar': navigation_bar}
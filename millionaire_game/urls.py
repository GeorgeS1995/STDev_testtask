from django.urls import path
from millionaire_game.views import WelcomeView, QuestionsView, ResultView

urlpatterns = [
    path('', WelcomeView.as_view(), name='index'),
    path('questions/<uuid:session>', QuestionsView.as_view(), name='question'),
    path('result/<uuid:session>', ResultView.as_view(), name='result'),
]

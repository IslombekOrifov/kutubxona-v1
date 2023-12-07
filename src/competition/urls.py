from django.urls import path

from . import views


urlpatterns = [
    path('participants/create/', views.CompetitionParticipantCreateAPIView.as_view()),
    path('question/list/', views.CompetitionQuestionListAPIView.as_view()),
    path('competition/list/', views.CompetitionRetriveAPIView.as_view()),
]

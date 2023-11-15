from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.layout, name='index'),
    path('hotQuestions', views.hotQuestions, name='hotQuestions'),
    path('addQuestion', views.addQuestion, name="addQuestion"),
    path('answersList/<int:question_id>', views.answersList, name='question'),
    path('tagQuestions/<selected_tag>', views.tagQuestions, name='tagsPage'),
    path('settingsPage', views.settingsPage, name='settings'),
    path('authorization', views.authorization, name='authorization'),
    path('registration', views.registration, name='registration'),
]

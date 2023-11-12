"""
URL configuration for AskQuestions project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.layout, name='index'),
    path('addQuestion', views.addQuestion),
    path('answersList/<int:question_id>', views.answersList, name='question'),
    path('tagQuestions', views.tagQuestions),
    path('settingsPage', views.settingsPage),
    path('authorization', views.authorization),
    path('registration', views.registration),
    path('admin/', admin.site.urls),
]

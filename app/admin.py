from django.contrib import admin
import django.contrib.admin

from .models import Question, Tag, Answer, Profile, Like

admin.site.register(Question)
admin.site.register(Tag)
admin.site.register(Answer)
admin.site.register(Profile)
admin.site.register(Like)


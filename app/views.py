from django.shortcuts import render
from django.core.paginator import Paginator

QUESTIONS = [
        {
            'id': i,
            'title': f'Question {i}',
            'content': f'Long Lorem ipsum {i}'
        } for i in range(20)
    ]

def paginate(objects, page, per_page = 15):
    paginator = Paginator(objects, per_page)
    return paginator.page(page)


def layout(request):
    page = request.GET.get('page', 1)
    return render(request, 'layout.html', {'questions': paginate(QUESTIONS, page)})


def addQuestion(request):
    return render(request, 'addQuestion.html')


def answersList(request, question_id):
    item = QUESTIONS[question_id]
    return render(request, 'answersList.html', {'question': item})


def tagQuestions(request):
    return render(request, 'tagQuestions.html')


def settingsPage(request):
    return render(request, 'settingsPage.html')


def authorization(request):
    return render(request, 'authorization.html')


def registration(request):
    return render(request, 'registration.html')

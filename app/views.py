from django.shortcuts import render
from django.core.paginator import Paginator

questionsCount = 20
questionsCountOnOnePage = 10

QUESTIONS = [
    {
        'id': i,
        'title': f'Question {i}',
        'content': f'A standard guitar has six strings made of various materials such as nylon, steel, or a combination of both (classical guitars, for example, would typically use nylon). The top three strings, also known as the treble strings, are typically made of plain steel, while the bottom three strings, also known as the bass strings, are made of a steel core wrapped in a thin layer of metal such as bronze or nickel. The thickness of each string determines its pitch.'
    } for i in range(questionsCount)
]

PAGES = [
    {
        'id': i,
        'content': f'{i}'
    } for i in range(2, questionsCount // questionsCountOnOnePage + 1)
]


def paginate(objects, page, per_page=questionsCountOnOnePage):
    paginator = Paginator(objects, per_page)
    return paginator.page(page)


def layout(request):
    page: object = request.GET.get('page', 1)
    return render(request, 'layout.html', {'questions': paginate(QUESTIONS, page), 'pages': PAGES})


def addQuestion(request):
    return render(request, 'addQuestion.html')


def answersList(request, question_id):
    item = QUESTIONS[question_id]
    page: object = request.GET.get('page', 1)
    return render(request, 'answersList.html',
                  {'question': item, 'questions': paginate(QUESTIONS, page), 'pages': PAGES})


def tagQuestions(request):
    page: object = request.GET.get('page', 1)
    return render(request, 'tagQuestions.html', {'questions': paginate(QUESTIONS, page), 'pages': PAGES})


def settingsPage(request):
    return render(request, 'settingsPage.html')


def authorization(request):
    return render(request, 'authorization.html')


def registration(request):
    return render(request, 'registration.html')

import math
from django.shortcuts import render
from django.core.paginator import Paginator

questionsCount = 100
PER_PAGE = 10

QUESTIONS = [
    {
        'id': i,
        'title': f'Question {i}',
        'content': f'A standard guitar has six strings made of various materials such as nylon, steel,'
                   f' or a combination of both (classical guitars, for example, would typically use nylon). '
                   f'The top three strings, also known as the treble strings, are typically made of plain steel, '
                   f'while the bottom three strings, also known as the bass strings, are made of a steel core wrapped '
                   f'in a thin layer of metal such as bronze or nickel. The thickness of each string determines its pitch.',
        'tag': []
    } for i in range(questionsCount)
]

for i in range(questionsCount):
    if i % 2 == 0:
        QUESTIONS[i]['tag'] = ['VK', 'HTML', 'BOOTSTRAP']
    else:
        QUESTIONS[i]['tag'] = ['mathematics', 'Pycharm', 'Guitars']


def paginate(objects, request, per_page=PER_PAGE):
    paginator = Paginator(objects, per_page)
    page: object = request.GET.get('page', 1)
    try:
        if int(page) <= 0:
            page = 1
        elif int(page) > len(QUESTIONS) // per_page and len(QUESTIONS) % per_page == 0:
            page = len(QUESTIONS) // per_page
        elif int(page) > len(QUESTIONS) // per_page + 1:
            if len(QUESTIONS) % per_page == 0:
                page = len(QUESTIONS) // per_page
            else:
                page = len(QUESTIONS) // per_page + 1
    except:
        page = 1
    return [paginator.page(page), int(page)]


def get_paginator(current_page, count):
    start_page = max(current_page - 4, 1)
    end_page = min(current_page + 4, count)
    arr = [i for i in range(start_page, end_page + 1)]
    return arr


def layout(request):
    arr_paginate = paginate(QUESTIONS, request)
    count = pages_count(len(QUESTIONS))
    current_page = arr_paginate[1]
    paginator_items = get_paginator(current_page, count)
    return render(request, 'layout.html',
                  {'questions': arr_paginate[0],
                   'current_page': current_page,
                   'pages_count': count,
                   'paginator': paginator_items
                   })


def pages_count(objects, per_page=PER_PAGE):
    return math.ceil(objects / per_page)


def hotQuestions(request):
    arr_paginate = paginate(QUESTIONS, request)
    count = pages_count(len(QUESTIONS))
    current_page = arr_paginate[1]
    paginator_items = get_paginator(current_page, count)
    return render(request, 'hotQuestions.html',
                  {'questions': arr_paginate[0],
                   'current_page': current_page,
                   'pages_count': count,
                   'paginator': paginator_items
                   })


def answersList(request, question_id):
    arr_paginate = paginate(QUESTIONS, request)
    count = pages_count(len(QUESTIONS))
    current_page = arr_paginate[1]
    paginator_items = get_paginator(current_page, count)
    item = QUESTIONS[question_id]
    return render(request, 'answersList.html',
                  {'question': item,
                   'questions': arr_paginate[0],
                   'current_page': current_page,
                   'pages_count': count,
                   'paginator': paginator_items
                   })


def tagQuestions(request, selected_tag):
    questions_list = []
    for item in QUESTIONS:
        if selected_tag in item['tag']:
            questions_list.append(item)
    arr_paginate = paginate(questions_list, request)
    count = pages_count(len(questions_list))
    current_page = arr_paginate[1]
    paginator_items = get_paginator(current_page, count)
    return render(request, 'tagQuestions.html',
                  {'questions': arr_paginate[0],
                   'current_page': current_page,
                   'pages_count': count,
                   'paginator': paginator_items,
                   'selected_tag': selected_tag})


def addQuestion(request):
    return render(request, 'addQuestion.html')


def settingsPage(request):
    return render(request, 'settingsPage.html')


def authorization(request):
    return render(request, 'authorization.html')


def registration(request):
    return render(request, 'registration.html')

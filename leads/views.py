from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    # return HttpResponse('Hello')
    context = {
        'name': 'John',
    }
    return render(request, 'second_page.html', context)

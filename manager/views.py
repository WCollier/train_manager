from django.shortcuts import render


def index(request):
    context = {
        'test': 'hello, world'
    }

    return render(request, 'manager/index.html', context)

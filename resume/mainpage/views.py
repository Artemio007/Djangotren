from django.shortcuts import render, redirect
from .models import Revo
from .forms import RevoForm


def main1(request):
    return render(request, 'mainpage/main1.html')


def index(request):
    return render(request, 'mainpage/index.html')


def me(request):
    return render(request, 'mainpage/page1.html')


def projects(request):
    return render(request, 'mainpage/projects.html')


def game(request):
    return render(request, 'mainpage/The game.html')


def reviews(request):

    about = Revo.objects.order_by('-id')
    return render(request, 'mainpage/reviews.html', {'revlist': about})


def btnrev(request):
    error = ''
    if request.method == 'POST':
        form = RevoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('reviews')
        else:
            error = 'Form is not correct'
    form = RevoForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'mainpage/bd.html', context)
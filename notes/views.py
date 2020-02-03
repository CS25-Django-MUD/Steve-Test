from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.  Each view, represents the expected output for a given url end point
# by default, django looks for a 'templates' subdirectory within the app.  to render html, create a templates directory within the app.
# app templates file structure - app --> templates directory -- > appname directory --> templates.html files

# To access data returned from a data call (i.e. api request), we can store it in a variable within the related view function and pass it as a third argument which will give the associated template access to that data based on the dict key. 

# example data response:
hotnotes = [
    {
        'subject': 'Math',
        'author': 'Albert Einstein',
        'note': 'E is equal to MC squared',
        'date_posted': 'should use datetime package to generate this!'
    },
    {
        'subject': 'Science',
        'author': 'Stephen Hawking',
        'note': 'Intelligence is the ability to adapt to change.',
        'date_posted': 'As stated before, should use datetime package to generate this!'
    },
]

def home(request):
    context = {
        'mynotes': hotnotes
    }
    return render(request, 'notes/home.html', context)

def about(request):
    return render(request, 'notes/about.html')
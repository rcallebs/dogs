from django.shortcuts import render

dogs = [
  {'name': 'Layla', 'breed': 'Pitbull', 'description': 'Ghostface', 'age': 10},
  {'name': 'Bram', 'breed': 'Swedish Mountain Dog', 'description': 'Dumb and friendly', 'age': 3},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html', {
        'dogs': dogs
    })

def dogs_index(request):
    return render(request, 'dogs/index.html', {
        'dogs': dogs
    })
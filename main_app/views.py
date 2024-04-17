from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Dog, Trait
from .forms import FeedingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    dogs = Dog.objects.all()
    return render(request, 'about.html', {
        'dogs': dogs
    })

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {
        'dogs': dogs
    })

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    # list of all traits dog currently has
    id_list = dog.traits.all().values_list('id')
    traits_not_had = Trait.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'dogs/detail.html', {
        'dog': dog, 'feeding_form': feeding_form,
         'traits': traits_not_had })

def add_feeding(request, dog_id):
      # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
    # don't save the form to the db until it
    # has the dog_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.dog_id = dog_id
        new_feeding.save()
    return redirect('detail', dog_id=dog_id)

def assoc_trait(request, dog_id, trait_id):
    Dog.objects.get(id=dog_id).traits.add(trait_id)
    return redirect('detail', dog_id=dog_id)

def remove_trait(request, dog_id, trait_id):
    Dog.objects.get(id=dog_id).traits.remove(trait_id)
    return redirect('detail', dog_id=dog_id)

class DogCreate(CreateView):
    model = Dog
    fields = ['name', 'breed', 'description', 'age']

class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs'

class TraitList(ListView):
    model = Trait

class TraitDetail(DetailView):
    model = Trait

class TraitCreate(CreateView):
    model = Trait
    fields = ['name', 'description']

class TraitUpdate(UpdateView):
    model = Trait
    fields = ['name', 'description']

class TraitDelete(DeleteView):
    model = Trait
    success_url = '/traits'
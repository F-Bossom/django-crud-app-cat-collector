from django.shortcuts import render, redirect
from .models import Cat, Toy # * imports everything
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import FeedingForm
from django.urls import reverse


# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

# # Create a list of Cat instances
# cats = [
#     Cat('Lolo', 'tabby', 'Kinda rude.', 3),
#     Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
#     Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
#     Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
# ]


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cat_index(request, pk):
    cats = Cat.objects.all(pk)

    return render(request, 'cats/detail.html', {
        'cat': cats,
    })

def cat_detail(request, pk):
    cats = Cat.objects.get(id=pk)
    feeding_form = FeedingForm() # new instance of the form
    toys = Toy.objects.exclude(id__in = cats.toy.all().values_list('id'))

    return render(request, 'cats/detail.html', {
        'cat': cats,
        'feeding_form': feeding_form, # pass the form to the template
        'toys': toys # this should show toys the cat does not own
    })

def add_feeding(request, cat_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('cat-detail', pk=cat_id)

def associate_toy(request, cat_id, toy_id):
    Cat.objects.get(id=cat_id).toy.add(toy_id)
    return redirect('cat-detail', pk=cat_id)


# CBV Class Based Views

'''
ListView - list stuff
CreateView - create stuff
DeleteView - delete stuff
UpdateView - update stuff
DetailView - show page
'''

# Listing
class CatList(ListView):
    model = Cat
    # By default Listview will look for a template in the path
    #  <your_app_name>/<modelname>_list.html
    #  AKA we made a templates/main_app/cal_list.html

    # or we override that default by providing a new path
    template_name = 'cats/index.html'

class CatCreate(CreateView):
    model = Cat
    # Lets createview know which fields to use
    # fields = '__all__'
    # or a list
    fields = ['name', 'breed', 'description', 'age']
    # success_url='/cats/'


# Detail
class CatDetail(DetailView):
    model = Cat
    template_name='cats/detail.html'

# Delete
class CatDelete(DeleteView):
    model=Cat
    success_url='/cats'

# Update
class CatUpdate(UpdateView):
    model=Cat
    fields=['breed', 'description', 'age']


# Get /toy/create and Post /toy/create
class ToyCreate(CreateView):
    model = Toy
    fields= "__all__"

class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/detail.html'

class ToyList(ListView):
    model = Toy
    template_name = 'toys/index.html'

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'
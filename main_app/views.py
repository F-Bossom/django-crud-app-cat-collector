from django.shortcuts import render
from .models import Cat
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

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

def cat_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})

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
from django.shortcuts import render
# Import HttpResponse to send text-based responses
from django.http import HttpResponse
from .models import Cat
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# views.py

# Removed the custom Cat class to avoid conflicts with the Cat model

# # Create a list of Cat instances replaced later with database queries
# cats = [
#     Cat('Lolo', 'tabby', 'Kinda rude.', 3),
#     Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
#     Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
#     Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
# ]

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

# about view
def about(request):
    return render(request, 'about.html')

def cats_index(request):
    cats = Cat.objects.all()  # look familiar?
    # Render the cats/index.html template with the cats data
    return render(request, 'cats/index.html', {'cats': cats})

def cats_detail(request, cat_id):
    # Get the specific cat by id
    cat = Cat.objects.get(id=cat_id)
    # Render the cats/detail.html template with the cat data
    return render(request, 'cats/detail.html', {'cat': cat})

def cat_detail(request, cat_id):
    # Fetch the specific cat by ID
    cat = Cat.objects.get(id=cat_id)
    # Render the detail template with the cat data
    return render(request, 'cats/detail.html', {'cat': cat})


# 
class CatCreate(CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']
    # success_url = '/cats/'  # Redirect to the cats index after successful creation
    failure_url = '/cats/create/'  # Redirect back to the create form on failure

class CatUpdate(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']
    # success_url = '/cats/'  # Redirect to the cats index after successful update
    failure_url = '/cats/<int:pk>/update/'  # Redirect back to the update form on failure
class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'  # Redirect to the cats index after successful deletion
    failure_url = '/cats/<int:pk>/delete/'  # Redirect back to the delete confirmation on failure
from django.shortcuts import render, redirect
# Import HttpResponse to send text-based responses
from django.http import HttpResponse
from .models import Cat, Toy
# Import the FeedingForm
from .forms import FeedingForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

# about view
def about(request):
    return render(request, 'about.html')

# cats index view
def cats_index(request):
    cats = Cat.objects.all()  # look familiar?
    # Render the cats/index.html template with the cats data
    return render(request, 'cats/index.html', {'cats': cats})

# single cat page
def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    # Only get the toys the cat does not have
    toys_cat_doesnt_have = Toy.objects.exclude(id__in=cat.toys.all().values_list('id'))

    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {
        'cat': cat,
        'feeding_form': feeding_form,
        'toys': toys_cat_doesnt_have  # Pass the correct variable to the template
    })


# Add a feeding from a details page
def add_feeding(request, cat_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_feeding = form.save(commit=False)
        # assign the cat_id to the feeding
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('cat-detail', cat_id=cat_id)
# Associate a toy with a cat (M2M relationship)
def associate_toy(request, cat_id, toy_id):
    # Note that you can pass a toy's id instead of the whole object
    Cat.objects.get(id=cat_id).toys.add(toy_id)
    return redirect('cat-detail', cat_id=cat_id)
# Remove a toy from a cat
def remove_toy(request, cat_id, toy_id):
    # Look up the cat
    cat = Cat.objects.get(id=cat_id)
    # Look up the toy
    toy = Toy.objects.get(id=toy_id)
    # Remove the toy from the cat
    cat.toys.remove(toy)
    return redirect('cat-detail', cat_id=cat.id)


# views for Cat model
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

# views for Toy model
class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy
class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

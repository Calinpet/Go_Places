from unicodedata import name
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Place, Photo
from .forms import VisitForm, DoingForm
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
import uuid
import boto3


 # Create your views here.
S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'go-places-calin'

def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def places_index(request):
  places = Place.objects.all()
  return render(request, 'places/index.html', { 'places': places }) 

def places_detail(request, place_id):
  place = Place.objects.get(id=place_id)
  visiting_form = VisitForm()
  todo_form = DoingForm()
  return render(request, 'places/detail.html', {'place': place, 'visiting_form': visiting_form, 'todo_form': todo_form
  })

def add_visit(request, place_id):
  form = VisitForm(request.POST)
  if form.is_valid():
    new_visit = form.save(commit=False)
    new_visit.place_id = place_id
    new_visit.save()
  return redirect('detail', place_id=place_id)

def add_todo(request, place_id):
  form = DoingForm(request.POST)
  if form.is_valid():
    new_todo = form.save(commit=False)
    new_todo.place_id = place_id
    new_todo.save()
  return redirect('detail', place_id=place_id)

def add_photo(request, place_id):
    # photo-file will be the "name" attribute on the <input 
    # attemp to collect the photo file data
    photo_file = request.FILES.get('photo-file', None)
    # use conditional logic to determine if file is present
    if photo_file:
        # if it's present, we will create a referance to the boto3 client
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        # create a unique id for each photo file
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        # upload the photo file to aws s3
        try:
            # if succesfull
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            # 1) create photo instance with photo model and provide cat_id as foreign key val
            photo = Photo(url=url, palce_id=place_id)
             # 2) save the photo instance to the database
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', place_id=place_id)         

class PlaceCreate(CreateView):
  model = Place
  fields = ['name', 'description'] 
  success_url = '/places/'
  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

class PlaceUpdate(UpdateView):
  model = Place
  fields = ['name', 'description'] 

class PlaceDelete(DeleteView):
  model = Place 
  success_url = '/places/' 



from django.shortcuts import render, redirect
from .models import Place
from django.views.generic.edit import CreateView
# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import VisitForm
from django.http import HttpResponse


 # Create your views here.


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
  return render(request, 'places/detail.html', {'place': place, 'visiting_form': visiting_form
  })

def add_visit(request, place_id):
  form = VisitForm(request.POST)
  if form.is_valid():
    new_visit = form.save(commit=False)
    new_visit.place_id = place_id
    new_visit.save()
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



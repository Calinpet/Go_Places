from django.forms import ModelForm
from .models import Visit, Doing


class VisitForm(ModelForm):
  class Meta:
    model = Visit
    fields = ['date', 'visited']

class DoingForm(ModelForm):
  class Meta:
    model = Doing
    fields = ['todo', 'complete']    
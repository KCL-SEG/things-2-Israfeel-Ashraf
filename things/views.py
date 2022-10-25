from django.shortcuts import render
from .forms import ThingForm
from .models import Thing

def home(request):

    if request.method == "POST":
        form = ThingForm(request.POST)
        if form.is_valid():
            form.clean()
            form.save()
            return render(request, 'home.html')

    else:
        form = ThingForm()

    return render(request, 'home.html', {'form' : form})

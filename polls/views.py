from django.shortcuts import render

from polls.forms import ProduktForm
from polls.models import Produkt


# Create your views here.

def index(request):
    return render(request, 'index.html')


def produkti(request):
    produkti = Produkt.objects.all()

    return render(request, 'produkti.html', {'produkti': produkti})

def add_produkt(request):
    if request.method == 'POST':
        form = ProduktForm(request.POST, request.FILES)
        if form.is_valid():
            produkt = form.save(commit=False)
            produkt.user = request.user
            produkt.save()
        else:
            form = ProduktForm()

        return render(request, "add_produkt.html", {"form": form})

from django.shortcuts import render, redirect
from .forms import DonorForm

def donate_blood(request):
    if request.method == "POST":
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = DonorForm()
    return render(request, 'donor/donate_form.html', {'form': form})

def thank_you(request):
    return render(request, 'donor/thank_you.html')

# Create your views here.

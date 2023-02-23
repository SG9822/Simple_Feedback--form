from django.shortcuts import render, redirect
from . forms import *
from . models import *

# Create your views here.

def index(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thankyou')    
            
    # form = FeedbackForm
    myform = {'form': form}
    return render(request, 'form/index.html', myform)

def thankyou(request):
    return render(request, 'form/thankyou.html')

    
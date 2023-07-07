from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import CustomerFeedback


def welcome(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = FeedbackForm()
    feedback_list = CustomerFeedback.objects.all()
    return render(request, 'welcome.html', {'feedback_list': feedback_list})
    
def AboutUs (request):
    return render(request, 'AboutUs.html')

def ContactUs (request):
    return render(request, 'ContactUs.html')

def places (request):
    return render(request, 'places.html')

def save_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = FeedbackForm()

    return render(request, 'welcome.html', {'form': form})
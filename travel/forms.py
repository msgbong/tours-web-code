from django import forms
from .models import CustomerFeedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = CustomerFeedback
        fields = ['customer_name', 'country', 'service_views', 'rating']
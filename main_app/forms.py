from django.forms import ModelForm, DateInput
from .models import Feeding


class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal'] # or something like "__all__"
        widgets = {
            'date': DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': "Select A Date",
                    'type': 'date'
                }
            )
        }
        
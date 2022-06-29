from django import forms
from django.forms import ModelForm
from .models import Ticket, Review

RATING = (("0", ("0")),
          ("1", ("1")),
          ("2", ("2")),
          ("3", ("3")),
          ("4", ("4")),
          ("5", ("5")))


class TicketForm(ModelForm):
    title = forms.fields.CharField(max_length=128)
    description = forms.fields.CharField(max_length=2048, strip=False)
    images = forms.ImageField(required=False)

    class Meta:
        model = Ticket
        fields = [
            'title',
            'description',
            'images'
        ]


class ReviewForm(ModelForm):
    headline = forms.fields.CharField(max_length=128)
    body = forms.fields.CharField(max_length=8192, strip=False)
    rating = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect)

    class Meta:
        model = Review
        fields = [
            'headline',
            'body',
            'rating'
        ]

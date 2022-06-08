from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from reviews.forms import TicketForm, ReviewForm


@login_required
def create_review(request):
    if request.POST:
        review_form = ReviewForm(request.POST)
        ticket_form = TicketForm(request.POST, request.FILES)
        if review_form.is_valid() and ticket_form.is_valid():
            print(request.POST)

            ticket_form.save()
            review_form.save()
            return redirect('/flow')


    else:
        review_form = ReviewForm()
        ticket_form = TicketForm()

    return render(request, 'create.html',
          {'ReviewForm': review_form, 'RequestForm': ticket_form})

@login_required
def request_review(request):
    if request.POST:
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            print(request.POST)
            ticket_form.save()
            return redirect('/flow')

    else:
        ticket_form = TicketForm()

    return render(request, 'request.html',
          {'RequestForm': ticket_form})

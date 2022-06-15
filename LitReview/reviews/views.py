from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from reviews.forms import TicketForm, ReviewForm
from .models import Ticket, Review


@login_required
def create_review(request):
    if request.POST:
        review_form = ReviewForm(request.POST, request.user)
        ticket_form = TicketForm(request.POST, request.FILES, request.user)
        if review_form.is_valid() and ticket_form.is_valid():
            print(request.POST)

            user = request.user
            title = request.POST['title']
            description = request.POST['description']
            images = request.POST['images']
            headline = request.POST['headline']
            body = request.POST['body']
            

            ticket = Ticket.objects.create(user=user, title=title, description= description, images=images)
            review = Review.objects.create(user=user, ticket=ticket, headline=headline, body=body)
            
            ticket.save()
            review.save()

            return redirect('/flow')


    else:
        review_form = ReviewForm()
        ticket_form = TicketForm()

    return render(request, 'create.html',
          {'ReviewForm': review_form, 'RequestForm': ticket_form})

@login_required
def request_review(request):
    if request.POST:
        ticket_form = TicketForm(request.POST, request.FILES, request.user)
        if ticket_form.is_valid():
            print(request.POST)

            user = request.user
            title = request.POST['title']
            description = request.POST['description']
            images = request.POST['images']


            ticket = Ticket.objects.create(user=user, title=title, description= description, images=images)
            ticket.save()

            return redirect('/flow')

    else:
        ticket_form = TicketForm()

    return render(request, 'request.html',
          {'RequestForm': ticket_form})

def delete_ticket(request, id):
    ticket = Ticket.objects.get(pk=id)
    ticket.delete()
    return redirect('/flow/posts')

def delete_review(request, id):
    review = Review.objects.get(pk=id)
    review.delete()
    return redirect('/flow/posts')

def modify_ticket(request, id):
    ticket = Ticket.objects.get(pk=id)
    print(ticket.title)
    form = TicketForm(request.POST or None, instance=ticket)
    if form.is_valid():
        form.save()
        return redirect('/flow/posts')
    return render(request, 'modif_request.html',{'ticket': ticket,'form': form})

def modify_review(request, id):
    review = Review.objects.get(pk=id)
    form = ReviewForm(request.POST or None, instance=review)
    if form.is_valid():
        form.save()
        return redirect('/flow/posts')
    return render(request, 'modif_create.html',{'review': review, 'form': form})
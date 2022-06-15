from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from flow.forms import FollowUsersForm
from reviews.models import Ticket, Review
from django.db.models import CharField, Value
from itertools import chain

@login_required
def main_flow(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()

    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created, 
        reverse=True
    )
    return render(request, 'flux.html', context={'posts': posts})

@login_required
def posts_page(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()

    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created, 
        reverse=True
    )
    return render(request, 'posts.html', context={'posts': posts})

@login_required
def subcription_page(request):
    followform = FollowUsersForm(instance=request.user)
    if request.method == 'POST':
        form = FollowUsersForm(request.POST, instance=request.user)
        if form.is_valid():
            print(request.POST)

            form.save()
    return render(request, 'subcription.html', context={'followform': followform})
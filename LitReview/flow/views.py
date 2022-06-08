from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def main_flow(request):

    return render(request, 'flux.html', {})

@login_required
def posts_page(request):

    return render(request, 'posts.html', {})

@login_required
def subcription_page(request):

    return render(request, 'subcription.html', {})
from django.shortcuts import render, redirect
# Create your views here.
def intro(request):
    return render(request, 'Introduction/intro.html')
def guide(request):
    return render(request, 'Introduction/guide.html')

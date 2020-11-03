from django.shortcuts import render
# Create your views here.
def search(request):
    return render(request, 'selector/search.html')

def edit(request):
    return render(request, 'selector/edit.html')

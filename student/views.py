from django.shortcuts import render

# Create your views here.

def studenthome(request):
    return render(request, 'index.html')

def notice(request):
    return render(request, 'notice.html')

def progress(request):
    return render(request, 'progress.html')

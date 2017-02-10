from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def qa_page(request):
    return render(request, 'main/qa_page.html')


def working(request):
    return render(request, 'main/working.html')

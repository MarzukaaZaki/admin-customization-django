from django.shortcuts import render
from .models import Category

# Create your views here.
def indexView(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request, 'categorymanager/index.html', context)

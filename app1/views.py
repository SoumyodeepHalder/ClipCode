from django.shortcuts import render, redirect, get_object_or_404
from app1.models import Snippet

# Create your views here.

def index(request):
    return render(request, 'index.html', {'snippets': Snippet.objects.all()})

def addpage(request):
    return render(request, 'addpage.html')

def add(request):
    title = request.POST.get('title', 'code heading')
    code = request.POST.get('code', 'default code')
    Snippet.objects.create(title=title, code=code)

    return redirect('app1:index')

def delete(request, todo_id):
    todo = get_object_or_404(Snippet, pk=todo_id)
    todo.delete()

    return redirect('app1:index')
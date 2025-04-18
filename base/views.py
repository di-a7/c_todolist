from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todolist
# Create your views here.
def index(request):
   return render(request,'index.html')

# contact_us
def contact_us(request):
   return HttpResponse("This is contant page")
# about_us

def home(request):
   person = [
      {"name": "Alice", "age": 15},
      {"name": "Bob", "age": 30},
      {"name": "Charlie", "age": 2},
      {"name": "Diana", "age": 28},
      {"name": "Ethan", "age": 50}
   ]
   context = {
      "name":"Home Page",
      "age" : 25,
      "persons": person
   }
   return render(request,'home.html', context)

def list(request):
   obj =  Todolist.objects
   tasks = obj.all()
   all = obj.all().count()
   completed = obj.filter(is_completed = True).count()
   not_completed = obj.filter(is_completed = False).count()
   context = {
      "tasks" : tasks ,
      "all" : all,
      "completed" : completed ,
      "not_completed" : not_completed
   }
   return render(request,'task.html', context)

def create(request):
   if request.method == 'POST':
      title = request.POST.get('title')
      description = request.POST.get('description')
      if title == '' and description == '':
         context =  {
            "error":"Both fields are required."
         }
         return render(request, 'create.html', context)
      
      Todolist.objects.create(title = title, description = description)
      return redirect('/task')
   return render(request,'create.html')

def mark(request, pk):
   task = Todolist.objects.get(pk = pk)
   task.is_completed = True
   task.save()
   return redirect('/task')

def edit(request, pk):
   task = Todolist.objects.get(pk = pk)
   if request.method == 'POST':
      task.title = request.POST.get('title')
      task.description = request.POST.get('description')
      task.save()
      return redirect('/task')
   context = {
      "task" : task
   }
   return render(request,'edit.html', context)

# todo:delete data
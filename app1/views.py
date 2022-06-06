from django.shortcuts import render , HttpResponse , redirect
from .models import Task
# Create your views here.

# For front end

def home(request):
    # for showing objects
    tasks = Task.objects.all()
    # if request.method == 'POST':
    #     delete = request.POST.get('delete')
    #     instance = Task.objects.get('Hello World')
    #     instance.delete()

    return render(request,'app1/home.html',{'tasks': tasks})

def delete(request,id):
    item =Task.objects.get(task_id=id)
    item.delete()
    return redirect('home')

def save(request):
    if request.method == 'POST':
        # id = request.POST.get('id')
        content = request.POST.get('content')
        task = Task(content=content)
        task.save()
        if task.save():
            return redirect('home')
    # tasks = Task.objects.all()
    paramas = {'task': task }

    return render(request,'app1/home.html',paramas)

def finish(request):
    if request.method == "POST":
        status = request.POST.getlist('finish')
        for x in status:
            Task.objects.filter(task_id=int(x)).update(status=True)

    return redirect('home')





    # return render(request,'app1/home.html')


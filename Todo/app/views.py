from django.shortcuts import render,redirect
from .forms import Form
from .models import Todo

def todo(request):
    item=Todo.objects.all()
    context={'item':item}
    return render(request,'index.html',context)

def form(request):
    model=Form()

    if request.method=='POST':
        form=Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    context={'model':model}
    return render(request,'form.html',context)

def edit(request,pk):
    
    item=Todo.objects.get(topic=pk)
    form=Form(instance=item)
    if request.method=="POST":
        update=Form(request.POST,instance=item)
        if update.is_valid():
            update.save()
            return redirect('todo')
    context={'model':form}
    return render(request,'form.html',context)

def delete(request,pk):
    item=Todo.objects.get(id=pk)
    context={'item':item}
    if request.method=="POST":
        item.delete()
        return redirect('todo')
    return render(request,'delete.html',context)
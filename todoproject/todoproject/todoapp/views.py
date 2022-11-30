from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import Todoform
from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbview')

class Taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'up'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbdetails',kwargs={'pk':self.object.id})

class Taskdetailview(DetailView):
    model=Task
    template_name = 'details.html'
    context_object_name = 'de'

class Tasklistview(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'detail'


# Create your views here.
def home(request):
    details = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority = request.POST.get('priority','')
        date=request.POST.get('date','')
        todo = Task(name=name, priority=priority,date=date)
        todo.save()
    return render(request,"home.html", {"detail": details})
def delete(request,taskid):
    if request.method=='POST':
        rem=Task.objects.get(id=taskid)
        rem.delete()
        return redirect('/')
    return render(request,"delete.html")
def update(request,id):
    model=Task.objects.get(id=id)
    form=Todoform(request.POST or None,instance=model)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"update.html",{"form":form})




from django.shortcuts import render, redirect
from .forms import listForm
from list.models import Tugas
from . import models

def index(req):
    form = listForm()
    if req.method == 'POST':
        form = listForm(req.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    data = models.Tugas.objects.all()
    return render(req, 'list/index.html', {'form':form,'data':data})

def detail(req, id):
    data = models.Tugas.objects.filter(pk=id).first()
    return render(req, 'list/detail.html', {
        'data' : data,
    })

def delete(req, id):
    models.Tugas.objects.filter(pk=id).delete()
    return redirect('/')

def edit(req, id):
    if req.POST:
        data = models.Tugas.objects.filter(pk=id).update(Task=req.POST['name'])
        return redirect('/')
    data = models.Tugas.objects.filter(pk=id).first()
    return render(req, 'list/edit.html', {
        'data': data,
    })

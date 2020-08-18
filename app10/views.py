from django.shortcuts import render
from django.http import HttpResponse
from app10 import forms

# Create your views here.

def builtin(request):
    form=forms.SampleForm()
    return render(request,"builtin.html",{'form':form})
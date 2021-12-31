from django.http import HttpResponse
from django.shortcuts import render


def ankush(request):
    return render(request,'index.html')


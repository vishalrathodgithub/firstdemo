from django.shortcuts import render
from demoapp.models import Student
from django.http import JsonResponse
# from rest_framework import Response

# Create your views here.
def Display(request):
    stuData=Student.objects.all()
    return render(request,"demoapp/result.html",{"stuData":stuData})


def json_view(request):
    stuData=Student.objects.all()
    for i in stuData:
        a,b,c,d=i.name,i.rollno,i.address,i.school
    data={"a":a,"b":b,"c":c,"d":d}
    return JsonResponse(data)

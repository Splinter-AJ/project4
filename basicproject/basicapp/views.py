from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import team
# Create your views here.

def demo(request):
    obj=place.objects.all()
    obj1 = team.objects.all()

    return render(request,'index.html',{'result':obj,
                                        'result1':obj1})
# def demo1(request):
#
#     return render(request,'index.html',{})

#def demo(request):
 #   return render(request,'home.html')

#def addition(request):
 #   x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
 #   res=x+y
 #   return render(request,'result.html',{'add':res})

#def about(request):
 #   return render(request,'about.html')
#def contact(request):
#    return HttpResponse("heLLo")

#def demo(request):
 #   name="Ajin"
  #  return render(request,'passing_value.html',{'obj':name})
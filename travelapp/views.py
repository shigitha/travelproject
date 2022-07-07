from django.http import HttpResponse
from django.shortcuts import render
from .  models import place
from . models import member
# Create your views here.
def demo(request):
  mem=member.objects.all()
  obj=place.objects.all()
  return render(request,"index.html",{'result':obj,'members':mem})
#def new(request):
   # return render(request,"new.html")
# return HttpResponse("hello world")

#def calculation(request):
 # x=int(request.GET['num1'])
 # y=int(request.GET['num2'])
  #resadd=x+y
  #resmul=x*y
  #ressub=x-y
  #resdiv=x/y
  #return  render(request,'result.html',{'result':resadd,'result2':ressub,'result3':resmul,'result4':resdiv})

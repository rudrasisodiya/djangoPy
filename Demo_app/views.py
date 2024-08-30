from django.shortcuts import render

def index(request):
    return render(request,'index.html', {'name':'Rudra\'s'})
def add(request):
    val1 = int(request.POST["val1"])
    val2 = int(request.POST["val2"])
    res = val1 + val2
    return render(request,'result.html',{'result':res})
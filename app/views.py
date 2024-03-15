from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='bandaru'
    d={'ban':data}
    return render(request,'data_render.html',context=d)

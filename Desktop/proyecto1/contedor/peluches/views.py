from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'inicio.html')
def semillas(request):
    return render(request,'semillas.html')
def fertilizantes(request):
    return render(request,'fertilizantes.html')


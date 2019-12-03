from django.shortcuts import render

# Create your views here.
def compra_create(request):
    return render(request, 'comp/compras.html')
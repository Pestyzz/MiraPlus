from django.shortcuts import render
from .models import Deuda

def index(request):
    # Fetch all Deuda records
    deudas = Deuda.objects.all()

    # Optional: Filter by estado if query parameter is provided
    estado = request.GET.get('estado')
    if estado:
        deudas = deudas.filter(estado=estado)

    # Pass deudas to template
    return render(request, 'index.html', {'deudas': deudas})
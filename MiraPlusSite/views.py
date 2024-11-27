from django.http import JsonResponse
from .models import Deuda

def get_all_deudas():
    return Deuda.objects.all()

def deuda_filter(request):
    deudas = get_all_deudas()
    estado = request.GET.get('estado')
    if estado:
        deudas = deudas.filter(estado=estado)
    return deudas

def get_deudas_pendientes(request, depto_id):
    deudas = Deuda.objects.filter(num_departamento=depto_id, estado='Deuda pendiente')
    deudas_list = [{'id_deuda': deuda.id_deuda, 'monto': deuda.monto, 'periodo_deuda': deuda.periodo_deuda.strftime('%Y-%m')} for deuda in deudas]
    return JsonResponse({'deudas': deudas_list})
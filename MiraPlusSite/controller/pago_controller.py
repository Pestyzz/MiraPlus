from django.shortcuts import redirect
from django.contrib import messages
from MiraPlusSite.models import Deuda, Pago
import datetime

def pagar_gasto_comun(request):
    if request.method == 'POST':
        department_number = request.POST.get('departmentNumber')
        deuda_id = request.POST.get('deuda')
        
        if department_number and deuda_id:
            deuda = Deuda.objects.get(id_deuda=deuda_id)
            deuda.estado = 'Deuda pagada'
            deuda.save()
            
            fecha_pago = datetime.date.today()
            periodo_pago = deuda.periodo_deuda

            # Determinar el estado del pago
            if fecha_pago <= periodo_pago:
                estado_pago = 'Pago exitoso dentro del plazo'
            else:
                estado_pago = 'Pago exitoso fuera del plazo'

            Pago.objects.create(
                monto=deuda.monto,
                estado=estado_pago,
                fecha_pago=fecha_pago,
                periodo_pago=periodo_pago,
                num_departamento=deuda.num_departamento
            )
            messages.success(request, estado_pago)
            return redirect('index')
    messages.error(request, 'Error en el pago')
    return redirect('index')
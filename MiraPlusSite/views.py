from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Deuda, Departamento, Pago
import datetime

def index(request):
    if request.method == 'POST':
        month_year = request.POST.get('monthYear')
        monto = request.POST.get('mount')

        if month_year and monto:
            month, year = month_year.split('-')
            periodo_deuda = f"{year}-{month}-01"
            monto = float(monto)

            departamentos = Departamento.objects.all()
            for departamento in departamentos:
                Deuda.objects.create(
                    monto=monto,
                    estado='Deuda pendiente',
                    fecha_deuda=periodo_deuda,
                    periodo_deuda=periodo_deuda,
                    num_departamento=departamento
                )
            return redirect('index')

    departamentos = Departamento.objects.all()
    deudas = Deuda.objects.all()
    pagos = Pago.objects.all()

    estado = request.GET.get('estado')
    if estado:
        deudas = deudas.filter(estado=estado)

    return render(request, 'index.html', {'deudas': deudas, 'departamentos': departamentos, 'pagos': pagos})

def get_deudas_pendientes(request, depto_id):
    deudas = Deuda.objects.filter(num_departamento=depto_id, estado='Deuda pendiente')
    deudas_list = [{'id_deuda': deuda.id_deuda, 'monto': deuda.monto, 'periodo_deuda': deuda.periodo_deuda.strftime('%Y-%m')} for deuda in deudas]
    return JsonResponse({'deudas': deudas_list})

def pagar_gasto_comun(request):
    if request.method == 'POST':
        print("Form Data:", request.POST)  # Imprime los datos del formulario en la consola
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
            return redirect('index')
    return redirect('index')
from django.shortcuts import render, redirect
from MiraPlusSite.models import Departamento, Deuda
from MiraPlusSite.views import deuda_filter
from MiraPlusSite.service.pago_service import get_all_pagos

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
    deudas = deuda_filter(request)
    pagos = get_all_pagos()

    return render(request, 'index.html', {'deudas': deudas, 'departamentos': departamentos, 'pagos': pagos})
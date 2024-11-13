document.addEventListener('DOMContentLoaded', function() {
    const departmentNumberSelect = document.getElementById('departmentNumber');
    const deudaSelect = document.getElementById('deuda');
    const montoDeudaSpan = document.getElementById('montoDeuda');
    const cancelTimeInput = document.getElementById('cancelTime');

    function formatCurrency(value) {
        // Asegurarse de que value sea un número
        value = typeof value === 'string' ? parseFloat(value.replace(/[^\d,]/g, '')) : value;
        
        return new Intl.NumberFormat('es-CL', {
            style: 'currency',
            currency: 'CLP',
            minimumFractionDigits: 0,
            maximumFractionDigits: 0
        }).format(value);
    }

    function getMonthName(monthNumber) {
        const monthNames = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ];
        return monthNames[monthNumber - 1];
    }

    function formatPeriod(period) {
        const [year, month] = period.split('-');
        return `${getMonthName(parseInt(month))} ${year}`;
    }

    if (departmentNumberSelect) {
        departmentNumberSelect.addEventListener('change', function() {
            const deptoId = this.value;
            fetch(`/get_deudas_pendientes/${deptoId}/`)
                .then(response => response.json())
                .then(data => {
                    deudaSelect.innerHTML = '<option value="">Seleccione una deuda</option>';
                    data.deudas.forEach(deuda => {
                        const option = document.createElement('option');
                        option.value = deuda.id_deuda;
                        option.textContent = `Deuda ${deuda.id_deuda} - Monto ${formatCurrency(deuda.monto)} - Periodo ${formatPeriod(deuda.periodo_deuda)}`;
                        option.dataset.monto = deuda.monto;
                        deudaSelect.appendChild(option);
                    });
                });
        });
    }

    if (deudaSelect) {
        deudaSelect.addEventListener('change', function() {
            if (this.selectedIndex > 0) {
                const selectedOption = this.options[this.selectedIndex];
                const monto = selectedOption.dataset.monto;
                montoDeudaSpan.textContent = formatCurrency(monto);
                
                const periodo = selectedOption.textContent.match(/Periodo (.+)$/)[1];
                cancelTimeInput.value = periodo;
            } else {
                montoDeudaSpan.textContent = formatCurrency(0);
                cancelTimeInput.value = '';
            }
        });
    }
});
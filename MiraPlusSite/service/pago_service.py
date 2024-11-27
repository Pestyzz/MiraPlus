from MiraPlusSite.models import Pago

def get_all_pagos():
    return Pago.objects.all()
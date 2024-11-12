from django import template

register = template.Library()

@register.filter
def currency(value):
    value = float(value)
    if value.is_integer():
        formatted_value = "${:,.0f}".format(value)
    else:
        formatted_value = "${:,.2f}".format(value)
    return formatted_value.replace(',', '.')
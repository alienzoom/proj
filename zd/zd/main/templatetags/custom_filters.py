# main/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def split(value, separator=','):
    """
    Разделяет строку по разделителю и возвращает список
    """
    if not value:
        return []
    # Убираем лишние пробелы и пустые значения
    return [item.strip() for item in value.split(separator) if item.strip()]

@register.filter
def trim(value):
    """
    Удаляет пробелы в начале и конце строки
    """
    if not value:
        return ''
    return str(value).strip()
from django import template
import re

register = template.Library()

@register.filter
def bold(text):
    pattern = r'\*\*(.*?)\*\*'
    
    # Replace the matched text with <strong> tags
    result = re.sub(pattern, r'<strong>\1</strong>', text)
    
    return result
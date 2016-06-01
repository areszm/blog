from django.core.urlresolvers import reverse
from django import template

register = template.Library()

@register.simple_tag(name='active')
def active(request, pattern):
    import re
    if re.search(pattern, request.path):
        print("patern %s path %s" % (pattern, request.path))
        return 'active'
    return ''


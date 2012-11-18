import re

from django.conf import settings
from django.utils.safestring import mark_safe

CLASS = getattr(settings, 'CURRENT_PAGE_CLASS', 'current_page')
CLASS_RE = re.compile(r"""(\bclass\s*=\s*(['"]))""", re.IGNORECASE)
HREF_RE = re.compile(r"""(<a\W[^>]*\bhref\s*=\s*
                         (["'])(.*?)(?<!\\)(["'])[^>]*>)""",
                         re.IGNORECASE + re.VERBOSE)
HTML_TYPES = ('text/html', 'application/xhtml+xml')


class ViewNameMiddleWare(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        import ipdb; ipdb.set_trace()  # BREAKPOINT
        request.view_name = ".".join((view_func.__module__, view_func.__name__))


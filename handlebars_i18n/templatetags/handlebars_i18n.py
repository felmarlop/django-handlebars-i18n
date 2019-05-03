from django import template
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import get_language

from ..utils import (
    get_offline_catalog_url,
    has_offline_catalog_file)

register = template.Library()

@register.simple_tag
def i18n_catalog(app):
    if getattr(settings, "I18N_OFFLINE_CATALOGS", False):
        lang_code = get_language()
        if has_offline_catalog_file(app, lang_code):
            return """<script src="%s"></script>""" % get_offline_catalog_url(app, lang_code)

        # Try falling back to the default language
        lang_code = settings.LANGUAGE_CODE
        if has_offline_catalog_file(app, lang_code):
            return """<script src="%s"></script>""" % get_offline_catalog_url(app, lang_code)

        raise OfflineCatalogError("I18N_OFFLINE_CATALOGS is set to True, but no offline catalog found for %s" % app)

    else:
        return """<script src="%s"></script>""" % reverse('handlebars_i18n.views.javascript_catalog', kwargs= { "packages": app })


class OfflineCatalogError(Exception):
    pass

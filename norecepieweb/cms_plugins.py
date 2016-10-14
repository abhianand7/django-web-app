"""This file is for creating custom plugins which can be used in different ways
below is greet plugin created, which will greet users when they visit the site
"""

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from norecepieweb.models import Greet


class GreetPlugin(CMSPluginBase):
    model = Greet
    name = _("Greet Plugin")
    render_template = "greet.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(GreetPlugin, self).render(context, instance, placeholder)
        return context
plugin_pool.register_plugin(GreetPlugin)
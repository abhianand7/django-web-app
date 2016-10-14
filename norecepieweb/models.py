from __future__ import unicode_literals

from django.db import models

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
from cms.models.pluginmodel import CMSPlugin


class Greet(CMSPlugin):
    guest_name = models.CharField(max_length=50, default='Guest')


class IconExtension(PageExtension):
    image = models.ImageField(upload_to='icons')


class TitleExtensions(PageExtension):
    title = models.TextField()
# create a model and register it and then import it into cms_wizard.py and forms.py to make a wizard so that
# it can be created directly from the frontend
# class FutureModel():
#     pass

extension_pool.register(IconExtension)
extension_pool.register(TitleExtensions)

from __future__ import unicode_literals

from django.db import models

from cms.extensions import PageExtension
from cms.extensions import TitleExtension
from cms.extensions.extension_pool import extension_pool


class IconExtension(PageExtension):
    image = models.ImageField(upload_to='icons')


class TitleExtensions(TitleExtension):
    title = models.TextField()


extension_pool.register(IconExtension)
extension_pool.register(TitleExtensions)

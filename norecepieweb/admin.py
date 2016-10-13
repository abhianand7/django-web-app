from django.contrib import admin

# Register your models here.
from cms.extensions import PageExtensionAdmin
from cms.extensions import TitleExtensionAdmin

from norecepieweb.models import IconExtension
from norecepieweb.models import TitleExtensions


class IconExtensionAdmin(PageExtensionAdmin):
    pass


class TitleExtensionsAdmin(TitleExtensionAdmin):
    pass

admin.site.register(IconExtension, IconExtensionAdmin)
admin.site.register(TitleExtensions, TitleExtensionsAdmin)
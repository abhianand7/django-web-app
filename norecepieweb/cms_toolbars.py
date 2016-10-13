"""
this is for creating toolbars for editing the extensions
"""


from cms.toolbar_pool import toolbar_pool
from cms.extensions.toolbar import ExtensionToolbar
from django.utils.translation import ugettext_lazy as _
from norecepieweb.models import IconExtension
from norecepieweb.models import TitleExtensions


@toolbar_pool.register
class IconExtensionToolbar(ExtensionToolbar):
    # defines the model for the current toolbar
    model = IconExtension

    def populate(self):
        # setup the extension toolbar with permissions and sanity checks
        current_page_menu = self._setup_extension_toolbar()
        # if it's all ok
        if current_page_menu:
            # retrieves the instance of the current extension (if any) and the toolbar item URL
            page_extension, url = self.get_page_extension_admin()
            if url:
                # adds a toolbar item
                current_page_menu.add_modal_item(_('Page Icon'), url=url,
                    disabled=not self.toolbar.edit_mode)


@toolbar_pool.register
class TitleExtensionToolbar(ExtensionToolbar):
    model = TitleExtensions

    def populate(self):
        # setup the extension toolbar with permissions and sanity checks
        current_page_menu = self._setup_extension_toolbar()
        # if it's all ok
        if current_page_menu and self.toolbar.edit_mode:
            # create a sub menu
            position = 0
            sub_menu = self._get_sub_menu(current_page_menu, 'submenu_label', 'Submenu', position)
            # retrieves the instances of the current title extension (if any) and the toolbar item URL
            urls = self.get_title_extension_admin()
            # cycle through the title list
            for title_extension, url in urls:
                # adds toolbar items
                sub_menu.add_modal_item('icon for title %s' % self._get_page().get_title(),
                                        url=url, disabled=not self.toolbar.edit_mode)
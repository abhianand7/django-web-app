"""
this is for creating toolbars for editing the extensions and page property
"""


from cms.toolbar_pool import toolbar_pool
from cms.extensions.toolbar import ExtensionToolbar
from django.utils.translation import ugettext_lazy as _
from cms.api import get_page_draft
from cms.toolbar_base import CMSToolbar
from cms.utils import get_cms_setting
from cms.utils.page_permissions import user_can_change_page
from django.core.urlresolvers import reverse, NoReverseMatch
from django.utils.translation import ugettext_lazy as _

# never do import by doing .models always import as below
from norecepieweb.models import IconExtension
from norecepieweb.models import TitleExtensions


@toolbar_pool.register
class IconExtensionToolbar(CMSToolbar):
    # defines the model for the current toolbar
    model = IconExtension

    def populate(self):
        # always use draft if we have a page
        self.page = get_page_draft(self.request.current_page)

        if not self.page:
            # Nothing to do
            return

        if user_can_change_page(user=self.request.user, page=self.page):
            try:
                icon_extension = IconExtension.objects.get(extended_object_id=self.page.id)
            except IconExtension.DoesNotExist:
                icon_extension = None
            try:
                if icon_extension:
                    url = reverse('admin:myapp_iconextension_change', args=(icon_extension.pk,))
                else:
                    url = reverse('admin:myapp_iconextension_add') + '?extended_object=%s' % self.page.pk
            except NoReverseMatch:
                # not in urls
                pass
            else:
                not_edit_mode = not self.toolbar.edit_mode
                current_page_menu = self.toolbar.get_or_create_menu('page')
                current_page_menu.add_modal_item(_('Page Icon'), url=url, disabled=not_edit_mode)


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
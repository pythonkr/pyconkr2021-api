from import_export.admin import ImportExportModelAdmin
from django_summernote.widgets import SummernoteWidget


class SummernoteWidgetWithCustomToolbar(SummernoteWidget, ImportExportModelAdmin):
    def template_contexts(self):
        contexts = super(SummernoteWidgetWithCustomToolbar,
                         self).template_contexts()
        contexts['width'] = '960px'
        return contexts

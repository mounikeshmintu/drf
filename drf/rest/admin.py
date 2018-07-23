from django.contrib import admin
from.models import status
from .forms import StatusForm
# Register yofrour models here.
class StatusAdmin(admin.ModelAdmin):
    list_display=['user','__str__','image']
    form=StatusForm
admin.site.register(status,StatusAdmin)

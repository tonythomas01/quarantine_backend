from django.contrib import admin

from crisis.models import Crisis, Request

# Register your models here.
from management.models import Participant


class ParticipantModelAdmin(admin.ModelAdmin):
    pass
    # formfield_overrides = {
    #     models.PointField: {'widget': widgets.TextInput()},
    # }


class CrisisModelAdmin(admin.ModelAdmin):
    pass


class RequestModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(Participant, ParticipantModelAdmin)
admin.site.register(Crisis, CrisisModelAdmin)
admin.site.register(Request, RequestModelAdmin)

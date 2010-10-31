from django.contrib import admin

from agon.models import PointValue, AwardedPointValue


class AwardedPointValueAdmin(admin.ModelAdmin):
    list_display = ["pk", "reason", "target", "points"]
    fields = ["target_user", "value", "timestamp"]
    
    def target(self, obj):
        if obj.target_user_id:
            return obj.target_user
        else:
            return obj.target_object
    
    def reason(self, obj):
        if obj.value_id:
            return obj.value.key
        else:
            if obj.reason:
                return obj.reason
            else:
                return None


admin.site.register(AwardedPointValue, AwardedPointValueAdmin)
admin.site.register(PointValue)

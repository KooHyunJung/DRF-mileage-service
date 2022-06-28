from django.contrib import admin

from mileage.models import Event, Place, PlaceHistory, Point, PointHistory, Review

admin.site.register(Point)
admin.site.register(PointHistory)
admin.site.register(Place)
admin.site.register(PlaceHistory)
admin.site.register(Review)


@admin.register(Event)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ("id", "action", "content", "created_at")
    search_fields = ("id", "action", "content")
    search_help_text = "[id, action, content] 항목으로 검색 가능합니다"

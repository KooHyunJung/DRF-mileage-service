from django.contrib import admin

from mileage.models import Place, PlaceHistory, Point, Review, ReviewPhoto

admin.site.register(Point)
admin.site.register(Place)
admin.site.register(PlaceHistory)


class ReviewPhotoInline(admin.TabularInline):
    model = ReviewPhoto
    verbose_name = "ReviewPhoto"


@admin.register(Review)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ("user_id", "place_id", "updated_at", "created_at")
    search_fields = ("user_id", "place_id", "content")
    search_help_text = "[user_id, place_id, content] 항목으로 검색 가능합니다"
    inlines = [ReviewPhotoInline]

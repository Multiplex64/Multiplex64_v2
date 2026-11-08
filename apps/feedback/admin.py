from django.contrib import admin
from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    # Columns displayed in the list view
    list_display = ("subject", "created_at")

    # Enable search bars for these fields
    search_fields = ("subject", "message")

    # Add a sidebar filter by date
    list_filter = ("created_at",)

    # Make created_at read-only so it doesn't accidentally get changed
    readonly_fields = ("created_at",)

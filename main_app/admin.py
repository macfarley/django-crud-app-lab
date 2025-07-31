from django.contrib import admin
# Add Feeding to the import
from .models import Cat, Feeding

# Register models here.
# Register the Cat model
admin.site.register(Cat)
# Register the new Feeding model
admin.site.register(Feeding)

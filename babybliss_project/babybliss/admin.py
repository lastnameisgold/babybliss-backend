from django.contrib import admin
from .models import User, Baby, Diaper, Feeding, Affirmation
admin.site.register(User)
admin.site.register(Baby)
admin.site.register(Diaper)
admin.site.register(Feeding)
admin.site.register(Affirmation)

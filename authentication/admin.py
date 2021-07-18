from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authentication.models import Author
# Register your models here.
UserAdmin.fieldsets[1][1]['fields'] += ('avatar_image','following',)

admin.site.register(Author, UserAdmin)

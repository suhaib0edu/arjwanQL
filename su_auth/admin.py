from django.contrib import admin
from .models import ExtendUser
from graphql_auth.models import UserStatus
# Register your models here.

admin.site.register(ExtendUser)
admin.site.register(UserStatus)
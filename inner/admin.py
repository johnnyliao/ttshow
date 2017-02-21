#-*- encoding: utf-8 -*-
from django import forms

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin, UserChangeForm as DjangoUserChangeForm
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from inner.models import Inner
from salmonella.admin import SalmonellaMixin

class InnerAdmin(SalmonellaMixin, admin.ModelAdmin):
    list_display = ["image_tag", "title", "inner_type", "date", "count"]
    search_fields = ["title", "user"]
    list_filter  = ["inner_type"]
    salmonella_fields  = ["user"]


admin.site.register(Inner, InnerAdmin)

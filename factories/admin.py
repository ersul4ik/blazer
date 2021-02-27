from django.contrib import admin

from factories.models import DataFixture, DataFixtureColumn


class DataFixtureColumnInline(admin.TabularInline):
    model = DataFixtureColumn
    extra = 3


@admin.register(DataFixture)
class DataFixtureAdmin(admin.ModelAdmin):
    inlines = [DataFixtureColumnInline]

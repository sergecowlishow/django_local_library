from django.contrib import admin

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


class BookInstanceAdmin(admin.ModelAdmin):
    pass
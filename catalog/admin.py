from django.contrib import admin

# Register your models here.

from catalog.models import Author, Genre, Language, Book, BookInstance
# from catalog.decs import AuthorAdmin, BookInstanceAdmin

admin.site.register(Genre)
admin.site.register(Language) 

class BooksInline(admin.TabularInline):
    model = Book
    exclude = ['isbn']
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
	fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
	inlines = [BooksInline]


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
    	(None, {
    		'fields':('book', 'imprint', 'id')	
    	}),
    	('Availability', {
    		'fields':('status', 'due_back', 'borrower' )
    		}),
    )

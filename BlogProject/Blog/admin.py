from django.contrib import admin
from .models import Post


# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # How to show all fields of model in admin page?
    # https://stackoverflow.com/questions/10543032/how-to-show-all-fields-of-model-in-admin-page
    # list_display = list_display = [field.name for field in Post._meta.get_fields()]

    list_display        = ['title','author','publish','status','created','updated']
    list_filter         = ['author','status','publish','created']
    list_editable       = ['status']
    search_fields       = ['title','body','slug']
    prepopulated_fields = {'slug' : ('title',)}
    date_hierarchy      = 'publish'
    ordering            = ['status','publish']

    # the author field is now displayed with a lookup widget,which can be much beĴer than a drop-down select input when you have thousands of users.
    raw_id_fields       = ['author']
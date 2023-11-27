
from django.urls import path
from .views import post_list,post_detail

# useful links:
# 1. Path converters    : https://docs.djangoproject.com/en/4.2/topics/http/urls/#path-converters
# 2. re_path()          : https://docs.djangoproject.com/en/4.2/ref/urls/#django.urls.re_path
# 3. Regular Expression : https://docs.python.org/3/howto/regex.html

app_name = 'Blog'

urlpatterns = [
    path(''               ,post_list   ,name='post_list'),
    # path('<int:post_id>/' ,post_detail ,name='post_detail')
    path('<int:post_year>/<int:post_month>/<int:post_day>/<slug:post_slug>/' ,post_detail ,name='post_detail')
]
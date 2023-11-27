# What is `Django Framework` ?

`Django` is a framework consisting of a set of components that solve common web development problems. Django components are loosely coupled, which means they can be managed independently. This helps separate the responsibilities of the different layers of the framework; the database layer knows nothing about how the data is displayed, the template system knows nothing about web requests, and so on. Django offers maximum code reusability by following the `DRY (don’t repeat yourself)` principle. Django also fosters rapid development and allows you to use less code by taking advantage of Python’s dynamic capabilities, such as introspection.  

```
Django follows the MTV (Model-Template-View) paĴern. It is a slightly similar paĴern to the well-known MVC (Model-ViewController) paĴern, where the Template acts as View and the framework itself acts as the Controller.
```

## Django Architecture

![[Django/source_file/Pasted image 20231016094229.png]]

This is how Django handles HTTP requests and generates responses:  
- A web browser requests a page by its URL and the web server passes the HTTP request to Django.  
- ==Django runs through its configured URL patterns and stops at the first one that matches the requested URL==.  
- Django executes the view that corresponds to the matched URL pattern.  
- The view potentially uses data models to retrieve information from the database.  
- Data models provide the data definition and behaviors. They are used to query the database.  
- The view renders a template (usually HTML) to display the data and returns it with an HTTP response.

## Starting a new project

Django provides a command that allows you to create an initial project file structure:

```shell
django-admin startproject your_project_name
```
for example)
```shell
django-admin startproject mysite
```

- This will create a Django project with the name `your_project_name`.
- ==Avoid naming projects after built-in Python or Django modules in order to avoid conflicts==.

Generated project structure is similar to the following example:

```
mysite/  
	manage.py  
	mysite/  
		__init__.py  
		asgi.py  
		settings.py  
		urls.py  
		wsgi.py
```

Django comes with a system that helps you manage database migrations:
```shell
cd mysite  
python manage.py migrate
```

Start the development server by typing the following command in the shell prompt:
```shell
python manage.py runserver
```

You should see something like this:
```
System check identified no issues (0 silenced).
October 16, 2023 - 11:09:48
Django version 4.2.6, using settings 'BlogProject.settings'
Starting development server at http://127.0.0.1:8000/      
Quit the server with CTRL-BREAK.
```
Now open http://127.0.0.1:8000/ in your browser. You should see a page stating that the project is successfully running as shown in the following Figure:

![[Django/source_file/Pasted image 20231016111133.png]]

*Note* : You can run the Django development server on a custom `host` and `port` or tell Django to load a specific settings file, as follows:
```shell
python manage.py runserver 127.0.0.1:8001 --settings=your_specific_setting_file
```
- For more information , please see this link : [How to properly runserver on different settings for Django?](https://stackoverflow.com/questions/49235486/how-to-properly-runserver-on-different-settings-for-django)

- This server is only intended for development and is not suitable for production use. To deploy Django in a production environment, you should run it as a [[WSGI]] application using a web server, such as :
	- [[Apache]]
	- [[Gunicorn]]
	- [[uWSGI]]
- or as an [[ASGI]] application using a server such as: 
	- [[Daphne]]
	- [[Uvicorn]]
## Django Settings

- ==DEBUG== is a Boolean that turns the debug mode of the project on and off. If it is set to True, Django will display detailed error pages when an uncaught exception is thrown by your application. When you move to a production environment, remember that you have to set it to False. Never deploy a site into production with DEBUG turned on because you will expose sensitive project-related data.
- ==ALLOWED_HOSTS== is not applied while debug mode is on or when the tests are run. Once you move your site to production and set `DEBUG to False`, you will have to add your domain/host to this setting to allow it to serve your Django site.  
- ==INSTALLED_APPS== is a setting you will have to edit for all projects. This setting tells Django which applications are active for this site. By default, Django includes the following applications:
	- `django.contrib.admin`             : An administration site  
	- `django.contrib.auth`               : An authentication framework  
	- `django.contrib.contenttypes` : A framework for handling content types  
	- `django.contrib.sessions`        : A session framework  
	- `django.contrib.messages`        : A messaging framework
	- `django.contrib.staticfiles`   : A framework for managing static files
- ==MIDDLEWARE== is a list that contains middleware to be executed. ROOT_URLCONF indicates the Python module where the root URL patterns of your application are defined.  
- ==DATABASES== is a dictionary that contains the settings for all the databases to be used in the project. There must always be a default database. The default configuration uses an SQLite3 database.  
- ==LANGUAGE_CODE== defines the default language code for this Django site.  
- ==USE_TZ== tells Django to activate/deactivate timezone support. Django comes with support for timezone-aware datetimes. This setting is set to True when you create a new project using the startproject management command.

## What is `Application` in Django ?

```
An application is a group of models, views, templates, and URLs. Applications interact with the framework to provide specific functionalities and may be reused in various projects.
```

- ==You can think of a project as your website, which contains several applications, such as a blog, wiki, or forum, that can also be used by other Django projects.==

![[Django/source_file/Pasted image 20231016171153.png]]

# Creating an application

```
We will build a `blog application` from scratch.
```

- Run the following command in the shell prompt from the project’s root directory:
```shell
python manage.py startapp blog
```

- This command will create the basic structure of the application, which will look like this:
```
Blog/  
	__init__.py  
	admin.py  
	apps.py  
	migrations/  
		__init__.py  
	models.py  
	tests.py  
	views.py
```

These files are as follows:  
- `__init__.py` : An empty file that tells Python to treat the blog directory as a Python module.  
- `admin.py`      : This is where you register models to include them in the Django administration  site — using this site is optional.  
- `apps.py`       : This includes the main configuration of the blog application.  
- `migrations`  : This directory will contain database migrations of the application. Migrations allow Django to track your model changes and synchronize the database accordingly. This directory contains an empty __init__.py file.  
- `models.py`   : This includes the data models of your application; all Django applications need to have a models.py file but it can be left empty.  
- `tests.py`     : This is where you can add tests for your application.  
- `views.py`     : The logic of your application goes here; each view receives an HTTP request, processes it, and returns a response.
## models

- The following diagram shows the `Post` model and the corresponding database table that Django will create when we synchronize the model to the database:

```python
from django.db import models  

class Post(models.Model):  
	title = models.CharField(max_length=250)  
	slug = models.SlugField(max_length=250)  
	body = models.TextField()  
	def __str__(self):  
	return self.title
```

![[Django/source_file/Pasted image 20231023133909.png]]

- By default, Django adds an auto-incrementing primary key field to each model. The field type for this field is specified in each application configuration or globally in the DEFAULT_AUTO_FIELD  setting . When creating an application with the `startapp command` , the default value for DEFAULT_AUTO_FIELD is `BigAutoField` . This is a 64-bit integer that automatically increments according to available IDs. If you don’t specify a primary key for your model, Django adds this field automatically. You can also define one of the model fields to be the primary key by seĴing `primary_key=True` on it.
- 


## Activating the application

- Assume that you have `blog` app in you Django project. We need to activate the blog application in the project, for Django to keep track of the application and be able to create database tables for its models.

```python
INSTALLED_APPS = [  
	# default apps
	'django.contrib.admin',  
	'django.contrib.auth',  
	'django.contrib.contenttypes',  
	'django.contrib.sessions',  
	'django.contrib.messages',  
	'django.contrib.staticfiles',
	# user/custom apps
	'blog.apps.BlogConfig',  
]
```

- *The `BlogConfig` class is the application configuration.*


## Creating and applying migrations

- The `migrate` command applies migrations for all applications listed in `INSTALLED_APPS`. It synchronizes the database with the current models and existing migrations.
- First, we will need to create an initial migration for our Post model : (running the following command in the root directory of your project)

```shell
python manage.py makemigrations your_project_name
```

- Run the following command from the shell prompt to inspect the SQL output of your first migration :

```shell
python manage.py sqlmigrate your_project_name table_num(for example --> 0001)
```

![[Django/source_file/Pasted image 20231023212358.png]]

- Execute the following command in the shell prompt to apply existing migrations :

```shell
python manage.py migrate
```

- ==If you edit the models.py file in order to add, remove, or change the fields of existing models, or if you add new models, you will have to create a new migration using the makemigrations command. Each migration allows Django to keep track of model changes. Then, you will have to apply the migration using the migrate command to keep the database in sync with your models.==

## Creating a superuser

- You will need to create a user to manage the `administration site`. Run the following command:

```ehell
python manage.py createsuperuser
```
## Adding models to the administration site

- Edit the `admin.py` file in your app : 

```python
from django.contrib import admin  
from .models import Post  

admin.site.register(Post)
```

### Customizing how models are displayed

```python
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display        = ['title', 'slug', 'author', 'publish', 'status']
    list_filter         = ['status', 'created', 'publish', 'author']
    search_fields       = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields       = ['author']
    date_hierarchy      = 'publish'
    ordering            = ['status', 'publish']
```

- The `@admin.register()` ==`decorator`== performs the same function as the `admin.site.register()` function that you replaced, registering the `ModelAdmin class` that it decorates.
- ==**`prepopulated_fields`**== doesn’t accept ==`DateTimeField`==, ==**`ForeignKey`**==, ==**`OneToOneField`**==, and ==**`ManyToManyField`**== fields.

### Another way to register your model in Admin site

```python
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "__str__", "publishing_date", "updating_date", "category",  "highlighted"]
    list_filter = ["publishing_date"]
    search_fields = ["title", "short_description", "contents", "keyconcept", "category"]
    prepopulated_fields = {"slug": ("title", "keyconcept", "category",)}

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
```

## ORM

### What is `ORM` ?

- The <mark style="background: #BBFABBA6;">Django object-relational mapper (ORM)</mark> is a powerful database abstraction API that lets you `create`, `retrieve`, `update`, and `delete` objects easily. 
- An ORM allows you to generate SQL queries using the object-oriented paradigm of Python. You can think of it as a way to interact with your database in pythonic fashion instead of writing raw SQL queries. 
- The ORM maps your models to database tables and provides you with a simple pythonic interface to interact with your database. The ORM generates SQL queries and maps the results to model objects. 
- The Django ORM is compatible with <mark style="background: #BBFABBA6;">MySQL</mark>, <mark style="background: #BBFABBA6;">PostgreSQL</mark>, <mark style="background: #BBFABBA6;">SQLite</mark>, <mark style="background: #BBFABBA6;">Oracle</mark>, and <mark style="background: #BBFABBA6;">MariaDB</mark>.

- <mark style="background: #FFB86CA6;">Note</mark> : Django can work with multiple databases at a time, and you can program database routers to create custom data routing schemes.

### Examples

- In the following example , we are retrieving the user object with the username admin :

```python
user = User.objects.get(username='admin')
```

- The <mark style="background: #BBFABBA6;">get()</mark> method allows you to retrieve a single object from the database. Note that this method expects a result that matches the query. If no results are returned by the database, this method will raise a <mark style="background: #FF5582A6;">DoesNotExist</mark> exception, and if the database returns more than one result, it will raise a <mark style="background: #FF5582A6;">MultipleObjectsReturned</mark> exception. Both exceptions are attributes of the model class that the query is being performed on.

- You can create the object and persist it into the database in a single operation using the `create()` method , as follows :

```python
Post.objects.create(title  = 'One more post',  
					slug   = 'one-more-post',  
					body   = 'Post body.',  
					author = user)
```

- <mark style="background: #FFB86CA6;">Note</mark> : The changes you make to a model object are not persisted to the database until you call the `save()` method.

- To retrieve` all objects` from a table, we use the <mark style="background: #BBFABBA6;">all()</mark> method on the default objects manager, like this :

```python
all_posts = Post.objects.all()
```

- To filter a `QuerySet`, you can use the <mark style="background: #BBFABBA6;">filter()</mark> method of the manager. For example, you can retrieve all posts published in the year 2022 using the following `QuerySet` :

```python
Post.objects.filter(publish__year=2022)
```

```python
Post.objects.filter(author__username__contains='moham') 
```

Note : Queries with field lookup methods are built using `two underscores`, for example, <mark style="background: #BBFABBA6;">publish__year</mark> , but the same notation is also used for accessing fields of related models, such as <mark style="background: #BBFABBA6;">author__username</mark>.

- You can exclude certain results from your `QuerySet` using the <mark style="background: #BBFABBA6;"> exclude()</mark> method of the manager. For example, you can retrieve all posts published in 2022 whose titles don’t start with Why :

```python
Post.objects.filter(publish__year=2022).exclude(title__startswith='Why')
```

- You can order results by different fields using the <mark style="background: #BBFABBA6;">order_by()</mark> method of the manager. For example, you can retrieve all objects ordered by their title, as follows:

```python
Post.objects.order_by('title')
```

<mark style="background: #FFB86CA6;">Note</mark> : You can indicate descending order with a negative sign prefix, like this:

```python
Post.objects.order_by('-title')
```

another examples )

```python
post = Post.objects.get(id=1)  
post.delete()
```

- <mark style="background: #FF5582A6;">Note</mark> : <mark style="background: #FFB86CA6;">that deleting objects will also delete any dependent relationships for ForeignKey objects defined with on_delete set to CASCADE.</mark>

### When `QueySets` evaluate ? 

<mark style="background: #BBFABBA6;">QuerySets</mark> are only evaluated in the following cases:  

- The first time you iterate over them  
- When you slice them, for instance, `Post.objects.all()[:3]`  
- When you pickle or cache them  
- When you call `repr() `or `len()` on them  
- When you explicitly call list() on them  
- When you test them in a statement, such as `bool()` , `or` , `and` , or `if`

### Creating model managers

- <mark style="background: #BBFABBA6;">The default manager for every model is the objects manager. This manager retrieves all the objects in the database</mark>.
#### custom managers

- There are `two` ways to add or customize managers for your models:
1. you can add extra manager methods to an existing manager
	- notation : <mark style="background: #BBFABBA6;">Post.objects.my_manager()</mark>
2. create a new manager by modifying the initial `QuerySet` that the manager returns
	- notation : <mark style="background: #BBFABBA6;">Post.objects.my_manager()</mark>








## Views

```python
from django.shortcuts import render,get_object_or_404
from .models import Post

def post_list(request):
    # getting all published post
    all_post = Post.published_manager.all()
    return render(
        request,
        'Blog/post/post_list.xhtml',
        {'posts':all_post}
    )
  
def post_detail(request,post_id):
    post = Post.published_manager.get(id==post_id)
    return render(
        request,
        'Blog/post/post_detail.xhtml',
        {'post':post}
    )
```


## URLS

- The following code is an example of defining URLs in `urls.py` file in your `Blog` app.

```python
from django.urls import path
from .views import post_list,post_detail

# useful links:

# 1. Path converters    : https://docs.djangoproject.com/en/4.2/topics/http/urls/#path-converters
# 2. re_path()          : https://docs.djangoproject.com/en/4.2/ref/urls/#django.urls.re_path
# 3. Regular Expression : https://docs.python.org/3/howto/regex.html

app_name = 'Blog'

urlpatterns = [
    path(''               ,post_list   ,name='post_list'),
    path('<int:post_id>/' ,post_detail ,name='post_detail')
]
```

- In the preceding code, you define an `application namespace` with the  <mark style="background: #BBFABBA6;">app_name</mark>  variable. <mark style="background: #FFF3A3A6;">This allows you to organize URLs by application and use the name when referring to them</mark>.

- <mark style="background: #FFF3A3A6;">Creating a urls.py file for each application is the best way to make your applications reusable by other projects.</mark>

Then you can add app's URLs to main project. see the following code:

```python
"""
URL configuration for BlogProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # importing all `Blog` app urls
    path('Blog/', include('Blog.urls',namespace='Blog'))
]
```

- The new URL patterns defined with include refers to the URL patterns defined in the blog application so that they are included under the `Blog/` path. <mark style="background: #FFF3A3A6;">You include these patterns under the  namespace blog. Namespaces have to be unique across your entire project</mark>.
- <mark style="background: #FFF3A3A6;">you will refer to your blog URLs easily by using the namespace followed by a colon and the URL name</mark>, for example, `Blog:post_list` and `Blog:post_detail`.

## Django request/response in one view

![[Pasted image 20231124213633.png|900]]

Let’s review the Django request/response process: 
1. A web browser requests a page by its URL, for example,`https://domain.com/blog/33/`. The web server receives the HTTP request and passes it over to Django. 
2. <mark style="background: #BBFABBA6;">Django runs through each URL patterns defined in the URL patterns configuration. The framework checks each patterns against the given URL path, in order of appearance, and stops at the first one that matches the requested URL</mark>. In this case, the patterns `/blog/<id>/` matches the path` /blog/33/`. 
3.  Django imports the view of the matching URL patterns and executes it, passing an instance of the `HttpRequest` class and the keyword or positional arguments. The view uses the models to retrieve information from the database. Using the Django ORM `QuerySets` are translated into SQL and executed in the database. 
4. The view uses the render() function to render an HTML template passing the Post object as a context variable. 
5. The rendered content is returned as a `HttpResponse` object by the view with the text/html content type by default.

- Note: You can using all URLs globally. How can you ? see the following example)

```python
Blog_app:post_detail
```

- <mark style="background: #FFF3A3A6;">We have used the blog  namespace `Blog_app` that defined in the main URL (main project URL file) followed by a colon and the URL name `post_detail`.</mark>

- If you adding `get_absolute_url` to your model , you can use it with the following format:

```html
<a href="{% url 'Blog_app:post_detail' post.id %}">
<a href="{{ post.get_absolute_url }}">
```
- `Blog_app`      : namespace (that defined in main the project's URLs)
- `post_detail` : URL that defined in Blog app


# Other Tips

- Basic Pagination Template : 
```html
<div class="pagination">
    <span class="step-links">
        {% if page_obj.has_previous %}
            <a href="?page=1">&laquo; first</a>
            <a href="?page={{ page_obj.previous_page_number }}">previous</a>
        {% endif %}
        <span class="current">
            Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
        </span>
        {% if page_obj.has_next %}
            <a href="?page={{ page_obj.next_page_number }}">next</a>
            <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>
        {% endif %}
    </span>
</div>
```

- Using the above template in another template:
```html
{% extends 'Blog/base.xhtml' %}

{% block title %}
    <h1>
        Blog List
    </h1>
{% endblock %}

{% block body%}
    <h1> - List of all published post</h1>
    {% for post in posts %}
        <ul>
            <h2>
                <a href="{{ post.get_absolute_url }}">
                    {{ post.title }}
                </a>
            </h2>
            <p class="date">
                Published {{ post.publish }} by {{ post.author }}
            </p>
            {{ post.body|truncatewords:30|linebreaks }}
        </ul>
    {% endfor %}
    {% include 'pagination.xhtml' with page_obj=posts %}
{% endblock %}
```

- <mark style="background: #FFF3A3A6;">{% include 'pagination.xhtml' with page_obj=posts %}</mark> : The `{% include %}` template tag loads the given template and renders it using the current template context. We use with to pass additional context variables to the template. The pagination template uses the `page_obj` variable to render, while the Page object that we pass from our view to the template is called `posts`.

# Some issues
- [You may need to add u'127.0.0.1' to ALLOWED_HOSTS](https://stackoverflow.com/questions/57545934/you-may-need-to-add-u127-0-0-1-to-allowed-hosts)

# Resources

- [Django 4 By Example](Django/source_file/Django_4_By_Example_Fourth_Edition_page61.pdf)
- [How to show all fields of model in admin page?](https://stackoverflow.com/questions/10543032/how-to-show-all-fields-of-model-in-admin-page)
- [More of one prepopulated_fields for django admin](https://stackoverflow.com/questions/52247181/more-of-one-prepopulated-fields-for-django-admin)
- [Django Models - Official Website](https://docs.djangoproject.com/en/4.2/ref/models/)
- [Path converters](https://docs.djangoproject.com/en/4.2/topics/http/urls/#path-converters)
- [re_path](https://docs.djangoproject.com/en/4.2/ref/urls/#django.urls.re_path)
- [The Django template language](https://docs.djangoproject.com/en/4.1/ref/templates/language/)
- [What is reverse()?](https://stackoverflow.com/questions/11241668/what-is-reverse)
- [Pagination](https://docs.djangoproject.com/en/4.2/topics/pagination/)
- 
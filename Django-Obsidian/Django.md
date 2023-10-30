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

# Some issues
- [You may need to add u'127.0.0.1' to ALLOWED_HOSTS](https://stackoverflow.com/questions/57545934/you-may-need-to-add-u127-0-0-1-to-allowed-hosts)


# Resources

- [Django 4 By Example](Django/source_file/Django_4_By_Example_Fourth_Edition_page61.pdf)
- [How to show all fields of model in admin page?](https://stackoverflow.com/questions/10543032/how-to-show-all-fields-of-model-in-admin-page)
- [More of one prepopulated_fields for django admin](https://stackoverflow.com/questions/52247181/more-of-one-prepopulated-fields-for-django-admin)
- 
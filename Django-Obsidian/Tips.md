# How can I setup a `virtualenv` ?

```shell
python -m venv your_folder_name
```
or 
```shell
python -m virtualenv your_folder_name
```

- With `deactivate` command you can deactivate your running environment.

# How can I install a `package` with `pip` command ?

```shell
pip install package_name
```

for example)
```shell
pip install Django~=4.1.0
```

- This will install Django’s latest 4.1 version in the Python `site-packages/` directory of your virtual environment.
## How can I checking package version ?

```shell
python -m package_name --version
```

# How can I install all requirements package in one project from `requirements.txt` file ?

```shell
pip install -r requirements.txt
```

# What is `middleware` ?

## Overview

Middleware is software and cloud services that provide common services and capabilities to applications and help developers and operators build and deploy applications more efficiently. Middleware acts like the connective tissue between applications, data, and users.

Middleware has been part of software engineering terminology since the [late 1960s](http://homepages.cs.ncl.ac.uk/brian.randell/NATO/nato1968.PDF), and as a category can apply to a wide range of modern software components. Middleware can include [application runtimes](https://www.redhat.com/en/technologies/cloud-computing/openshift/application-runtimes), enterprise application [integration](https://www.redhat.com/en/topics/integration/what-is-integration) and various kinds of cloud services. Data management, [application services](https://www.redhat.com/en/products/application-foundations), messaging, authentication, and [application programming interface (API) management](https://www.redhat.com/en/topics/api/what-is-api-management) are all commonly handled by middleware.  
  
Today middleware is the technological foundation for modern cloud-native architectures. For organizations with multi-cloud and containerized environments, middleware can make it cost-effective to develop and run applications at scale.

For more information see this link : [What is middleware](https://www.redhat.com/en/topics/middleware/what-is-middleware)



# Other Resources 

- [Python Enum](https://docs.python.org/3/library/enum.html)
- [Django Enum](https://docs.djangoproject.com/en/4.2/ref/models/fields/#enumeration-types)
- [Can I move a virtualenv?](https://stackoverflow.com/questions/32407365/can-i-move-a-virtualenv)
- 
=========================
Django Default ImageField
=========================

Default static file path for Django ImageField


Setup
=====

* install it via ``pip install django-default-imagefield``
* add it to your settings and it auto-registers itself
  ::

      settings.INSTALLED_APPS = [
         ...
         'django_fields',
         ...
      ]

Usage
=====

* add field to your model class
  ::

      from django_fields import DefaultStaticImageField

      class Post(models.Model):
        photo = DefaultStaticImageField(blank=True)

* default path is ``django_fields/no_image.png`` and is included in the package. you can change it via ``settings.py``
  ::

      # settings.py
      DEFAULT_IMAGE_PATH = 'images/custom_no_image.png'

* or add field attribute ``default_image_path``
  ::

      class Post(models.Model):
        photo = DefaultStaticImageField(blank=True, default_image_path='images/blank.png')

* if there is no file in the ``default_image_path`` of the field or ``DEFAULT_IMAGE_PATH`` in settings.py, use the default image built into the package.

* if deploying to a production environment, you must run the ``./manage.py collectstatic`` command to copy the image files included in the package to the static file serving path.

Contributing
============

As an open source project, we welcome contributions.

The code lives on `github <https://github.com/LeeHanYeong/Django-Default-ImageField>`_.

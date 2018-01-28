from django.conf import settings
from django.contrib.staticfiles import finders
from django.db.models.fields.files import ImageFieldFile, ImageField

__all__ = (
    'DefaultStaticImageField',
    'DefaultStaticImageFieldFile',
)

DEFAULT_IMAGE_PATH = 'django_fields/no_image.png'


class DefaultStaticImageFieldFile(ImageFieldFile):
    @property
    def url(self):
        try:
            return super().url
        except ValueError:
            from django.contrib.staticfiles.storage import staticfiles_storage
            if finders.find(self.field.static_image_path):
                return staticfiles_storage.url(self.field.static_image_path)
            return staticfiles_storage.url(DEFAULT_IMAGE_PATH)


class DefaultStaticImageField(ImageField):
    attr_class = DefaultStaticImageFieldFile

    def __init__(self, *args, **kwargs):
        self.static_image_path = kwargs.pop(
            'default_image_path',
            getattr(settings, 'DEFAULT_IMAGE_PATH', DEFAULT_IMAGE_PATH))
        super().__init__(*args, **kwargs)

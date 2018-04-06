from django.conf import settings
from django.db.models.fields.files import ImageFieldFile, ImageField
from django.utils.module_loading import import_string

__all__ = (
    'DefaultStaticImageField',
    'DefaultStaticImageFieldFile',
)

DEFAULT_IMAGE_PATH = 'django_fields/no_image.png'


class DefaultStaticImageFieldFile(ImageFieldFile):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.field.default_image_path and (
                not self.name or self.name == self.field.default_image_path):
            self.name = self.field.static_image_path
            self.storage = import_string(settings.STATICFILES_STORAGE)()
            # disable delete and save methods
            del self.delete
            del self.save


class DefaultStaticImageField(ImageField):
    attr_class = DefaultStaticImageFieldFile

    def __init__(self, *args, **kwargs):
        self.static_image_path = kwargs.pop('default_image_path', DEFAULT_IMAGE_PATH)
        super().__init__(*args, **kwargs)

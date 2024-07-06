from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class ExtensionValidator(RegexValidator):
    def __init__(self, extensions, message=None):
        if not hasattr(extensions, '__iter__'):
            extensions = [extensions]
        regex = '\.(%s)$' % '|'.join(extensions)
        if message is None:
            message = _('Тип файла не поддерживается. Принятые типы:: %s.' % ', '.join(extensions))
        super(ExtensionValidator, self).__init__(regex, message)

    def __call__(self, value):
        super(ExtensionValidator, self).__call__(value.name)
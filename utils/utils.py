import datetime
import functools
import secrets, string
from django.conf import settings


def build_absolute_uri(url):
    if not settings.BACKEND_HOST.endswith('/'):
        base_url = settings.BACKEND_HOST + '/'
    else:
        base_url = settings.BACKEND_HOST

    relative_url = url.lstrip('/')

    absolute_url = base_url + relative_url

    return absolute_url


def rgetattr(obj, attr, *args):
    def _getattr(obj, attr):
        return getattr(obj, attr, *args)

    return functools.reduce(_getattr, [obj] + attr.split('.'))


def make_bool(val):
    if str(val) == 'false' or str(val) == '0' or str(val) == 'False':
        return False
    else:
        return True


def make_next_date(day):
    now = datetime.datetime.now()
    return now + datetime.timedelta(days=day)


def get_object_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist as e:
        return None


def make_password():
    letters = string.ascii_letters
    digits = string.digits
    alphabet = letters + digits
    pwd_length = 9
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))
    return pwd

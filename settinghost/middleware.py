from django.conf import settings
from django.contrib.sites.models import Site

class SettingHost(object):

    def process_request(self, request):
        host = request.get_host()
        try:
            site = Site.objects.get(domain=host)
        except Site.DoesNotExist:
            site = Site(domain=host, name=host)
            site.save()
        settings.SITE_ID = site.id
import os
import geoip2.database

from geoip2.errors import AddressNotFoundError

from cotidia.geoip.utils import get_client_ip


CURRENT_DIR = os.path.dirname(__file__)


def geoip_data(request):

    reader = geoip2.database.Reader(os.path.join(CURRENT_DIR, 'data/GeoLite2-Country.mmdb'))

    try:
        response = reader.country(get_client_ip(request))
        country_iso_code = response.country.iso_code
    except AddressNotFoundError:
        country_iso_code = None

    return {
        "GEOIP_COUNTRY_ISO_CODE": country_iso_code,
    }

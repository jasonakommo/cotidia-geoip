# Geolocate IP

This module locate an IP using the Maxmind database: [https://dev.maxmind.com/geoip/geoip2/geolite2/](https://dev.maxmind.com/geoip/geoip2/geolite2/).

Download **GeoLite2 Country**: [here](http://geolite.maxmind.com/download/geoip/database/GeoLite2-Country.tar.gz)

## Usage

Include the context processor to add the country ISO code to your template context.

```python
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'cotidia.geoip.context_processor.geoip_data',
            ],
        },
    },
]
```

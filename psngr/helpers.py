""" """
import logging
import pandas as pd
from django.conf import settings

from urllib.parse import urlparse


logs = logging.getLogger(__name__)

VALID_IMAGE_EXTENSIONS = [
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
]


def cache_csv_data(DB_URL, URL_OUTPUT_TYPE, skiprows=[], nrows=None):
    """ """
    try:
        return pd.DataFrame(
            pd.read_csv(
                DB_URL + URL_OUTPUT_TYPE,
                sep=",", header=0, index_col=False,
                skiprows=skiprows, nrows=nrows))
    except Exception as e:
        logs.exception(e)
        return pd.DataFrame({'no_data': []})


def validate_image(url):
    """ """
    url_parse = urlparse(url)
    path = url_parse.path
    if not path:
        return settings.DEFAULT_IMAGE_URL
    if any([path.endswith(e) for e in VALID_IMAGE_EXTENSIONS]):
        return url
    else:
        return settings.DEFAULT_IMAGE_URL

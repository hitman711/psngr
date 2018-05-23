""" """
import logging
import pandas as pd

logs = logging.getLogger(__name__)


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

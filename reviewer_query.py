from constants import *
from business import Business
from yelp_requester import YelpRequester
import reviewer_utils as r_utils

import requests


def find_buz_at(location: str, limit: int=None) -> set[Business]:
    """
    Returns a list of businesses at the location.
    If limit is defined (not None), then only a slice of the
    entire result set up to limit is returned.
    """
    url = G_BASE_YELP_URL + G_BUSINESS_SEARCH + "?location={}".format(location)
    requester = YelpRequester("app-config.yml")
    res = requester.get(url)

    if limit:
        buz_set = r_utils.to_business_set(res.json()["businesses"][:limit])
    else:
        buz_set = r_utils.to_business_set(res.json()["businesses"])

    return buz_set
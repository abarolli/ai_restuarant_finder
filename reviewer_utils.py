from ruamel.yaml import YAML
from ruamel.yaml.compat import ordereddict

from business import Business


def get_configs(_file: str) -> ordereddict:
    """
    Returns configurations necessary for Yelp API in an ordereddict.
    """
    yml = YAML()
    with open(_file) as f:
        configs = yml.load(f)

    return configs


def to_business_set(businesses: list) -> set[Business]:
    """
    Consumes a list of businesses (dictionaries containing the necessary
    restuarant information) and returns a set of Businesses
    """
    businesses_set = set()
    for business_info in businesses:
        businesses_set.add(Business(**business_info))
    
    return businesses_set
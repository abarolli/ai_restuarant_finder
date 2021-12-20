import requests
import reviewer_utils as r_utils


class YelpRequester:
    def __init__(self, config_file):
        self.config_file = config_file
        self.__configs = r_utils.get_configs(config_file)


    def get(self, url):
        headers = {
            "Authorization": "Bearer {}".format(self.__configs["APIKey"])
        }

        return requests.get(url, headers=headers)
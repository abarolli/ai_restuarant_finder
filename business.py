import requests


class Business:
    def __init__(self, **props):
        self.name = props["name"]
        self.phone = props["phone"]
        self.location = props["location"]
        self.__image_url = props["image_url"]
        
        
    @property
    def image(self) -> bytes:
        
        """
        Returns the raw byte content of the
        image of the business per Yelps website.
        Can be written to a file to save the image.
        """

        image_url = self.__image_url
        raw_content = requests.get(image_url).content
        return raw_content


    def __str__(self):
        return "Business name='{}'".format(self.name)
import requests
from selectorlib import Extractor # scrape tool

class Temperature:
    """
    Represent a temperature value extracted from the timeanddate.com/weather webpage.
    """

    def __init__(self, city:str, country:str):
                # the scrapping site needs space in - ,and lower case
        self.city = city.replace(" ", "-").lower()
        self.country = country.replace(" ", '-').lower()

    def _build_url(self):                                   # country  # city
        return f'https://www.timeanddate.com/weather/{self.country}/{self.city}'

    @property # func becomes attribute
    def scrape(self):
        url = self._build_url()
        yaml_path = 'temperature.yaml'

        res = requests.get(url=url).text

        extractor = Extractor.from_yaml_file(yaml_filename= yaml_path)
        raw_data = extractor.extract(html=res) # dict
        return raw_data

    def get_temperature(self):
        # Cleaning the scraped data
        result = float(self.scrape['temperature'].replace('\xa0°C', ''))
        return result


if __name__ == "__main__": # meaning if the script is executed directly otherwise don't
    temp = Temperature(city= 'karur', country= 'India')
    print(temp.get_temperature())

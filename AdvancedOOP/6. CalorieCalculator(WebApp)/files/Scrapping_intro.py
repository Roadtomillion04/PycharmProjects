import requests
from selectorlib import Extractor # scrape tool
            # static                       # country  # city
url = 'https://www.timeanddate.com/weather/usa/new-york'
res = requests.get(url= url).text # .text returns HTML code in str
print(type(res))

# no need to instance Extractor() because from_yaml_file class method does for it
extractor = Extractor.from_yaml_file(yaml_filename= 'temperature.yaml')
print(extractor)

print(extractor.extract(html= res)) # this returns a dictionary

# Let's filter data
raw_data = extractor.extract(html= res)

result = float(raw_data['temperature'].replace('\xa0°C', ''))
print(result)


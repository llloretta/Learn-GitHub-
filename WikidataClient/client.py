import wikidata
from wikidata.client import Client
client = Client()
entity = client.get('Q20145', load=True)
print(entity)
print(entity.description)

image_prop = client.get('P18')
image = entity[image_prop]
print(image)
print(image.image_resolution)
print(image.image_url)
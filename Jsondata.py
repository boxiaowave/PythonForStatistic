import json
import urllib2
# from swampy.Lumpy import Lumpy

# lumpy=Lumpy()
# lumpy.make_reference()

def get_country(ip):
    response = urllib2.urlopen('http://freegeoip.net/json/'+ip).read().decode('utf-8')
    print response
    responseJson = json.loads(response)
    return responseJson.get('country_code')

print get_country('210.45.121.4')

#lumpy.object_diagram()

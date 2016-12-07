import requests

# def get_location():
#     url = 'http://192.168.1.129:8063/gift/v1/location/' 
#     location = r.json()
#     location_list = {'location':location['results']}
#     return requests.get(url).json()

def get_location():
    print("in get location")
    url = 'http://192.168.1.129:8063/gift/v1/location/' 
    #params = {'year': year, 'author': author}
    r = requests.get('http://192.168.1.129:8063/gift/v1/location/')
    location = r.json()
    #location_list = {'location':location}
    print("service location", location)
    #print("service location", location_list)
    return requests.get(url).json()
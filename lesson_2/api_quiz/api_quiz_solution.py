import json
import requests

import json
import requests

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
    # local workspace requires last.fm api key
    x = open(url, 'r')
    result = json.loads(x.read())
    return result['topartists']['artist'][0]['name'] # return the top artist in Spain


if __name__ == '__main__':
	# url should be the url to the last.fm api call which
	# will return find the top artists in Spain

    url = 'lastfm.json'# fill this in 
    print api_get_request(url) 


import sys
import requests
from datetime import datetime

from formatting import format_msg

def send (name, website = None, verbose = False):
    if website != None:
        msg = format_msg (my_name = name, my_website = website)
    else:
        msg = format_msg (my_name = name)
    if verbose:
        print (name, website)
    #msg = format_msg(my_name=name, my_website=website)
    #send the message
    r =requests.get('https://httpbin.org/json')
    if r.status_code == 200:
        return r.json()
    else:
        return 'There was an error'

    #return msg

if __name__ == '__main__':
    print (sys.argv)
    name = 'Unknown'
    if len (sys.argv) > 1:
        name = sys.argv [1]
    response = send ('Ruby', verbose = True)
    print (response)
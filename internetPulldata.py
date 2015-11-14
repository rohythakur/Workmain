import requests
import argparse, os, time
import urlparse, random
from bs4 import BeautifulSoup


requests.packages.urllib3.disable_warnings()



url = 'https://confluence.ndg.intel.com/login.action?os_destination=%2Fdashboard.action'
values = {'os_username': 'eeamesX',
          'os_password': 'Corporate$123'}
try:
    r = requests.post(url, data=values, verify=False)
    # Now you have logged in

    params = {'Category': 6, 'deltreeid': 6, 'do': 'Delete Tree'}
    url = 'https://confluence.ndg.intel.com/login.action?os_destination=%2Fdashboard.action'

    # sending cookies as well
    result = requests.get(url, data=params, cookies=r.cookies, verify=False)
    print "successfully logged onto " + url
    #print result.text
    #print r.headers
    print result.url

    #print result.content
except Exception as e:
    print str(e)



page = 'https://confluence.ndg.intel.com/pages/viewpage.action?pageId=146574736'
getconfluence = requests.get (page, data=values, verify=False)
print getconfluence.url
print getconfluence.content







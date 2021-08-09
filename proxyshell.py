# Proxyshell scanner
# - Nicolas 9/8/2021

import urllib3
import requests,sys
requests.packages.urllib3.disable_warnings()

def proxyshell(url):
    url = url.strip()
    url = url + "/autodiscover/autodiscover.json?@abc.com/owa/?&Email=autodiscover/autodiscover.json%3F@abc.com"
    try:
        r = requests.get(url, timeout=10,verify=False)
        print ("Connecting to:", url)
        if (r.status_code == 302):
            print ("Vulnerable")
        else:
            print ("Not Vulnerable")
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


if __name__ == '__main__':
    try:
        proxylogon(sys.argv[1])
    except:
        print ("python3 proxyshell.py url" )

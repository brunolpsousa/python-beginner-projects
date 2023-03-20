# import urllib
# use urllib.request to get the data from the url
# write a function that takes a url
# returns a response

from urllib.request import urlopen
import urllib.error as err


def checker(url):
    if "http" not in url:
        url = "https://" + url
    try:
        response = urlopen(url, timeout=10)
        print("Site is up and running. Code:", response.getcode())
    except err.HTTPError as e:
        print(e)
    except err.URLError as e:
        print(e)
    except Exception as e:
        print("Exception:", e)


url = input("Enter a URL: ")

checker(url)

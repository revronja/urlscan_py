

import requests

class Scanner:
    def __init__(self):
       self.API_KEY = "key"
       self.BASE_URL = "https://urlscan.io/api/v1/"
       self.Headers =  {
            'Content-Type': 'application/json',
            'API-Key': self.API_KEY,
        }

    def scan_url(self, url):
        """
        a function that will submit a URL to the scan endpoint

        a sample response
            {"url": "https://www.google.com", "public": "on"}
            {
            "message": "Submission successful",
            "uuid": "afee5355-ac59-48a0-8993-eb8db40f5ca4",
            "result": "https://urlscan.io/result/afee5355-ac59-48a0-8993-eb8db40f5ca4/",
            "api": "https://urlscan.io/api/v1/result/afee5355-ac59-48a0-8993-eb8db40f5ca4/",
            "visibility": "public",
            "options": {
                "useragent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
            },
            "url": "https://www.google.com"
            }
        """
        data = '{"url": "%s", "public": "on"}' % url
        print(data)
        response = requests.post(self.BASE_URL+'scan/', headers=self.Headers, data=data)
        r = response.content.decode("utf-8")
        print(r)
    


scanner = Scanner()
try:
    scanner.scan_url("https://www.google.com")
except:
    pass

# TO DO 
# check last scans for updates

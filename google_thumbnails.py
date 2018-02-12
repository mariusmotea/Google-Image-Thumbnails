import requests
import sys
import json
import base64

query = sys.argv[1]
query = query.split()
query = '+'.join(query)
url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}

response = requests.get(url, headers=header)

response_pices = response.text.split("data:image/")
response_pices = response_pices[8:] # remove footer images

index = 0

for image in response_pices:
    pices = image.split(";base64,")
    extension = pices[0]
    img_data = pices[1].split("\"]")[0]
    index +=1
    with open("image" + str(index) + "." + extension, "wb") as fh:
        fh.write(base64.standard_b64decode(img_data))

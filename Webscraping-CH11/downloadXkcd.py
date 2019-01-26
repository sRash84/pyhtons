#! python3
# downloadXkcd.py - Downloads every single XKCD Comic

import requests, os, bs4

url = "https://xkcd.com/"

os.makedirs('xkcd', exist_ok= True)
while not url.endswith("#"):
    #TODO: Download the page
    print("Downloading page %s...." % url )
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    #TODO: Find the url of the comic page
    comicElem = soup.select("#comic img")

    if comicElem  == []:
        print("Could not find image")
    else:
        try:
            comicUrl = comicElem[0].get('src')
            #Download the image
            print("Downloading image %s .... " % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            #skip this comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com'+prevLink.get('href')
            continue
        #Save the image to ./XKCD
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    #Get the prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com'+prevLink.get('href')
print("Done")

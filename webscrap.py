import requests
from bs4 import BeautifulSoup as soup

for i in range(1,51):
    my_url = "https://www.justdial.com/Mumbai/Candid-Wedding-Photographers/nct-10956046/page-"+str(i)
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    page_html = requests.get(my_url, headers=agent)
    page_soup = soup(page_html.text, "html.parser")
    container = page_soup.findAll("div", {'class': 'card_imgwrap'})
    #print(page_soup.h1)
    #contain = container[0]
    #contain.div.a["href"]
    for contain in container:
        dynamic_url = contain.div.a['href']
        print("url :" + dynamic_url)
        dynamic_html = requests.get(dynamic_url, headers=agent)
        dynamic_soup = soup(dynamic_html.text, "html.parser")
        pageWall = dynamic_soup.findAll('div', {'class':"company-details"})
        detailsData = pageWall[0]
        spanArray = detailsData.div.div.span.find_all("span", class_= "fn")
        name = spanArray[0].text.strip()
        print("name :" + name)
        websiteSpan = dynamic_soup.find_all('span', class_="mreinfp")

        website = websiteSpan[0].a['href']
        print("website :" + website)
        #email, website, mobile, name


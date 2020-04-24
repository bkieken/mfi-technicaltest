from bs4 import BeautifulSoup
import requests

# Recursive retrieval of all links from a website
def getLinksFromURL(mainUrl, url, listLink):
    try :
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')        
    except :            
        print('##### ERROR retrieving url : ' + url)
        if (url not in listLink):
            listLink.append(url)
        return listLink
            
    for link in soup.find_all('a', href=True):  # Get all links          
        if (mainUrl in link['href']): # Get only absolute html links
            if (link['href'] not in listLink):
                print("URL found : " + link['href'])
                listLink.append(link['href'])
                listLink = getLinksFromURL(mainUrl, link['href'], listLink)
       
    return listLink

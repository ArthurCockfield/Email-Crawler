# Resources used:
# Google search parameters https://moz.com/blog/the-ultimate-guide-to-the-google-search-parameters
# web scraping https://automatetheboringstuff.com/chapter11/

import requests, bs4, time
import re # for finding the URL using the package I pulled
import numpy as np

search_string = "kingston restaurants"


def open_google(page=0) :
    URL = 'http://www.google.com/search?q='+search_string+"&start="+str(page*10)
    res = requests.get(URL)
    return res

def Collect_Links(URL=None) : 
    """Collects URLS from chosen web page based on passed URL
    ARGS: URL that person wants to input(in case someone wants to put input outside function)
    Returns: list of websites """

 
    res = requests.get(URL)
    # html = bs4.BeautifulSoup(res)

    #print(text)

    soup = bs4.BeautifulSoup(res.text,"lxml")
    # Turn this into set to remove duplicates
##    only_links = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', str(soup))
##    print(len(only_links))
    # Re is being commented out temporarily. The reason for doing so is to test out beautiful soup's parser
    only_links = []
    souptest = soup.find_all('a')
    for i in souptest :
        only_links.append(i['href'])
    print(len(only_links))

                
            
    return only_links

def collect_google(URL=None, google_search = False) : 
    """Collects URLS from Google based on a search input
    ARGS: Search term (in case someone wants to put input outside function)
    Returns: list of websites """
    all_links = ""
#    only_links = []
    for i in range(50) :
        time.sleep(10)
        if i > 0 :
            
            # Open Google Web page
            res = open_google(page=i)
        
            
          
            soup = bs4.BeautifulSoup(res.text,"lxml")
            # All Links collects all information stored in this class. Could be useful later when I am trying to collect more than just the URL
            one_page = soup.find_all('h3', class_="r")
            all_links = all_links + str(one_page)

    only_links = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', all_links)
            

    return only_links


# error handling
def collect_email(URL) :
    res = requests.get(URL)
    text = bs4.BeautifulSoup(res.text,"lxml")
    text = str(text)
    text = text.split(" ")
    all_emails = []
    for i in range(len(text)-1) :
        if '@' in text[i] and "." in text[i] and len(text[i]) <20 :
            strip = text[i]

            all_emails.append(strip)
    if all_emails != [] : 
        return all_emails
    else:
        "Nothing found at this link"
def data_clean(email_list) :
    """ Cleans all emails"
    arg: email data
    return: email data without common errors like quotations
    removes emails that are images"""
    pass
           


Google_Links = collect_google()
print(Google_Links)
print(len(Google_Links))
email_collection = []
for i in Google_Links :
    #Add email collection on home page logic
   try:
    # Try to collect email on home page
        home_email = collect_email(i)
        if home_email != None :
            email_collection.append(home_email)
            continue
        website_links = Collect_Links(URL=i)
        print("The websites being collected for ",i," is", website_links)
            # website_links pulls all the URLS it finds from its home page.
        for j in website_links :
            try: 
                time.sleep(2)
                print("The Link being checked is: ", j)
                temp_email = collect_email(j)
                print(temp_email)
                if temp_email != None :
                    email_collection.append(temp_email)
            except Exception as e :
                print("Error in collecting emails. Here is the error: ", e)
   except Exception as e :
        print("Error with collecting collect the 2nd level of links", e)
print(email_collection)
try : 
    np.savetxt("file_name.csv", email_collection, delimiter=",", fmt='%s', header=header)
except Exception as e :
    print(e)
# collect all URLS associated with webpage
# Try to pull email from webpage
# pull title of webpage
# Pull all links from this webpage
# then repeat process of trying to pull email
# Navigate to next page by adding &start=10 to end of url



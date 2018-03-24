# Resources used:
# Google search parameters https://moz.com/blog/the-ultimate-guide-to-the-google-search-parameters
# web scraping https://automatetheboringstuff.com/chapter11/

import requests, bs4, time

search_string = "kingston restaurants"


def open_google(page=0) :
    URL = 'http://www.google.com/search?q='+search_string+"&start="+str(page*10)
    res = requests.get(URL)
    return res

def collect_URLS(URL=None, google_search = False) : 
    """Collects URLS from Google based on a search input
    ARGS: Search term (in case someone wants to put input outside function)
    Returns: list of websites """
    
    only_results = []
    for i in range(4) :
        if google_search == True :
            time.sleep(30)
        else :
            pass
        if i > 0 :
            
            # Open Google Web page
            if google_search == True :
                res = open_google(page=i)
            else : 
                res = requests.get(URL)
            # html = bs4.BeautifulSoup(res)
        
            #print(text)
        
            soup = bs4.BeautifulSoup(res.text,"lxml")
            
            all_links = soup.find_all('h3', class_="r")
            for i in all_links :
                
                print(i)
            
            
##            for i  in all_links :
##                if 'settings/' not in i['href'] and 'webcache' not in i['href'] and 'accounts.google' not in i['href'] :
##                ## Many cases where the link starts with https or just //www. Strips all that for simplicity
##                    i['href'] = i['href'].lstrip('//')
##                    if  '/url?q' in i['href'] :
##                        only_results.append(i['href'].replace('/url?q=',''))
##                    else :
##                        only_results.append(i['href'])
##    print(only_results)
    return all_links


# error handling
def collect_email(URL) :
    res = requests.get(URL)
    text = bs4.BeautifulSoup(res.text,"lxml")
    text = str(text)
    text = text.split(" ")
    all_emails = []
    for i in range(len(text)-1) :
        if '@' in text[i] and "." in text[i] and len(text[i])<20 :
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
           

            #email = strip[
# collect_URLS(search=None) 
Google_Links = collect_URLS(google_search= True)
print(Google_Links)
print(len(Google_Links))
##email_collection = []
##for i in Google_Links :
##   try:
##       website_links = collect_URLS(URL=i)
##       print("The websites collected for this restaurant is, ", website_links)
##            # website_links pulls all the URLS it finds from its home page.
##       for j in website_links :
##            try: 
##                time.sleep(2)
##                print("The Link being checked is: ", j)
##                temp_email = collect_email(j)
##                print(temp_email)
##                if temp_email != None :
##                    email_collection.append(collect_email(j))
##            except Exception as e :
##                print("Error in collecting emails. Here is the error: ", e)
##   except Exception as e :
##        print("Error with collecting collect the 2nd level of links", e)
##print(email_collection)

# collect all URLS associated with webpage
# Try to pull email from webpage
# pull title of webpage
# Pull all links from this webpage
# then repeat process of trying to pull email
# Navigate to next page by adding &start=10 to end of url



# Resources used:
# Google search parameters https://moz.com/blog/the-ultimate-guide-to-the-google-search-parameters
# web scraping https://automatetheboringstuff.com/chapter11/

import requests, bs4, time
def collect_URLS(search=None) : 
    """Collects URLS from Google based on a search input
    ARGS: Search term (in case someone wants to put input outside function)
    Returns: list of websites """
    search_string = "kingston restaurants"
    for i in range(10) :
        if i >= 0 :
            # Open Google Web page
            URL = 'http://www.google.com/search?q='+search_string+"&start="+str(i*10)
            
            res = requests.get(URL)
            
            # html = bs4.BeautifulSoup(res)
        
            #print(text)
        
            soup = bs4.BeautifulSoup(res.text,"lxml")
            
            all_links = soup.find_all('a', href=True)
            print(all_links)
            only_results = []
        
            for i  in all_links :
                if '/url?q' in i['href'] and 'settings/' not in i['href'] and 'webcache' not in i['href'] :
                    only_results.append(i['href'].replace('/url?q=',''))
    print(only_results)
    return only_results
#    print(type(all_links))
#    print(only_results)
#    print(set(only_results))
#    print("the length is", len(only_results))
#    print("the new length is", len(set(only_results)))
#
#    for i in only_results :
#        pass
# error handling
def collect_email(URL) :
    res = requests.get(URL)
    text = bs4.BeautifulSoup(res.text,"lxml")
    text = str(text)
    text = text.split(" ")
    all_emails = []
    for i in range(len(text)-1) :
        if '@' in text[i] and "." in text[i] and len(text[i])<20:
            strip = text[i]
            all_emails.append(strip)
    return all_emails
def data_clean(email_list) :
    """ Cleans all emails"
    arg: email data
    return: email data without common errors like quotations
    removes emails that are images"""
    pass
           

            #email = strip[
URL = 'https://www.benchmarkemail.com/help-FAQ/answer/How-do-I-add-a-link-in-my-email-to-a-Webpage-Email-address-Anchor-or-Survey'
# collect_URLS(search=None) 
Google_Links = collect_URLS()
for i in Google_Links :
    print(collect_email(i))


# collect all URLS associated with webpage
# Try to pull email from webpage
# pull title of webpage
# Pull all links from this webpage
# then repeat process of trying to pull email
# Navigate to next page by adding &start=10 to end of url



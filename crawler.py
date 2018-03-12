# Resources used:
# Google search parameters https://moz.com/blog/the-ultimate-guide-to-the-google-search-parameters
# web scraping https://automatetheboringstuff.com/chapter11/

import requests, bs4, time
def collect_URLS(search=None) : 
    search_string = input("What would you like to collect data for?")
    # Open Google Web page
    res = requests.get('http://www.google.com/search?q='+search_string)

    # html = bs4.BeautifulSoup(res)
    text = bs4.BeautifulSoup(res.text)

    print(text)

    soup = bs4.BeautifulSoup(res.text)

    all_links = soup.find_all('a', href=True)

    only_results = []

    for i  in all_links :
        if '/url?q' in i['href'] and 'settings/' not in i['href'] and 'webcache' not in i['href'] :
            only_results.append(i['href'].replace('/url?q=',''))
    print(type(all_links))
    print(only_results)
    print(set(only_results))
    print("the length is", len(only_results))
    print("the new length is", len(set(only_results)))

    for i in only_results :
        pass
# error handling
def collect_email(URL) :
    res = requests.get(URL)
    text = bs4.BeautifulSoup(res.text)
    print(text)
    for i in range(len(text)) :
        if text[i] == '@' :
            strip = text[i:].split(' ',1)[0]
            return strip
            #email = strip[
URL = 'https://stackoverflow.com/questions/22767509/python-get-the-x-first-words-in-a-string'
# collect_URLS(search=None) 
print(collect_email(URL))

# collect all URLS associated with webpage
# Try to pull email from webpage
# pull title of webpage
# Pull all links from this webpage
# then repeat process of trying to pull email
# Navigate to next page by adding &start=10 to end of url



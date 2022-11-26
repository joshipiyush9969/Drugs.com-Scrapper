import bs4
import requests
import pandas

import medicine


def makeLink(link):
    return 'https://www.drugs.com' + link
    
#MEDS NAME
def makeDF():
    read_more = []
    for item in med_links:
        read_more.append(makeLink(item))
    
    data = {"names":med_names, "Read More":read_more}
    df = pandas.DataFrame(data= data)
    print(df.to_string())

# Single Medicine
input_initial = input("Enter Medicine Initial(a,b,c,d,1,0, etc..): ").lower()

URL = f"https://www.drugs.com/alpha/{input_initial}.html"
page = requests.get(URL)
soup = bs4.BeautifulSoup(page.content,'html.parser')
med_names = soup.find('ul',class_ = 'ddc-list-column-2').text.split("\n")
med_links = [str(a['href']) for a in soup.select('.ddc-list-column-2 a')]


makeDF()


input_med = input("Enter Medicine Name: ").lower()


for item in med_links:
    if input_med in item:
        curr_link = makeLink(item)
        med_page = requests.get(curr_link)
        med_soup = bs4.BeautifulSoup(med_page.content,'html.parser') 
        medicine.explore_med(med_soup)

    else:
        pass






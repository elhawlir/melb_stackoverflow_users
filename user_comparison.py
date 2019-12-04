
# need to scrape stackoverflow and provide reputation score for a
# particular user

def final_rank():
    import requests
    from bs4 import BeautifulSoup
    import re
    url = input("Enter the user's stackoverflow url: ") #take url input from user
    r = requests.get(url) #fetch the url
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'lxml') #parses the webpage
    
    rep_score = soup.find_all('div', class_='grid--cell fs-title fc-dark') #this class contains the reputation score
    rep_score = list(rep_score)

    for i in rep_score:
        match = re.findall(r"([0-9,]+)", str(i)) #matching for numbers and commas for the final score
        match = match[0].replace(',','')
        match = int(match)
   

    import pandas as pd
    melb_df = pd.read_csv('QueryResults.csv') #reads in downloaded file provided by stackoverflow_melb.py

    rep_melb = list(sorted(melb_df['Reputation'],reverse=True)) #sorts and lists all the Melbourne users reputation scores in descending order

    bigger_list = [] #will contain values higher individual reputation score
    [bigger_list.append(i) for i in rep_melb if i > match] #adding values higher than individual score to list
    percentage_rank = round((len(bigger_list)/len(rep_melb))*100,2) #calculating what rank user will have compared with the rest of Melbourne
    print(url, "is in the top", percentage_rank, "percent of Melbourne Stackoverflow users based on reputation") #final statement

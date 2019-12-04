from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.common.keys import Keys
import webbrowser 

# website contains a stackoverflow query that lists all the users from Melbourne
# it's worth noting some users don't record their location, so the list is not exhaustive

driver.get('https://data.stackexchange.com/stackoverflow/query/1162148/stackoverflow-users-in-melbourne') #connects to and opens url in new tab
rep = driver.find_elements_by_xpath('.//a[@id="resultSetsButton"]') #section where download csv link can be found
rep_scores = []
for i in rep:
    rep_scores.append(i.get_attribute('href')) #saves the link of the csv version of the tabled results

driver.quit() #shuts down the browser

webbrowser.open(rep_scores[0]) #opens the link you just found in a new browser and downloads the csv file


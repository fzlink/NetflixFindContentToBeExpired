import time
from selenium import webdriver

driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe') 
driver.get('https://www.netflix.com/Login?locale=tr-TR') #Enter local Netflix Login Page
time.sleep(1) 
username= 'username'  #Enter Netflix email
password= 'password'  #Enter Netflix password
loginBox = driver.find_element_by_name('userLoginId')
passwordBox = driver.find_element_by_name('password')
loginBox.send_keys(username)
passwordBox.send_keys(password)
#search_box.send_keys('ChromeDriver')
loginBox = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div[1]/form/button")
loginBox.click()
time.sleep(1) # Let the user actually see something!
driver.get("Enter Profile URL")
time.sleep(0.1)
driver.get("https://www.netflix.com/browse/my-list")
time.sleep(5)
items = driver.find_elements_by_class_name("title")
titles = []
for item in items:
    titles.append(item.text)
driver.get("https://unogs.com/countrydetail")
time.sleep(1)

countries = driver.find_elements_by_class_name("gencsinfo")
countryIndex = 0
for country in countries:
    countryIndex+=1
    if "Turkey" in country.text: #Enter Country Name
        break

countryExpireBox = driver.find_element_by_xpath("/html/body/div[10]/div["+str(countryIndex)+"]/div/div[2]/button[2]")
countryExpireBox.click()
time.sleep(1)
movies = driver.find_elements_by_class_name("videodiv")
expireMovieLen = len(movies)
expirationMovies = []
expireDates = []
for index in range(1,expireMovieLen+1):
    movieTitle = driver.find_element_by_xpath("/html/body/div[10]/div["+str(countryIndex)+"]/div/div[3]/div[3]/div["+str(index)+"]/div[3]/b/span")
    expireDate = driver.find_element_by_xpath("/html/body/div[10]/div["+str(countryIndex)+"]/div/div[3]/div[3]/div["+str(index)+"]/b/span")
                                              
    expirationMovies.append(movieTitle.text)
    expireDates.append(expireDate.text)


for expireIndex,expireMovie in enumerate(expirationMovies):
    for myMovieIndex,myMovie in enumerate(titles):
        if(expireMovie == myMovie):
            print("-----------------")
            print(expireMovie +"\n" +expireDates[expireIndex])
            
driver.close()

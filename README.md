# NetflixFindContentToBeExpired

This script tells you which content will leave from your Netflix List

## Installation
```python
pip install selenium
```
## Usage
```python
#Enter local Netflix Login Page
driver.get('https://www.netflix.com/Login?locale=tr-TR') 

#Enter Netflix email
username= 'username'  

#Enter Netflix password
password= 'password' 

countries = driver.find_elements_by_class_name("gencsinfo")
countryIndex = 0
for country in countries:
    countryIndex+=1
    #Enter Country Name
    if "Turkey" in country.text: 
        break
```

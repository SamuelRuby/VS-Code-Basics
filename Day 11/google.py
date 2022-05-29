import time
from selenium import webdriver


browser = webdriver.Chrome() #or webdriver.Firefox if you are using firefox

url = 'https://duckduckgo.com'
#url = 'https://google.com'
browser.get(url)
#browser.get('https://duckduckgo.com')

"""
<input type = 'text' class='' id='' name='??'/>
<textarea><textarea>
<input name="q" type="text">
"""
time.sleep(2)
name= 'q'
search_el = browser.find_element_by_name('q')
#print(search_el)
#or with css
# search_el = browser.find_element_by_css_selector('h1')

#to send texts to the above elements, like typing something in the search bar

search_el.send_keys('Selenium python')
#browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src, 'consent.google.com')]")) 
time.sleep(3) 
#browser.find_element_by_xpath('//*[@id="introAgreeButton"]/span/span').click()
#these have the abiltity to click
'''
<input type= 'submit' />
<button type= 'submit' />
<form></form> 

<input type="submit"> 
''' 
submit_btn_el = browser.find_element_by_css_selector("input[type='submit']")
print (submit_btn_el.get_attribute('name'))
time.sleep(2)
submit_btn_el.click()
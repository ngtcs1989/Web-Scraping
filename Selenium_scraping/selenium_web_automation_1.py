
# coding: utf-8

# In[21]:

from selenium import webdriver
import time
#reference : http://selenium-python.readthedocs.io/locating-elements.html
browser=webdriver.Chrome()
browser.set_window_size(1024,768)
browser.get('https://leetcode.com/accounts/login/')
query = "//input[@id='id_login']"
mail= 'naveengt1989@gmail.com'
browser.find_element_by_xpath(query).click()
browser.find_element_by_xpath(query).clear()
browser.find_element_by_xpath(query).send_keys(mail)
query = "//input[@id='id_password']"
password= 'kl5p2099'
browser.find_element_by_xpath(query).click()
browser.find_element_by_xpath(query).clear()
browser.find_element_by_xpath(query).send_keys(password)
query = "//button[@class='btn btn-primary']"
browser.find_element_by_xpath(query).click()

query = "//table[@id='problemList']/tbody/tr"
table = browser.find_elements_by_xpath(query)
cnt=0
for row in table:
    query = "./td"
    cols = row.find_elements_by_xpath(query)
    print "id: ",cols[1].text
    print "link: ",cols[2].find_element_by_xpath("./a").get_attribute('href')
    print "problem: ",cols[2].text
    print "accuracy: ",cols[3].text
    print "difficulty: ",cols[6].text
    if(cols[0].find_element_by_xpath("./span").get_attribute('class') == "ac"):
        print "status: SOLVED"
    else:
        print "status: NOT SOLVED"
    cols[2].find_element_by_xpath("./a").click() 
    time.sleep(2)
    browser.execute_script("window.history.go(-1)")
    time.sleep(2)
    # elem.tag_name
    # time.sleep(5)
    print "############################\n\n"    
    cnt += 1
    if cnt>5:
        break


# In[ ]:




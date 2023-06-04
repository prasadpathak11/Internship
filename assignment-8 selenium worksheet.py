#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install selenium')


# In[2]:


import selenium


# In[3]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

import warnings
warnings.filterwarnings('ignore')


# In[4]:


driver = webdriver.Chrome (r'chromedriver.exe')


# In[5]:


driver.get ('https://www.naukri.com/')


# In[ ]:





# # QUESTION NO. = 1

# In[6]:


designation = driver.find_element (By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Analyst')


# In[7]:


location = driver.find_element (By. XPATH, "/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys('Banglore')


# In[8]:


# here in the above case the 'class name' is same for both 'designatio & location', therfore for 'designation- we use 'CLASS_NAME'
# and for location we are using'ABSOLUTE XPATH'


# In[9]:


search = driver.find_element (By.CLASS_NAME, "qsbSubmit")
search.click()


# In[10]:


# now upto here we are having all the pagewise data for "data analyst" for "banglore" location.


# In[ ]:





# In[12]:


# now below we are finding and makiing data frame top 10 companies list with mentioned criteria:

job_title = []
job_location = []
company_name = []
experiance_required = []


# for job_title :-

title_all = driver.find_elements (By.XPATH,'//a[@class="title ellipsis"]')
for i in title_all [0:10]:
    title = i.text
    job_title.append(title)
    
    
#  for job_location :-

location_all = driver.find_elements (By.XPATH, '//span[@class="ellipsis fleft locWdth"]')
for i in location_all [0:10]:
    location = i.text
    job_location.append(location)
    
    
# for company_name :-

company_all = driver.find_elements (By.XPATH, '//a[@class="subTitle ellipsis fleft"]')
for i in company_all [0:10]:
    name = i.text
    company_name.append(name)
    
    
# for experiance_required :-

experiance_required = driver. find_elements (By.XPATH, '//span[@class="ellipsis fleft expwdth"]')
for i in experiance_required [0:10]:
    experiance = i.text
    experiance_required.append(experiance)
    exp1 = experiance_required[0:10]
# to identify whether the length of all lists are same or not

len(job_title),len(job_location),len(company_name),len(exp1)


# In[13]:


import pandas as pd


# In[14]:


df = pd.DataFrame({'Job Title':job_title, 'Location':job_location, 'Company':company_name, 'Experiance':exp1})
df


# In[ ]:





# # QUESTION NO. = 2

# In[15]:


driver.get ('https://www.naukri.com/')


# In[16]:


designation = driver.find_element (By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Scientist')


# In[17]:


location = driver.find_element (By. XPATH, "/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys('Banglore')


# In[18]:


search = driver.find_element(By.CLASS_NAME, 'qsbSubmit')
search.click()


# In[19]:


ds_job_title = []
ds_job_location = []
ds_company_name = []
ds_experiance_required = []


# In[20]:


title_tag1 = driver.find_elements (By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tag1[0:10]:
    title1 = i.text
    ds_job_title.append(title1)


# In[21]:


len(ds_job_title)


# In[22]:


title_tag2 = driver.find_elements (By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in title_tag2[0:10]:
    title2 = i.text
    ds_job_location.append(title2)


# In[23]:


len(ds_job_location)


# In[24]:


title_tag3 = driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in title_tag3[0:10]:
    title3 = i.text
    ds_company_name.append(title3)


# In[25]:


len(ds_company_name)


# In[26]:


title_tag4 = driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in title_tag4[0:10]:
    title4 = i.text
    ds_experiance_required.append(title4)


# In[27]:


len(ds_experiance_required)


# In[28]:


import pandas as pd

df = pd.DataFrame({'Job Tile':ds_job_title, 'Location':ds_job_location, 'Company Nmae':ds_company_name, 'Experiance':ds_experiance_required})


# In[29]:


df


# In[ ]:





# In[ ]:





# # Question No.- 3

# In[30]:


driver.get ('https://www.naukri.com/')


# In[31]:


designation = driver.find_element (By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Scientist')


# In[32]:


search = driver.find_element(By.CLASS_NAME, 'qsbSubmit')
search.click()


# In[33]:


ds_loc = driver.find_element (By.XPATH,'/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[5]/div[2]/div[2]/label/i')


# In[34]:


ds_loc.click()


# In[35]:


ds_sal = driver.find_element (By.XPATH,'/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[6]/div[2]/div[2]/label/i')
ds_sal.click()


# In[36]:


ds_job_title_ncr = []
ds_job_location_ncr = []
ds_company_name_ncr = []
ds_experiance_required_ncr = []


# In[37]:


title_ncr = driver.find_elements (By. XPATH, '//a[@class="title ellipsis"]')
for i in title_ncr [0:10]:
    title1 = i.text
    ds_job_title_ncr.append(title1)


# In[38]:


len(ds_job_title_ncr)


# In[39]:


location_ncr = driver.find_elements (By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_ncr [0:10]:
    location1 = i.text
    ds_job_location_ncr.append(location1)


# In[40]:


len(ds_job_location_ncr)


# In[41]:


company_ncr = driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_ncr [0:10]:
    company1 = i.text
    ds_company_name_ncr.append(company1)


# In[42]:


len(ds_company_name_ncr)


# In[43]:


experiance_ncr = driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experiance_ncr[0:10]:
    exp2 = i.text
    ds_experiance_required_ncr.append(exp2)


# In[44]:


ds_experiance_required_ncr


# In[45]:


len(ds_experiance_required_ncr)


# In[46]:


import pandas as pd


# In[47]:


df = pd.DataFrame({'Job Title':ds_job_title_ncr,'Job Location': ds_job_location_ncr, 'Company Name':ds_company_name_ncr, 'Experiance':ds_experiance_required_ncr})
df


# In[ ]:





# In[ ]:





# # Question No.- 4

# In[68]:


driver.get ('https://www.flipkart.com')


# In[69]:


search = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
search.send_keys('sunglasses')


# In[71]:


find = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
find.click()


# In[72]:


sunglasses = driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
len(sunglasses)


# In[73]:


sunglass_brand = []
sun_pro_disc = []
sunglasses_price = []


# In[ ]:





# In[74]:


s_brand = []
start=0
end=3
for page in range(start,end):
    brand = driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in brand:
        s_brand.append(i.text)
    next_button = driver.find_element (By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[75]:


sunglasses_brand = s_brand[0:100]
len(sunglasses_brand)


# In[76]:


s_disc = []
start=0
end=3
for page in range(start,end):
    discription = driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in discription:
        s_disc.append(i.text)
    next_button = driver.find_element (By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[77]:


sun_pro_disc = s_disc[0:100]
len(sun_pro_disc)


# In[78]:


s_price = []
start=0
end=3
for page in range(start,end):
    price = driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in price:
        s_price.append(i.text)
    next_button = driver.find_element (By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[79]:


sunglasses_price = s_price[0:100]
len(sunglasses_price)


# In[80]:


import pandas as pd


# In[81]:


df = pd.DataFrame({'Brand':sunglasses_brand,'Product Discription':sun_pro_disc,'Price':sunglasses_price})
df


# In[ ]:





# # Question No.-5

# In[82]:


driver.get ('https://www.flipkart.com')


# In[ ]:


search = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
search.send_keys('apple iphone 11 black 64 gb')


# In[ ]:


find_button = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
find_button.click()


# In[ ]:


phone = driver .find_element(By.CLASS_NAME,'_4rR01T')
phone.click()


# In[ ]:


rating_all = []
review_summary = []
full_review = []


# In[ ]:


star_rating = driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')


# In[ ]:


star_rating


# In[ ]:


# i think there is problem with above "flipkart code", because i have tried soo many times with different 'class-name', 
# 'absolute-xpath', 'relative-xpath', but always the output list is shown empty, weather the same code is working with the flip-
# -kart other products / questions.  so unable to this particular question. PLEASE PROVIDE THE SOLUTION FOR THE ABOVE QUESTION.


# In[ ]:





# # Question No.- 6

# In[83]:


driver.get ('https://www.flipkart.com')


# In[84]:


search = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
search.send_keys('sneakers')


# In[85]:


find_button = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
find_button.click()


# In[86]:


brand_all = []
discription_all = []
price_all = []


# In[87]:


brand = driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand [0:40]:
    brand1 = i.text
    brand_all.append(brand1)


# In[88]:


len(brand_all)


# In[89]:


brand_name = []


# In[90]:


start=0
end=3
for page in range (start,end):
    name = driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in name:
        brand_name.append(i.text)
    next_button = driver.find_element (By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[91]:


len(brand_name)


# In[92]:


brand_all = brand_name[0:100]
len(brand_all)


# In[93]:


disc = []
start=0
end=3
for page in range (start,end):
    discription = driver.find_elements (By.XPATH,'//a[@class="IRpwTa"]')
    for i in discription:
        disc.append(i.text)
    next_button = driver.find_element (By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)
    


# In[94]:


discription_all = disc[0:100]
len(discription_all)


# In[95]:


price = []
start=0
end=3
for page in range(start,end):
    rate = driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in rate:
        price.append(i.text)
    next_button = driver.find_element (By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[96]:


price_all = price [0:100]
len(price_all)


# In[97]:


len(brand_all),len(discription_all),len(price_all)


# In[98]:


import pandas as pd


# In[99]:


df = pd.DataFrame({'Brand Name':brand_all,'Product Discription':discription_all,'Price':price_all})
df


# In[ ]:





# # Question No.- 7

# In[100]:


driver = webdriver.Chrome (r'chromedriver.exe')


# In[101]:


driver.get('https://www.amazon.in/')


# In[102]:


title_all =[]
ratings_all =[]
price_all =[]


# In[103]:


title_tag = driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
title_tag.send_keys('LAPTOP')


# In[104]:


search_button = driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
search_button.click()


# In[105]:


filter_cpu = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[6]/span[11]/li/span/a/div/label/i')
filter_cpu.click()


# In[ ]:





# In[106]:


laptop_title = driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
for i in laptop_title[0:10]:
    laptop = i.text
    title_all.append(laptop)


# In[107]:


title_all = laptop_title[0:10]


# In[108]:


len(title_all)


# In[ ]:





# In[109]:


laptop_rating = driver.find_elements(By.XPATH,'//span[@class="a-icon-alt"]')
for i in laptop_rating[0:10]:
    rating = i.text
    ratings_all.append(laptop)


# In[110]:


ratings_all = laptop_rating[0:10]
len(ratings_all)


# In[111]:


laptop_price = driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in laptop_price[0:10]:
    price1 = i.text
    price_all.append(price1)


# In[112]:


price_all = laptop_price[0:10]
len(price_all)


# In[113]:


len(title_all),len(ratings_all),len(price_all)


# In[ ]:





# In[114]:


import pandas as pd


# In[115]:


df = pd.DataFrame({'Title':title_all,'Ratings':ratings_all,'Price':price_all})
df


# In[ ]:





# In[ ]:





# # Question- 8

# In[137]:


driver.get ('https://www.azquotes.com/')


# In[138]:


top_quotes = driver .find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a')
top_quotes.click()


# In[139]:


quotes = []
author = []
type_of_quotes = []


# In[154]:


# start=0
# end=10
# for page in range (start,end):
#     quotes_tag = driver.find_elements(By.XPATH,'//a[@class="title"]')
#     for i in quotes_tag:
#         quotes.append(i.text)
#     next_button = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]/li[12]/a')
#     next_button.click()
#     time.sleep(5)


# In[155]:


quotes_tag = driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in quotes_tag[0:100]:
    quot = i.text
    quotes.append(quot)


# In[159]:


quotes_all = quotes[0:100]


# In[160]:


len(quotes_all)


# In[ ]:





# In[163]:


author = []
author_tag = driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in author_tag[0:100]:
    auth = i.text
    author.append(auth)


# In[166]:


len(author)


# In[ ]:





# In[168]:


type_of_quote = []
type_tag = driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in type_tag[0:100]:
    typ = i.text
    type_of_quote.append(typ)


# In[170]:


len(type_of_quote)


# In[ ]:





# In[172]:


import pandas as pd


# In[173]:


df = pd.DataFrame({'Quote':quotes_all,'Author':author,'Type Of Quote':type_of_quotes})
df


# In[ ]:





# In[ ]:





# In[ ]:





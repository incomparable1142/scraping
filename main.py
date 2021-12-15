import pandas as pd
import pdb
from selenium import webdriver
from bs4 import BeautifulSoup
import glob
from config import *

for j in range(101, 2009):
    url = ''
    try:
        url = URL + str(j)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument('log-level=3')
        driver = webdriver.Chrome("/home/gaurav/pythonProject/hcl/chromedriver", chrome_options=chrome_options)

        driver.implicitly_wait(50)
        driver.get(url)
        username = driver.find_element_by_name("username")
        username.clear()
        username.send_keys(EMAIL)
        password = driver.find_element_by_name("password")
        password.clear()
        password.send_keys(PASSWORD)
        res = driver.find_element_by_class_name("submit-row").click()

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        table = driver.find_element_by_id("result_list")

        thead = table.find_element_by_tag_name("thead")
        columns = ['FIRST NAME', 'LAST NAME', 'PHONE NUMBER', 'DATE JOINED', 'BALANCE', 'PREMIUM TAG', 'COUNTRY OF ORIGIN',
                   'REFERRER CODE', 'REFEREE CODE', 'EMAIL']

        res = []
        table_rows = table.find_elements_by_tag_name("tr")
        for n, tr in enumerate(table_rows):
            if n == 0:
                pass
            else:
                td = tr.find_elements_by_tag_name('td')
                row = []
                for i in td:
                    row.append(i.text.strip())
                row.insert(1, tr.find_elements_by_tag_name('th')[0].find_elements_by_tag_name('a')[0].text)
                if row:
                    res.append(row)
        df = pd.DataFrame(res)
        print(df)
        filename= "/home/gaurav/pythonProject/hcl/files/%s.csv" % str(j)
        df.to_csv(filename, index=False)
        driver.close()
    except Exception as e:
        print(e)

# merging the files
path =r'/home/gaurav/pythonProject/hcl/files'
# A list of all joined files is returned
joined_list = glob.glob(path + "/*.csv")
# # Finally, the files are joined
columns = ['', 'EMAIL', 'FIRST NAME', 'LAST NAME', 'PHONE NUMBER', 'DATE JOINED', 'BALANCE', 'IS OFFER', 'IS PHONE CONFIRMED', 'COMMENT', 'GET DESC', 'GET APP STATUS', 'GET APP TYPE', 'PREMIUM TAG', 'COUNTRY OF ORIGIN', 'REFERRER CODE', 'REFEREE CODE']

df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
df.columns = columns
df.to_csv('output.csv', index=False)
print(df)

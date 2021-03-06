from selenium import webdriver
import time
import re
import calendar
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
expNote = 'https://keep.google.com/#NOTE/1445630158926.1066527822'
account = ''
password = ''

p = re.compile(r'(?P<day>\d{2})(?P<month>\d{2});(?P<detail>[^;]*);(?P<category>[^;]*);(?P<amount>\d*.*\d*);'
               r'(?P<currency>\w{3})', re.I | re.M)

def logingoog(mail, passw):
    driver.get("http://keep.google.com/")
    driver.find_element_by_id('Email').send_keys(mail)
    driver.find_element_by_id('next').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="Passwd"]').send_keys(passw)
    driver.find_element_by_id('signIn').click()


def getexpenses(note):
    global expenses
    driver.get(note)
    time.sleep(1)
    expenses = p.findall(driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div[1]/div[5]').text)
    #expenses = p.findall(driver.find_element_by_css_selector('div.VIpgJd-TUo6Hb.XKSfm-L9AdLc.eo9XGd').text)

print('Logging in...')
log = time.time()
logingoog(account, password)
logged = time.time() - log

print('Getting Expenses...')
get = time.time()
getexpenses(expNote)
gotten = time.time()-get
print(expenses)

print('Processing expenses...')
process = time.time()
for i in range(len(expenses)):
    day = expenses[i][0]
    month = expenses[i][1]
    detail = expenses[i][2]
    category = expenses[i][3]
    amount = expenses[i][4]
    currency = expenses[i][5]
    print('You spent {} {} on the {} of {} in {} which enters in the category {}.'.format(amount, currency, day,
                                                               calendar.month_name[int(month)], detail, category))
processed = time.time() - process

print('It took {} for the whole thing but just {} to get the expenses. To process the expenses it took {}.'
      .format(logged + gotten, gotten, processed))
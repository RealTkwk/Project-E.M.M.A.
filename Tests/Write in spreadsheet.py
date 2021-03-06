import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
import time

json_key = json.load(open('')) #Insert json with key
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
gc = gspread.authorize(credentials)

sht = gc.open_by_key('1uVvqxtRWIBN8foiBLPFNVzRog-97ZXRlX7KpNA47GlM')

#print(sht.worksheet('October').row_count)
#print(sht.worksheet('October').acell('B'+str(10)).value)
#print(sht.worksheet('October').col_values('B'))

sstart = time.time()
e = 2
while sht.worksheet('October').acell('B'+str(e)).value != '':
        slastrow = e + 1
        e += 1

start = time.time()
lastrow = len(sht.worksheet('October').col_values(2)) + 1

print('To find the last row(lastrow) {}, it took {}.'.format(lastrow, time.time() - start))
print('To find the last row(slastrow) {}, it took {}.'.format(slastrow, time.time() - sstart))
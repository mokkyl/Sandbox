import requests
from lxml import html
from lxml.html import tostring
import time
import datetime

class SwChecker(object):
    def __init__(self, confirmation, firstname, lastname):
        self.confirmation = confirmation
        self.firstname = firstname
        self.lastname = lastname
        
    def attempt_checkin(self):
        r = requests.post('https://www.southwest.com/flight/retrieveCheckinDoc.html', data =
                         {'confirmationNumber':self.confirmation, 'firstName':self.firstname, 'lastName':self.lastname})
        tree = html.fromstring(r.content)
        return tree
    
    def find_bad_elements(self, tree):
        try:
            error_codes = tostring(tree.get_element_by_id('errors_props_wrapper'))
        except:
            error_codes = None
        
        return error_codes
    
    def parse_result(self, result):
        errors = ['SW302105',
                 'SW101081',
                 'SW301007',
                 'SW301008',
                 'SW301009',
                 'SW301010',
                 'SW301011',
                 'SW3011023']
        error_list = []
        
        for code in errors:
            if code in result:
                error_list.append(code)
        
        return error_list
    
    def send_checkin(self):
        result = self.attempt_checkin()
        bad_codes = self.find_bad_elements(result)
        if bad_codes == None:
            return 'All Good'
        else:
            stat = self.parse_result(bad_codes)
            return 'These error codes were found: ' + str(stat)
            #return bad_codes

conf = 'ddswdw'
fname = 'Nancy'
lname = 'Drew'

checkmein = SwChecker(conf, fname, lname)

flight_time = datetime.datetime(2016,3,9,21,0,0)
flight_buffer = flight_time + datetime.timedelta(days=-1, minutes=2)

while datetime.datetime.now() < flight_buffer:
    result = checkmein.send_checkin()
    timeleft = flight_buffer - datetime.datetime.now() - datetime.timedelta(minutes=2)
    testleft = flight_buffer - datetime.datetime.now()
    print result
    

    if result == 'All Good':
    	break

    elif flight_buffer - datetime.datetime.now() >= datetime.timedelta(minutes=3):
        print 'Time Difference is greater than 1 minute, time remaining to check-in : %s, delaying ...' % timeleft
        time.sleep(5)
    
    elif flight_buffer - datetime.datetime.now() < datetime.timedelta(minutes=3):
        print 'Time Difference is less than 1 minute, time remaining to check-in : %s, spamming ...' % timeleft
    
    elif flight_buffer < datetime.datetime.now():
        print 'deadline passed'
        break

print 'done!'

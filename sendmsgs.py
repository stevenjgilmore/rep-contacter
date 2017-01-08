import json
import settings 

from mechanize import Browser

listcontrols = ["radio","checkbox","select"]

def loadsenators():
   	with open('senators.json') as data_file:    
		data = json.load(data_file) 
	return data['senators']

def msgall(send=False):
	senators = filter(lambda s: s['locale'] == settings.PERSONAL['state'], loadsenators())
	br = Browser()
    # Ignore robots.txt
	br.set_handle_robots(False)
    # Google demands a user-agent that isn't a robot
	br.addheaders = [('User-agent', 'Firefox')]

	pages= []

	for senator in senators:
		br.open(senator['site'])
		br.form = list(br.forms())[senator['form']]  # use when form is unnamed

		for conkey in senator['controls']:
			control = br.form.find_control(conkey['name'])
			# print "type=%s, name=%s value=%s" % (control.type, control.name, br[control.name])

			# try to get value
			try: 
				value= settings.PERSONAL[conkey['key']]
			except Exception:
				if conkey['required']:
					value = conkey['default']
				else:
					continue

			# set value
			if control.type in listcontrols:
				control.value = [value]
			else:
				control.value = value 
				
			# print "type=%s, name=%s value=%s" % (control.type, control.name, br[control.name])
		if send == True: 
			response =  br.submit()
			pages.append(response)
		else:
			pages.append(br)
	return pages

from bottle import template, static_file, route, run, get, post, request, debug
from OmegaExpansion import relayExp
import omega_gpio

# pinStates is a string list(comma delimited) that determines the state of 
# Omega board pins. Each entry is a number followed by a pinState
# corresponding to this table
# 1on = button 1 lite on
# 1off = button 1 lite off
# R1on = relay 1 on
# R1off = relay 1 off

pinStates = "0off,1off,2off,3off"
pinStates2 = pinStates
loggedIn = False

# This is the number of pins that are controlled by buttons
pins = 3
# This is the number of relays that are controlled by buttons
relays = 1

# dictPins is a dictionary that translates the button numbers to the actual 
# Omega pin that needs to be changed. button numbers come from the client side.
dictPins = {
              0:15,
              1:16,
              2:17
}

# The for loop sets the direction for the pins(always output for this)
for x in range(0, pins):
	omega_gpio.initpin(dictPins[x],'out')

# Initialize the relay. If more than one expansion then this will need to use
# a for loop to do multiple units.
relayStatus = relayExp.driverInit(7)
if (relayStatus == 0):
	print('Relay is initialized')
else:
	print('Relay is NOT initialized')

# This sets all pins to off and all relays to open
for x in range(0, pins):
	omega_gpio.setoutput(dictPins[x], 1)
for x in range(0, relays):
	relayExp.setChannel(7,0,x)

# This allows use of files in the static directory
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root = './static/')


@route('/')
@post('/<pinStates>') 
def root1(pinStates=pinStates):
	global loggedIn
	print(loggedIn)
	global pinStates2
	if (loggedIn == False):	
		password = request.forms.get('password')
		print('below is return for password')
		print(password)
		if (password != '1234'):
			return template('login.tpl')
		else:
			loggedIn = True
			pinStates = pinStates2
	buttonNum = (str(request.forms.get('btnId'))).splitlines()
	buttonNum = buttonNum[0]
	print (buttonNum)
	if (buttonNum == 'None'):
		return template('gpio.tpl', pinStates = pinStates)
	buttonNum = int(buttonNum)	
	pinStates = pinStates2.split(',')
	if (pinStates[buttonNum] == '0on'):
		pinStates[buttonNum] = '0off'
		omega_gpio.setoutput(dictPins[buttonNum], 1)
	elif (pinStates[buttonNum] == '0off'):
		pinStates[buttonNum] = '0on'
		omega_gpio.setoutput(dictPins[buttonNum], 0)
	elif (pinStates[buttonNum] == '1on'):
		pinStates[buttonNum] = '1off'
		omega_gpio.setoutput(dictPins[buttonNum], 1)
	elif (pinStates[buttonNum] == '1off'):
		pinStates[buttonNum] = '1on'
		omega_gpio.setoutput(dictPins[buttonNum], 0)
	elif (pinStates[buttonNum] == '2on'):
		pinStates[buttonNum] = '2off'
		omega_gpio.setoutput(dictPins[buttonNum], 1)
	elif (pinStates[buttonNum] == '2off'):
		pinStates[buttonNum] = '2on'
		omega_gpio.setoutput(dictPins[buttonNum], 0)
	elif (pinStates[buttonNum] == '3on'):
		pinStates[buttonNum] = '3off'
		relayExp.setChannel(7,0,0)
	elif (pinStates[buttonNum] == '3off'):
		pinStates[buttonNum] = '3on'
		relayExp.setChannel(7,0,1)		
	else:
		print ('Unable to decode the pinStates string')
		print (pinStates)
	pinStates2 = ",".join(pinStates)
	print (pinStates2)
	return template('gpio.tpl', pinStates = pinStates2)
	
run(host = '0.0.0.0', port = 8080, debug = True, reloader = True)



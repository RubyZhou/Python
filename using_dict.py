#!/usr/bin/python
#Filename : using_dict.py


#'ab' is short for 'a'ddress'b'ook

ab={	'Swaroop' :'swaroopch@bytefpython.info',
	'Larry' :'larry@wall.org',
	'Matsumoto':'matz@ruby-lang.org',
	'Spammer':'spammer@hotmail.com'
}

print "Swaroop's address is %s"%ab['Swaroop']

#Adding a key/value pair
ab['Guido']='guido@python.org'

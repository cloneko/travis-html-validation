import nose
import os
import re
from py_w3c.validators.html.validator import HTMLValidator

files = []
results = {}

for root, dirs, file in os.walk('.'):
	for name in file:
		if re.search('.*\.html?$',name):
			validator = HTMLValidator()
			filepath = os.path.join(root,name)
			validator.validate_file(filepath)
			results[filepath] = {}
			results[filepath]['errors'] = validator.errors
			results[filepath]['warnings'] =  validator.warnings



def validation(key):
	count = 0
	for path,result in results.items():
		print '* ' + path + ': ' + str(len(result[key])) + ' ' + key
		if len(result[key]) > 0:
			errorcount = 0
			for error in  result[key]:
				errorcount += 1
				print '    ' + str(errorcount) +'. line ' + error['line'] + ': ' + error['message'].rstrip('\n')
		count += len(result[key])

	return count

def test_has_no_errors():
	assert validation('errors') == 0

def test_has_no_warnings():
	assert validation('warnings') == 0

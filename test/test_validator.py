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


def test_has_no_error():
	count = 0
	for path,result in results.items():
		print '* ' + path + ': ' + str(len(result['errors'])) + ' errors'
		if len(result['errors']) > 0:
			errorcount = 0
			for error in  result['errors']:
				errorcount += 1
				print '    ' + str(errorcount) +'. line ' + error['line'] + ': ' + error['message'].rstrip('\n')
		count += len(result['errors'])

	assert count == 0

def test_has_no_warnings():
	count = 0
	for path,result in results.items():
		print '* ' + path + ': ' + str(len(result['warnings'])) + ' warnings'
		if len(result['warnings']) > 0:
			errorcount = 0
			for error in  result['warnings']:
				errorcount += 1
				print '    ' + str(errorcount) +'. line ' + error['line'] + ': ' + error['message'].rstrip('\n')
		count += len(result['warnings'])

	assert count == 0

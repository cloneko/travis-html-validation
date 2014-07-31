import nose
import json
import sys
import os
import re
from py_w3c.validators.html.validator import HTMLValidator

files = []

for root, dirs, file in os.walk('.'):
	for name in file:
		if re.search('.*\.html?$',name):
			files.append(os.path.join(root,name))
	

def test_has_no_error():
	count = 0
	validator = HTMLValidator()
	for target in files:
		validator.validate_file(target) 
		print '* ' + target + ': ' + str(len(validator.errors)) + ' errors'
		if len(validator.errors) > 0:
			errorcount = 0
			for error in  validator.errors:
				errorcount += 1
				print '    ' + str(errorcount) +'. line ' + error['line'] + ': ' + error['message'].rstrip('\n')
		count += len(validator.errors)

	assert count == 0

def test_has_no_warnings():
	count = 0
	validator = HTMLValidator()
	for target in files:
		validator.validate_file(target) 
		print '* ' + target + ': ' + str(len(validator.warnings)) + ' warnings'
		if len(validator.warnings) > 0:
			errorcount = 0
			for error in  validator.warnings:
				errorcount += 1
				print '    ' + str(errorcount) +'. line ' + error['line'] + ': ' + error['message']
		count += len(validator.warnings)

	assert count == 0

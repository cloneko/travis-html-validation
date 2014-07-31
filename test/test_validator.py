import nose
import json
import sys
import glob
from py_w3c.validators.html.validator import HTMLValidator

files = glob.glob('*.html')

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
				print '    ' + str(errorcount) +'. line ' + error['line'] + ': ' + error['message']
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

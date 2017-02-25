from setuptools import setup
setup(name="systeminfo",
	version="0.1",
	description="Led light boord for UCD Science Centre",
	url="",
	author="Nkosi Ndlovu",
	author_email="nkosi.ndlovu@ucdconnect.ie",
	licence="GPL3",
	packages=['solve_led'],
	entry_points={
	'console_scripts':[
		'solve_led=src.main:main'
	]
	})
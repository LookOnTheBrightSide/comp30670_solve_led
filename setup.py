from setuptools import setup
setup(name="solve_led",
	version="0.2",
	description="Led light boord for UCD Science Centre",
	url="https://github.com/LookOnTheBrightSide/comp30670_solve_led",
	author="Nkosi Ndlovu",
	author_email="nkosi.ndlovu@ucdconnect.ie",
	license="GPL3",
	packages=['solve_led'],
	entry_points={
	'console_scripts':['solve_led=solve_led.main:main']
	})
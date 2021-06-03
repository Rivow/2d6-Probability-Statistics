from setuptools import setup, find_packeges

setup(name = "Catan Probabilitys",
	  version = "alpha 0.1",
	  description = "Catan probability visualizer",
	  packeges = find_packeges(),
	  install_requires = ['matplotlib', 'kivy']
	)
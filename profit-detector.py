#!/usr/bin/python
#################
#
# Python based profit deobfuscator for EVE Online.
#	Written by Brett Atkins, June 2015.
#
# Primarily for Tech I equipment so far, Profit Detector
# definitely enumerates how much manufacturing an item
# ACTUALLY costs. I have yet to find another tool that
# actually factors in all of the details.
#
# DISCLAIMER/WARNING
# CCP still does something nutso with the system index, 
# the job price is always off a tad. Still way better
# than EVE-Cost.
#
#################

### Constants ###
# global crest = "public-crest.eveonline.com/industry/systems/" # Properly implemented, crest eliminates the need to ask for the System Cost Index. Efficiency I'll write later.
global evecentral = "api.eve-central.com/api/evemon" # This is our price index for minerals. Of course custom variables are allowed.

### Inputs ###
	## Global ##
		# Initial Mineral Declarations #
		global tritanium = float(0)
		global pyerite = float(0)
		global mexallon = float(0)
		global isogen = float(0)
		global nocxium = float(0)
		global zydrine = float(0)
		global megacyte = float(0)

		# System Cost Index #
		global systemcost = float(0)

		# Station Tax #
		global stationtax = float(0)

	## Anticipated Locals ##
	##
	## Each Item will have the following locals, listed here for reference, but not declared.
		# itemname		# The item's name
		# defaultcomposition 	# An array identifying the default material composition of the item
		# melevel		# Material Efficiency level for the item
		# jobbasecost		# The base cost of the job (hover over the cost)
		# estimatedmineralcost	# Really_verbose_variable_name.jpg
		# saleprice		# The amount the item will be sold at.
		

### Outputs ###
		# skilledcomposition	# An array identifying the material composition after factoring in Material Efficiency.
		# jobcost		# The cost of starting the job
		# actualcost		# The total cost of development
		# profit		# sale - cost
		# profit-margin		# The percentage richer you are after selling the item. Sort of.

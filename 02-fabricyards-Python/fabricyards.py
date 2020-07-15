# fabricyards(inches)
# Fabric must be purchased in whole yards, so purchasing just 1 inch 
# of fabric requires purchasing 1 entire yard. With this in mind, 
# write the function fabricYards(inches) that takes the number of 
# inches of fabric desired, and returns the smallest number of whole 
# yards of fabric that must be purchased.

# fabricexcess(inches)
# Write the function fabricExcess(inches) that takes the number of 
# inches of fabric desired and returns the number of inches of excess 
# fabric that must be purchased (as purchases must be in whole yards)
# . Hint: you may want to use fabricYards, which you just wrote!
# 1 yard = 36 inches
import math

def fun_fabricyards(inches):
	val = inches/36
	return math.ceil(val)

def fun_fabricexcess(inches):
	val = fun_fabricyards(inches)
	return (val*36)-inches



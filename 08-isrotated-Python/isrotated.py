# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
	if str1 == str2[::-1]:
		return True
	position = str1.find(str2[0])
	str1 = str1[position:]+str1[:position]
	return str1 == str2
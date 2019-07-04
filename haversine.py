from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 6373.0

lat1 = radians(30.900810)
lon1 = radians(75.857198)
lat2 = radians(32.239620)
lon2 = radians(77.188758)

dLon = lon2 - lon1
dLat = lat2 - lat1

a = sin(dLat / 2)**2 + cos(lat1) * cos(lat2) * sin(dLon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print("Result:", distance)
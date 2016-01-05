import matplotlib.pyplot as plt
from pykml import parser

Y = parser.fromstring(open('Monitoring wells.kml', 'r').read())
name = []
x_coord = []
y_coord = []

for place in Y.Document.Folder.Placemark:
    name.append(str(place.name))
    coords = str(place.Point.coordinates)
    coords = coords.split(',')
    xf = coords[0]
    yf = coords[1]
    x_coord.append(float(xf))
    y_coord.append(float(yf))


Wells = zip(name, x_coord, y_coord)
Wells.sort(key=lambda x: x[0])

#print Wells


print x_coord


plt.figure()
plt.scatter(x_coord, y_coord)
plt.title('Well locations')
plt.show()
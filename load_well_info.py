import csv
import matplotlib.pyplot as plt
from pykml import parser
from numpy import linspace, meshgrid, array, float
from matplotlib.mlab import griddata
import matplotlib.tri as tri

'''Code to load in data for monitoring wells from a text file, and load their locations
from a kml file
'''

# parse the kml file
Y = parser.fromstring(open('Monitoring wells.kml', 'r').read())
name = []
x_coord = []
y_coord = []

# move data from the parsed kml file into a list of well names and well coordinates
for place in Y.Document.Folder.Placemark:
    name.append(str(place.name))
    coords = str(place.Point.coordinates)
    coords = coords.split(',')
    x_coord.append(float(coords[0]))
    y_coord.append(float(coords[1]))

Well_locations = zip(name, x_coord, y_coord)
Well_locations.sort(key=lambda x: x[0])  # sort so names are in alphabetical order

# turn this section on to make a plot of the wells
if False:
    plt.figure()
    plt.scatter(x_coord, y_coord)
    plt.title('Well locations')
    plt.show()

# next, we load in the well data from the file wells.txt
filename = 'wells.txt'

names = [x[0] for x in csv.reader(open(filename, 'rU'), delimiter='\t')]
depth_to_water = [x[1] for x in csv.reader(open(filename, 'rU'), delimiter='\t')]
depth_to_product = [x[2] for x in csv.reader(open(filename, 'rU'), delimiter='\t')]
product_thickness = [x[3] for x in csv.reader(open(filename, 'rU'), delimiter='\t')]
notes = [x[4] for x in csv.reader(open(filename, 'rU'), delimiter='\t')]
drill_method = [x[5] for x in csv.reader(open(filename, 'rU'), delimiter='\t')]
depth_to_sandpack = [x[6] for x in csv.reader(open(filename, 'rU'), delimiter='\t')]
total_depth = [x[7] for x in csv.reader(open(filename, 'rU'), delimiter='\t')]
loggable_depth = [x[8] for x in csv.reader(open(filename, 'rU'), delimiter='\t')]
saturated_depth = [x[9] for x in csv.reader(open(filename, 'rU'), delimiter='\t')]
lithology = [x[10] for x in csv.reader(open(filename, 'rU'), delimiter='\t')]

Well_info = zip(names, depth_to_water, depth_to_product, product_thickness, notes, drill_method, depth_to_sandpack,
                total_depth, loggable_depth, saturated_depth, lithology)
Well_info.sort(key=lambda x: x[0])  # sort so names are in alphabetical order

# unzip sorted data into holder variables
A1,A2,A3 = zip(*Well_locations)
B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, B11 = zip(*Well_info)

# make dictionary from holder variables
Well_data = {
    "Name": A1,
    "Latitude": A2,
    "Longitude": A3,
    "Depth to water": B2,
    "Depth to product": B3,
    "Product thickness": B4,
    "Notes": B5,
    "Drill method": B6,
    "Depth to sandpack": B7,
    "Total depth": B8,
    "Loggable depth": B9,
    "Saturated depth": B10,
    "Lithology": B11
}

'''
for key in Well_data:
    print key, Well_data[key]
'''

def grid(x,y,z, resX=100, resY=100):
    "Convert 3 column data to matplot grid"
    xi = linspace(min(x),max(x),resX)
    yi = linspace(min(y),max(y),resY)
    Z = griddata(x, y, z, xi, yi, 'linear')
    X, Y = meshgrid(xi, yi)
    return X, Y, Z

x = Well_data["Latitude"]
y = Well_data["Longitude"]
z = array(Well_data["Depth to water"]).astype(float)
X, Y, Z = grid(x, y, z)


T = tri.Triangulation(x, y)

if True:
    plt.figure()
    plt.contourf(X, Y, Z)
    plt.colorbar()
    plt.scatter(x, y)
    plt.title('Water levels (Dec 2014)')
    # plt.show()
    plt.savefig('water_levels_meshgrid.jpg')

if True:
    plt.figure()
    plt.tricontourf(T,z)
    plt.colorbar()
    plt.scatter(x, y)
    plt.title('Water levels (Dec 2014) triangulated')
    # plt.show()
    plt.savefig('water_levels_trigrid.jpg')

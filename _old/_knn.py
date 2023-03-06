### K-Nearest-Neighbor by Benjamin Fever
### This is a implementation of the K Nearest Neighbor Machine learning algorithm
# TODO: Clean up code, read files from command line, check all testing data

# Import any needed librarys 
from Util import Scanner  # Custom library I made to help read files
from math import sqrt
from collections import OrderedDict

# Function that returns the result of the min max scaling calculation
# Let min(x) be the minimum value for x, Let max(x) be the maximum value for x. x - min(x) / max(x) - min(x) 
def min_max_scaling(x, min, max):
    return ((x - min) / (max - min))

# Calculate the euclidean distance between point1 and point2 sqrt((p1 - p2)^2)
def euclidean_dist(point1, point2):
    total = 0
    for i in range(0, 13):
        total += (point1[i] - point2[i])**2
    return sqrt(total)

# Read the raw data files and return it as a nested list
def read_data(filepath):
    scanner = Scanner(filepath)
    data = []
    while scanner.has_next():
        value = []
        for i in range(0, 14):
            value.append(scanner.next_float())
        data.append(value)
    return data

#  Use the training data to find the mins and maxs for each category to use later
def train_data(data):
    mins = []
    maxs = []
    for x in range(0, 13):
        max = 0
        min = 999999
        for i in range(0, len(data)):
            num = data[i][x]
            if num > max:
                max = num
            if num < min:
                min = num
        mins.append(min)
        maxs.append(max)

    #  Normalize the data between values 0-1 so our data isn't skewed
    for point in data:
        normalize_point(point, mins, maxs)
        
    return data, mins, maxs

# This normalize a data point and all its values, returns the normalized point
def normalize_point(point, mins, maxs):
    for i in range(0, 13):
        point[i] = min_max_scaling(point[i], mins[i], maxs[i])
    return point

# This function calculates the nearest neigbors of count K and returns how many "votes" each class has
def find_class(point1, data, k):
    # Get the distance for all points
    order = {}
    for point2 in data:
        order.update({euclidean_dist(point1, point2): point2[13]})

    # Sort all the points by distance
    order = OrderedDict(sorted(order.items()))

    # Take the shortest distances, k times
    count = [0, 0, 0]
    for key, value in order.items():
        count[int(value)-1] += 1
        if (count[0] + count[1] + count[2] >= k):
            break

    return count
    
# Train data
data, mins, maxs = train_data(read_data("data\\wine-training"))
k = 21 # random k value
point1 = normalize_point([1.79, 2.13, 2.78, 28.5, 92.0, 2.13, 2.24, 0.58, 1.76, 3.0, 0.97, 2.44, 466.0], mins, maxs) # selected point from data file

class_counts = find_class(point1, data, k)

# print what class the point is
if (class_counts[0] > class_counts[1] and class_counts[0] > class_counts[2]):
    print("Class: 1")
if (class_counts[1] > class_counts[0] and class_counts[1] > class_counts[2]):
    print("Class: 2")
if (class_counts[2] > class_counts[0] and class_counts[2] > class_counts[1]):
    print("Class: 3")
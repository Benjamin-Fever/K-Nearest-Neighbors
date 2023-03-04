# K-Nearest-Neighbor by Benjamin Fever

from FileScanner import Scanner
from math import sqrt, pow
from collections import OrderedDict

filepath = __file__[0:len(__file__) - len("src\\knn.py")]

def min_max_scaling(x, min, max):
    return ((x - min) / (max - min))

def euclidean_dist(point1, point2):
    total = 0
    for i in range(0, 13):
        total += (point1[i] - point2[i])**2
    return sqrt(total)

def read_data(filename):
    scanner = Scanner(filepath + filename)
    data = []
    scanner.skip(14)
    while scanner.has_next():
        value = []
        for i in range(0, 14):
            value.append(scanner.next_float())
        data.append(value)
    return data

def train_data(data):
    # Train for the mins and maxs and normalizes the the training data
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

    for point in data:
        normalize_data(point, mins, maxs)
        
    return data, mins, maxs

def normalize_data(point, mins, maxs):
    for i in range(0, 13):
        point[i] = min_max_scaling(point[i], mins[i], maxs[i])
    return point


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
    

data, mins, maxs = train_data(read_data("data\\wine-training"))
k = 21
point1 = normalize_data([12.93, 3.8, 2.65, 18.6, 102.0, 2.41, 2.41, 0.25, 1.98, 4.5, 1.03, 3.52, 770.0], mins, maxs)

class_counts = find_class(point1, data, k)
if (class_counts[0] > class_counts[1] and class_counts[0] > class_counts[2]):
    print("Class: 1")
if (class_counts[1] > class_counts[0] and class_counts[1] > class_counts[2]):
    print("Class: 2")
if (class_counts[2] > class_counts[0] and class_counts[2] > class_counts[1]):
    print("Class: 3")
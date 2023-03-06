from Util import *
from sys import argv
from collections import OrderedDict

class K_Nearest_Neighbor:
    def __init__(self, k=3):
        self.training_data = []
        self.trained_mins = []
        self.trained_maxs = []
        self.k = k

    def training(self, filepath):
        self.training_data = self.read_data_file(filepath)

        # Train for mins and max's for min-max scaling
        for x in range(0, len(self.training_data[0]) - 1):
            values = []
            for y in range(0, len(self.training_data)):
                values.append(self.training_data[y][x])
            self.trained_mins.append(find_min(values))
            self.trained_maxs.append(find_max(values))
        
        # Normalize data points
        self.training_data = self.normalize_data(self.training_data)

    def normalize_point(self, point):
        for i in range(0, len(point) - 1):
            value = point[i]
            point[i] = min_max_scaling(value, self.trained_mins[i], self.trained_maxs[i])
        return point

    def normalize_data(self, data):
        for i in range(0, len(data)):
            data[i] = self.normalize_point(data[i])
        return data
        
    def read_data_file(self, filepath):
        scanner = Scanner(filepath)
        data = []
        while scanner.has_next():
            value = []
            for i in range(0, 14):
                value.append(scanner.next_float())
            data.append(value)
        return data

    def find_neighbors(self, point1):
        order = {}
        for point2 in self.training_data:
            total_dist = 0
            for i in range(0, len(point2)-1):
                total_dist += euclidean_dist(point1[i], point2[i])
            order.update({total_dist: point2[13]})
        order = OrderedDict(sorted(order.items()))
        count = 0
        neighbors = {}
        for key, value in order.items():
            count += 1
            neighbors.update({key: value})
            if count >= self.k:
                break

        return neighbors


if __name__ == "__main__":
    machine_learning = K_Nearest_Neighbor()
    machine_learning.training("F:\Software Projects\K-Nearest-Neighbors\data\wine-training")
    test = machine_learning.find_neighbors([13.05, 3.86, 2.32, 22.5, 85.0, 1.65, 1.59, 0.61, 1.62, 4.8, 0.84, 2.01, 515.0])
    pass
    # TODO: Check which class is more
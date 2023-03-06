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

    def classification(self, neighbors):
        class1 = class2 = class3 = 0
        for neighbor_key, neighbor_value in neighbors.items():
            if int(neighbor_value) == 1:
                class1 += 1
            elif int(neighbor_value) == 2:
                class2 += 1
            elif int(neighbor_value) == 3:
                class3 += 1
        if class1 > class2 and class1 > class3:
            return 1
        elif class2 > class1 and class2 > class3:
            return 2
        elif class3 > class1 and class3 > class2:
            return 3

    def testing(self, filepath):
        test_data = self.read_data_file(filepath)
        # Normalize data points
        test_data = self.normalize_data(test_data)
        
        classified = []
        for point in test_data:
            neighbors = self.find_neighbors(point)
            classified.append(self.classification(neighbors))
        print(classified)
        correct = 0
        for i in range(0, len(classified)):
            if (classified[i] == int(test_data[i][13])):
                correct += 1
        print("Accuracy: " + str(correct / len(test_data) * 100))


if __name__ == "__main__":
    print("K Value = 3")
    machine_learning = K_Nearest_Neighbor()
    machine_learning.training(str(argv[1]))
    machine_learning.testing(str(argv[2]))
    print("K Value = 1")
    machine_learning = K_Nearest_Neighbor(5)
    machine_learning.training(str(argv[1]))
    machine_learning.testing(str(argv[2]))
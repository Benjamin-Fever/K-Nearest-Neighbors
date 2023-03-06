### This is a utility class made by Benjamin Fever
### It follows the same idea as the java.util.Scanner
### Makes it easier to scan through a large file
import math

class Scanner:
    #  Sets the initial variables
    def __init__(self, filelocation):
        self.position = 0
        file = open(filelocation)
        file_read = file.read()
        self.line_count = len(file_read.splitlines())
        self.read_file = file_read.split()
        file.close()

    #  Returns the next word as a string
    def next(self):
        value = self.read_file[self.position]
        self.position+=1
        return value
    
    #  Returns the next int and sets the position to that point
    def next_int(self):
        value = None
        for i in range(self.position, len(self.read_file)):
            num = self.read_file[i]
            self.position+=1
            try:
                value = int(float(num))
                break
            except ValueError:
                continue
        return value
    
    #  Returns the next float and sets the position to that point
    def next_float(self):
        value = None
        for i in range(self.position, len(self.read_file)):
            num = self.read_file[i]
            self.position += 1
            try:
                value = float(num)
                break
            except ValueError:
                continue
        return value
    
    #  Reset position
    def reset(self):
        self.position = 0
    
    #  Get size of scanner
    def size(self):
        return len(self.read_file)
    
    #  Get line count
    def get_line_count(self):
        return self.line_count
    
    #  Return true if there is a word next, else return false
    def has_next(self):
        return self.position < self.size()

# Calculate the min-max scaling of a given value
def min_max_scaling(x, min_x, max_x):
    return ((x - min_x) / (max_x - min_x))

# Calculate the euclidean distance between point1 and point2 sqrt((p1 - p2)^2)
def euclidean_dist(point1, point2):
    return math.sqrt((point1 - point2) ** 2)

def find_min(values):
    min = math.inf
    for value in values:
        if (value < min):
            min = value
    return min

def find_max(values):
    max = -math.inf
    for value in values:
        if (value > max):
            max = value
    return max
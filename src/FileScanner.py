# This is a helper class made by Benjamin Fever

class Scanner(object):
    def __init__(self, filelocation):
        self.position = 0
        file = open(filelocation)
        file_read = file.read()
        self.line_count = len(file_read.splitlines())
        self.read_file = file_read.split()
        file.close()


    def next(self):
        value = self.read_file[self.position]
        self.position+=1
        return value
    
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
    
    def reset(self):
        self.position = 0
    
    def size(self):
        return len(self.read_file)
    
    def get_line_count(self):
        return self.line_count
    
    def has_next(self):
        return self.position < self.size()
    
    def skip(self, x):
        for i in range(0, x):
            self.next()

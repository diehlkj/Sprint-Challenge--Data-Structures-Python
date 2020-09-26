class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.contents = []
        self.clock = 0
        
    def __len__(self):
        return len(self.contents)
    
    def append(self, item): 
        if len(self.contents) == self.capacity:
            del self.contents[self.clock]
            self.contents.insert(self.clock, item)
            
            if self.clock == self.capacity - 1:
                self.clock = 0
            else:
                self.clock += 1
            
        else:
            self.contents.append(item)

    def get(self):
        contents = [item for item in self.contents if item is not None]
        return contents
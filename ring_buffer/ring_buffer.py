class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [] * capacity
        self.size = 0
        self.spot = 0

    def append(self, item):
        if self.size+1 <= self.capacity:
            self.queue.append(item)
            self.size += 1
        else:
            
            if self.spot <= self.capacity-1:
                i = self.spot
            else:
                self.spot = 0
                i = self.spot
            self.spot += 1    
            self.queue[i] = item
            

    def get(self):
        return self.queue
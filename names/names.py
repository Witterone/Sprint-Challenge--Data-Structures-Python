import time
# from queue import Queue 

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
# Q_1 = Queue()
# Q_2 = Queue()
# Q_3 = Queue()
# Replace the nested for loops below with your improvements
for name_1 in names_1:
    # Q_1.enqueue(name_1)
    if name_1 in names_2:
        duplicates.append(name_1)
# for name_2 in names_2:
#     Q_2.enqueue(name_2)

# for name in Q_1.storage:
#     if name in Q_2.storage:
#         Q_3.enqueue(name)
  
# duplicates= Q_3.storage
"""I tried very hard to impliment queues into the problem but for some reason 
it would not recognize the attributes I needed so I went with what I know."""
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

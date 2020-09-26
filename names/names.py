import time
start_time = time.time()


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                return self.left.insert(value)

        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                return self.right.insert(value)
    
    def contains(self, target):
        if target == self.value:
            return True
        else:
            if target < self.value:
                if self.left is None:
                    return False
                else:
                    return self.left.contains(target)
            if target > self.value:
                if self.right is None:
                    return False
                else:
                    return self.right.contains(target)



duplicates = []  # Return the list of duplicates in this data structure

f = open('names_1.txt', 'r')
# names_1 = f.read().split("\n")  # List containing 10000 names
firstLine = f.readline()
allname1 = BSTNode(firstLine)
for line in f:
    if line is firstLine:
        pass
    else:
        allname1.insert(line)
f.close()

f = open('names_2.txt', 'r')
# names_2 = f.read().split("\n")  # List containing 10000 names
for line in f:
    if allname1.contains(line):
        duplicates.append(line)
f.close()




# Replace the nested for loops below with your improvements


# f = open('names_1.txt', 'r')
# names_1 = f.read().split("\n")  # List containing 10000 names
# f.close()

# f = open('names_2.txt', 'r')
# names_2 = f.read().split("\n")  # List containing 10000 names
# f.close()

# duplicates = []  # Return the list of duplicates in this data structure

# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

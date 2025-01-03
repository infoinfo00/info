import os

path = "./labels/val"

n = 0

for file_name in os.listdir(path):
    with open(path + "/" + file_name, "r") as f:
        n += 0 if len(f.readline()) == 0 else 1
        
print(n)
import os

path = "./labels/val"
path2 = "C:/Users/Albert/Documents/A_Programacao/_GITIGNORE/cataovo-annotations/Ground-Truth-Evaluation/evaluation-2024-12-24_17-58-17/val/labels"

real_labels = set()
pred_labels = set(os.listdir(path2))

for file_name in os.listdir(path):
    with open(path + "/" + file_name, "r") as f:
        if len(f.readlines()) != 0:
            real_labels.add(file_name)
    
print(len(real_labels))
print(real_labels - pred_labels)
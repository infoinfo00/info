import os
import random
import shutil

imgs_src = "images/bundle/"
labels_src = "labels/bundle/"

img_names = sorted(os.listdir(imgs_src))
label_names = sorted(os.listdir(labels_src))
img_names = map(lambda x: imgs_src + x, img_names)
label_names = map(lambda x: labels_src + x, label_names)

data = list(zip(img_names, label_names))
# print(data[0], data[1], data[2])
random.shuffle(data)
# print(data[0], data[1], data[2])
# exit(0)

train_rate = 0.80
val_rate = 0.20

train_data = data[:int(train_rate * len(data))]
# val_data = data[int(train_rate * len(data)):int(train_rate * len(data))+int(val_rate*len(data)) + 1] # Verbose way
val_data = data[int(train_rate * len(data)):]

print(f"data_size: {len(data)}")
print(f"train_size: {len(train_data)} ({train_rate})")
print(f"val_size: {len(val_data)} ({val_rate})")

imgs_train_dir = "images/train/"
imgs_val_dir = "images/val/"
labels_train_dir = "labels/train/"
labels_val_dir = "labels/val/"

os.makedirs(imgs_train_dir, exist_ok=False)
os.makedirs(imgs_val_dir, exist_ok=False)
os.makedirs(labels_train_dir, exist_ok=False)
os.makedirs(labels_val_dir, exist_ok=False)

# print("images/val".rindex("/"))

def save_data(data, imgs_dir, labels_dir):
    for img, label in data:
        # print(img, label)
        shutil.copy2(img, imgs_dir + img[img.rindex("/")+1:])
        shutil.copy2(label, labels_dir + label[label.rindex("/")+1:])

save_data(train_data, imgs_train_dir, labels_train_dir)
save_data(val_data, imgs_val_dir, labels_val_dir)

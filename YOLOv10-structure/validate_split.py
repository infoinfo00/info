import os
import random
import shutil

imgs_src = "images/bundle/"
labels_src = "labels/bundle/"

imgs_train_dir = "images/train/"
imgs_val_dir = "images/val/"

labels_train_dir = "labels/train/"
labels_val_dir = "labels/val/"

imgs_src_size = len(os.listdir(imgs_src))
labels_src_size = len(os.listdir(labels_src))

assert (
    imgs_src_size == labels_src_size
), "ERROR: bundle imgs and bundle labels folder's size doesn't match."

### Train
imgs_train, lbs_train = sorted(os.listdir(imgs_train_dir)), sorted(os.listdir(labels_train_dir))
assert len(imgs_train) == len(lbs_train), f"FILE COUNT ERROR!!! imgs:{len(imgs_train)}, lbs:{len(lbs_train)}"

for img, label in zip(imgs_train, lbs_train):
    # Ignoring extensions.
    assert label[:-3] == img[:-3], f"FILE NAME ERROR!!! {img, label}"
    
### Val
imgs_val, lbs_val = sorted(os.listdir(imgs_val_dir)), sorted(os.listdir(labels_val_dir))
assert len(imgs_val) == len(lbs_val), f"FILE COUNT ERROR!!! imgs:{len(imgs_val)}, lbs:{len(lbs_val)}"

# print(lbs_train[:5])
# print(imgs_train[:5])
# print(imgs_val[:5])
# print(lbs_val[:5])

for img, label in zip(imgs_train, lbs_train):
    # Ignoring extensions.
    assert label[:-3] == img[:-3], f"FILE NAME ERROR!!! {img, label}"

### Total number of images and labels.
assert len(imgs_train) + len(imgs_val) == imgs_src_size, f"{len(imgs_train)} + {len(imgs_val)} != {imgs_src_size}"
assert len(lbs_train) + len(lbs_val) == labels_src_size, f"{len(lbs_train)} + {len(lbs_val)} != {labels_src_size}"

print("ALL OK.")

import cv2 as cv
import os

to_augment_dir = "to_augment"
augmented_dir = "augmented"

os.makedirs(augmented_dir, exist_ok=True)

labels_dir = "labels_original"
imgs_dir = "images"
augmented_dir = "augmented"

images_to_augment = []

for root, dirs, files in os.walk(labels_dir):
    for file in files:
        label_path = os.path.join(root, file)
        
        if os.path.getsize(label_path) > 0:
            img_path = os.path.join(".", imgs_dir, file[:-3] + "png")
            images_to_augment.append(img_path)
            
# print(images_to_augment)

# 0 -> vertical
# 1 -> horizontal
for img_path in images_to_augment:
    last_backslash = img_path.rfind("\\")
    img_name_without_extension = img_path[last_backslash+1:-4]
    print(img_name_without_extension)
    
    img = cv.imread(img_path)
    # Horizontal
    cv.imwrite(augmented_dir + "\\" + img_name_without_extension + "-aug-h.png", cv.flip(img, 1))
    # Vertical
    cv.imwrite(augmented_dir + "\\" + img_name_without_extension + "-aug-v.png", cv.flip(img, 0))
    # Horizontal and Vertical
    cv.imwrite(augmented_dir + "\\" + img_name_without_extension + "-aug-h-v.png", cv.flip(cv.flip(img, 1), 0))
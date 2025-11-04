import os
import shutil
from PIL import Image
from sklearn.model_selection import train_test_split


source_dir = "C:\\Users\\Theodore King\\Documents\\Images of American Sign Language (ASL) Alphabet Gestures\\Images of American Sign Language (ASL) Alphabet Gestures\\Root\\Root\\Type_01_(Raw_Gesture)"
output_base = "data"          # Output base folder
image_size = (300, 300)       # Desired size
test_ratio = 0.2              # 20% test data


train_dir = os.path.join(output_base, "train")
test_dir = os.path.join(output_base, "test")

os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

print(" Resizing .jpg images to 300x300 and split")

for class_name in os.listdir(source_dir):
    class_path = os.path.join(source_dir, class_name)
    if not os.path.isdir(class_path):
        continue

    # Get all .jpg files (case-insensitive)
    images = [
        os.path.join(class_path, f)
        for f in os.listdir(class_path)
        if f.lower().endswith(".jpg")
    ]

    if not images:
        print(f"⚠️ No .jpg images found in folder {class_name}")
        continue

    # Split 80/20
    train_imgs, test_imgs = train_test_split(images, test_size=test_ratio, random_state=42)

    # Create output folders
    os.makedirs(os.path.join(train_dir, class_name), exist_ok=True)
    os.makedirs(os.path.join(test_dir, class_name), exist_ok=True)

    # Resize and save
    for img_path in train_imgs:
        try:
            img = Image.open(img_path).convert("RGB")
            img = img.resize(image_size)
            save_path = os.path.join(train_dir, class_name, os.path.basename(img_path))
            img.save(save_path, "JPEG")
        except Exception as e:
            print(f"Error processing {img_path}: {e}")

    for img_path in test_imgs:
        try:
            img = Image.open(img_path).convert("RGB")
            img = img.resize(image_size)
            save_path = os.path.join(test_dir, class_name, os.path.basename(img_path))
            img.save(save_path, "JPEG")
        except Exception as e:
            print(f"Error processing {img_path}: {e}")

print("Done! Check your 'data/train' and 'data/test' folders.")

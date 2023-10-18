import os

# Base folder path
base_folder_path = 'C:/Users/Games/Downloads/sURVEY/validfirenew'
labels_folder_path = os.path.join(base_folder_path, 'labels')
images_folder_path = os.path.join(base_folder_path, 'images')

# Iterate through all files in the labels folder
for filename in os.listdir(labels_folder_path):
    # Check if it is a text file
    if filename.endswith(".txt"):
        label_file_path = os.path.join(labels_folder_path, filename)
        
        # Open the file for reading
        with open(label_file_path, 'r') as file:
            first_line = file.readline()
        
        # Check the first character of the first line
        if first_line and first_line[0] == '1':
            # Delete the text file
            os.remove(label_file_path)
            print(f"Deleted: {label_file_path}")

            # Delete the corresponding image file
            # Assuming images are in a different directory and have extensions like .jpg, .png, etc.
            # Adjust as per your use case
            image_extensions = [".jpg", ".jpeg", ".png"]
            for ext in image_extensions:
                image_file_path = os.path.join(images_folder_path, os.path.splitext(filename)[0] + ext)
                if os.path.exists(image_file_path):
                    os.remove(image_file_path)
                    print(f"Deleted: {image_file_path}")
                    break  # Exit the loop if an image file is found and deleted to avoid unnecessary checks
        else:
            print(f"Kept: {label_file_path}")

import os

# Folder path
base_folder_path = 'C:/Users/Games/Downloads/sURVEY/validfirenew'
labels_folder_path = os.path.join(base_folder_path, 'labels')

# Iterate through all files in the labels folder
for filename in os.listdir(labels_folder_path):
    # Check if it is a text file
    if filename.endswith(".txt"):
        label_file_path = os.path.join(labels_folder_path, filename)
        
        # Open the file for reading
        with open(label_file_path, 'r') as file:
            lines = file.readlines()
        
        # Perform the modifications
        modified_lines = []
        for line in lines:
            # Check the first character of the line
            if line and line[0] == '2':
                # Change the first character to '1' and append to the modified_lines list
                modified_lines.append('1' + line[1:])
            else:
                # Append the line unchanged
                modified_lines.append(line)

        # Open the file for writing and overwrite it with the modified lines
        with open(label_file_path, 'w') as file:
            file.writelines(modified_lines)

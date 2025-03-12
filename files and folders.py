import os

def list_files_and_folders(main_folder):
    all_items = []

    # os.walk generates the file names in a directory tree by walking either top-down or bottom-up
    for root, dirs, files in os.walk(main_folder):
        # Adding the path of each directory with a folder icon
        for directory in dirs:
            all_items.append("📁 " + os.path.join(root, directory))
        # Adding the path of each file with a file icon
        for file in files:
            all_items.append("📄 " + os.path.join(root, file))

    return all_items

# Example usage
main_directory = 'I:\\Packages for python\\scia'  # Replace this with the path to your main directory
items = list_files_and_folders(main_directory)

# Print each item on a new line for better readability
for item in items:
    print(item)
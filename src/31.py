def add_file(file_path):
    with open(file_path, 'a') as file:
        print("Added new file:", file_path)

add_file("/home/user/your_file.txt")

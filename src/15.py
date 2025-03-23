import os
import shutil

def remove_file_and_directory(directory_path):
    """
    Removes a directory and its contents.
    
    Args:
    directory_path (str): The path of the directory to be removed.
    
    Returns:
    None
    """
    try:
        shutil.rmtree(directory_path)
        print(f"Directory {directory_path} has been successfully removed.")
    except FileNotFoundError:
        print(f"The specified directory {directory_path} does not exist.")
    except Exception as e:
        print(f"An error occurred while removing the directory: {e}")

def clean_and_copy_file(src, dst):
    """
    Cleans a file and its metadata, then copies it to the destination.
    
    Args:
    src (str): The path of the source file.
    dst (str): The path of the destination file.
    
    Returns:
    None
    """
    remove_file_and_directory(src)
    shutil.copy2(src, dst)
    print(f"File {src} has been copied to {dst}.")

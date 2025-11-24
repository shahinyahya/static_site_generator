import os 
import shutil

def copy_static(src, dest):
    """_summary_
    Args:
        src (_type_): _description_
        dest (_type_): _description_
    Recursively copy all files from src to destination folder.
    """

    #! If destination directory exist, remove it completely
    if os.path.exists(dest):
        print(f"Deleting existing directory: {dest}")
        shutil.rmtree(dest)
    
    # Recreate root dest directory
    os.mkdir(dest)

    #? Start recrusive copy
    _copy_recursive(src, dest)

def _copy_recursive(src, dest):
    """
        Internal helper function that recursively copies content.
    """

    for item in os.listdir(src):
        print(item)
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        # If it's a directory, create directory and start copying.
        if os.path.isdir(src_path):
            print(f"Creating directory: {dest_path}")
            os.mkdir(dest_path)
            _copy_recursive(src_path, dest_path)
        
        # If it's a file → copy it
        elif os.path.isfile(src_path):
            print(f"Copying file: {src_path} → {dest_path}")
            shutil.copy(src_path, dest_path)

        # If its a file copy it
        else:
            print(f"Copying file: {src_path} -> {dest_path}")
            _copy_recursive(src_path, dest_path)

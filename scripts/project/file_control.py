import os
import shutil

def copy_file_with_category(file_path, dst_path):
    file_name = os.path.basename(file_path)
    os.makedirs(dst_path, exist_ok=True)

    dst_file = os.path.join(dst_path, file_name)
    shutil.copy(file_path, dst_file)






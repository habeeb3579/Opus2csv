import os
import opusFC

def list_OpusFiles(directory_path):
    all_files = []
    
    counter = 0
    for root, dirs, files in os.walk(directory_path):
        file_paths = [os.path.join(root, x) for x in files\
             if opusFC.isOpusFile(os.path.join(root, x))]
        all_files.extend(file_paths)
        
        if counter==0:
            print(f"Rootfolder: {root} | Number of Files: {len(file_paths)}")
            print("-" * (len(f"Rootfolder: {root} | Number of Files: {len(file_paths)}") + 5))
        else:
            # Log the subfolder and number of files with dashes covering the text above
            print(f"Subfolder: {root} | Number of Files: {len(file_paths)}")
            print("-" * (len(f"Subfolder: {root} | Number of Files: {len(file_paths)}") + 5))
        counter+=1
    return all_files
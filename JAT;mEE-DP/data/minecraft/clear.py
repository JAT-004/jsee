
import os
from tqdm import tqdm

entries = [
    ["advancement"],
    ["loot_table"],
    ["recipe"]
]

path = os.path.dirname(os.path.abspath(__file__))
counter = 0

for entry in entries:
    directory = path

    for element in entry:
        directory = os.path.join(directory, element)
    
    for root, directories, files in os.walk(directory):
        if len(files) > 0:
            print(f"TASK/ clear {directory}")

            with tqdm(total=len(files), unit='file', desc='TASK/ clear files') as progress:
                for file in files:
                    if file.endswith('.json'):
                        file_path = os.path.join(root, file)

                        try:
                            with open(file_path, 'w') as json_file:
                                pass
                            counter += 1
                        except Exception:
                            print(f"ERROR/ unable to clear {file_path}")
                    progress.update(1)

print(f"INFO/ cleared {counter} files")
input('EXIT/ finished')

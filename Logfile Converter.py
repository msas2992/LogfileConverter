import re
import csv
import os

# Function to process each file
def process_file(id, filename, file_path):
    with open(file_path, 'r') as txt_file:
        lines = txt_file.readlines()
    data = [id, filename]
    for index, line in enumerate(lines):
        if is_valid_line(line):
            line_temp = line.split()
            for line_temp in line_temp:
                data.append(line_temp)
        else:
            data.append(line)
    return data

def is_valid_line(line):
    # Define a regular expression pattern for four sets of numbers separated by spaces
    pattern = re.compile(r'^\d+\s+\d+\s+\d+\s+\d+\s*$')

    # Check if the line matches the pattern
    return bool(pattern.match(line))

print("")
print("########################################################################################################################")
print("")
_folder_path = input("Folder logfile path : ")
folder_path = _folder_path.replace('"', '')

_output_csv_path = input("Output filename (need .csv) : ")
output_csv_path = _output_csv_path.replace('"', '')

# List all file names in the folder
file_names = os.listdir(folder_path)

with open(output_csv_path, 'a', newline='') as csv_file: 
    csv_writer = csv.writer(csv_file)

    for file_name in file_names:
        id = file_name.split('_')[1]
        file_path = os.path.join(folder_path, file_name)
        data = process_file(id, file_name, file_path)
        
        csv_writer.writerow(data)

print("Data from multiple files has been successfully saved to " + output_csv_path)

_output_csv_path = input("Press any key to exit")

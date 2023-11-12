import os
import sys

def convert_bbox_to_min_max(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            input_file_path = os.path.join(input_folder, filename)
            with open(input_file_path, 'r') as file:
                lines = file.readlines()

            new_lines = []
            for line in lines:
                parts = line.split()
                class_id = int(parts[0])
                x_center, y_center, width, height = map(float, parts[1:])

                # Convert to min-max format
                x_min = x_center - (width / 2)
                y_min = y_center - (height / 2)
                x_max = x_center + (width / 2)
                y_max = y_center + (height / 2)

                new_line = f'{class_id} {x_min} {y_min} {x_max} {y_max}\n'
                new_lines.append(new_line)

            # Write the converted lines to a new file in the output folder
            output_file_path = os.path.join(output_folder, filename)
            with open(output_file_path, 'w') as new_file:
                new_file.writelines(new_lines)

            print(f'Converted {filename} and saved as {output_file_path}')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_folder> <output_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    convert_bbox_to_min_max(input_folder, output_folder)

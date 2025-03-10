def open_and_read_file(path):
  
  with open(path, 'r', encoding='utf-8') as file:
    return [line.strip() for line in file.readlines()]


def write_lines_to_file(file_path, lines):
  with open(file_path, 'w', encoding='utf-8') as file:
    for line in lines:
        file.write(line + '\n')

input_file = "C:/Users/josia/Downloads/canciones.txt"
output_file = "C:/Users/josia/Downloads/canciones_ordenadas.txt"

lines = open_and_read_file(input_file)

sorted_lines = sorted(lines)

write_lines_to_file(output_file, sorted_lines)

print(f"Las canciones se ordenaron y guardaron en' {output_file}'.")
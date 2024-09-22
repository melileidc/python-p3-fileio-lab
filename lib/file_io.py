def write_file(file_name, file_content):
    file_name = str(file_name)  # Convert file_name to string
    with open(file_name + ".txt", "w") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    file_name = str(file_name)  # Convert file_name to string
    with open(file_name + ".txt", "a") as file:
        if file.tell() > 0:  # Check if file is not empty
            file.write("\n")  # Add newline only if file is not empty
        file.write(append_content)  # Append content

def read_file(file_name):
    file_name = str(file_name)  # Convert file_name to string
    with open(file_name + ".txt", "r") as file:
        content = file.read()
    return content
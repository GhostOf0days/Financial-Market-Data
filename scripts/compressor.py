import zipfile
import os

''' Add to datasets folder before running script and remove original file after running script
    then use Git LFS to track it if still over file size limit. Please remove any temporary
    directories created. '''

def reduce_file_size(input_file, output_file):
    # Create a temporary directory
    temp_dir = 'temp'
    os.makedirs(temp_dir, exist_ok=True)

    # Split the input file into smaller chunks
    chunk_size = 100 * 1024 * 1024  # 100 MB
    chunk_names = []
    with open(input_file, 'rb') as file:
        chunk_counter = 0
        while True:
            data = file.read(chunk_size)
            if not data:
                break
            chunk_filename = os.path.join(temp_dir, f'chunk{chunk_counter}.dat')
            chunk_names.append(chunk_filename)
            with open(chunk_filename, 'wb') as chunk_file:
                chunk_file.write(data)
            chunk_counter += 1

    # Compress the chunks into a ZIP file
    with zipfile.ZipFile(output_file, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
        for chunk_filename in chunk_names:
            zipf.write(chunk_filename, os.path.basename(chunk_filename))

    # Clean up temporary files
    for chunk_filename in chunk_names:
        os.remove(chunk_filename)
    os.rmdir(temp_dir)

# Usage example
input_file_path = 'datasets/folder/file'
output_file_path = 'datasets/folder'

reduce_file_size(input_file_path, output_file_path)

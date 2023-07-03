import lz4.frame as lz4
import shutil
import os

def compress(input_file, output_file):
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(absolute_path, input_file)
    output_path = os.path.join(absolute_path, output_file)
    with open(input_path, 'rb') as f_in:
        with open(output_path, 'wb') as f_out:
            compressor = lz4.LZ4FramedCompressor(f_out)
            shutil.copyfileobj(f_in, compressor)
            compressor.close()
    compressed_file_size = os.path.getsize(output_path)
    max_file_size = 100 * 1024 * 1024  # 100 MB
    if compressed_file_size > max_file_size:
        print("Compressed file is still greater than 100 MB. Please remove the compressed file and use a different method.")
    else:
        print('File successfully compressed.')

def decompress(input_file, output_file):
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(absolute_path, input_file)
    output_path = os.path.join(absolute_path, output_file)
    with open(input_path, 'rb') as f_in:
        with open(output_path, 'wb') as f_out:
            decompressor = lz4.LZ4FramedDecompressor(f_in)
            shutil.copyfileobj(decompressor, f_out)
            decompressor.close()
    print('File successfully decompressed.')

# Example values:
# input_file = '../../datasets/$AAPL Option Chains Dataset/aapl_2016_2020.csv' or '../datasets/$AAPL Option Chains Dataset/aapl_2016_2020.csv.lz4'
# compressed_file = '../../datasets/$AAPL Option Chains Dataset/aapl_2016_2020.csv.lz4'
# decompressed_file = '../../datasets/$AAPL Option Chains Dataset/aapl_2016_2020_decompressed.csv'

input_file = '../../datasets/folder/file_name.file_extension'
compressed_file = '../../datasets/folder/file_name.file_extension.lz4'
decompressed_file = '../../datasets/folder/file_name_decompressed.file_extension'

# Comment whichever one you don't need (compression or decompression) by adding # in front of the function call

# Compress the file
compress(input_file, compressed_file)

# Decompress the file
decompress(compressed_file, decompressed_file)

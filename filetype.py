import os

# Define a dictionary mapping magic numbers to file types
MAGIC_NUMBERS = {
    b'\x89PNG\r\n\x1a\n': 'PNG image',
    b'\xFF\xD8\xFF': 'JPEG image',
    b'%PDF': 'PDF document',
    b'\x50\x4B\x03\x04': 'ZIP archive',
    b'\x25\x21\x50\x53': 'PostScript document',
    b'GIF87a': 'GIF image',
    b'GIF89a': 'GIF image',
    b'\x1F\x8B': 'GZIP archive',
    b'\x7F\x45\x4C\x46': 'ELF executable',
    b'\x42\x4D': 'BMP image',
    b'\x4D\x5A': 'Windows Executable',
    b'\x49\x49\x2A\x00': 'TIFF image (little-endian)',
    b'\x4D\x4D\x00\x2A': 'TIFF image (big-endian)',
    b'\xFF\xFE': 'UTF-16 encoded text',
    b'\xFE\xFF': 'UTF-16 encoded text',
    b'\xEF\xBB\xBF': 'UTF-8 encoded text',
    b'\x00\x00\x00\x14\x6C\x6F\x63\x61\x74\x69\x6F\x6E\x2D\x78\x38\x36': 'Docx document',
    b'\x52\x61\x72\x21\x1A\x07\x00\x00': 'RAR archive',
    b'\x1F\x9D': '7z archive',
}

# Function to identify file type based on magic numbers
def identify_file_type(file_path):
    """
    Identify the file type by checking its magic numbers.
    
    Args:
        file_path (str): The path to the file to be checked.
        
    Returns:
        str: The type of the file or 'Unknown file type' if not recognized.
    """
    try:
        with open(file_path, 'rb') as file:
            # Read the first 16 bytes of the file
            file_start = file.read(16)
            for magic, file_type in MAGIC_NUMBERS.items():
                if file_start.startswith(magic):
                    return file_type
            return 'Unknown file type'
    except IOError:
        return 'Could not read file'

# Main function to handle user input and process the file
if __name__ == "__main__":
    # Prompt the user to enter the path to the file
    file_path = input("Enter the path to the file you want to check: ").strip()
    
    if os.path.exists(file_path):
        file_type = identify_file_type(file_path)
        print(f'{file_path}: {file_type}')
    else:
        print(f'{file_path}: File does not exist')

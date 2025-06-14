from PIL import Image

# Ask the user for the path to the PNG file
file_path = input("Path to PNG file: ")

# Ask the user for the desired ICO sizes (comma-separated)
ico_sizes = input("Enter desired ICO sizes (e.g., 16,32,64): ").split(',')

# Convert the entered sizes to integers
ico_sizes = [int(size.strip()) for size in ico_sizes]

try:
    # Open the PNG image
    image = Image.open(file_path)

    # Ensure the image has an alpha channel (for transparency)
    if image.mode != "RGBA":
        image = image.convert("RGBA")

    # Save the image as an ICO file with the specified sizes
    output_path = "output_icon.ico"
    image.save(output_path, format="ICO", sizes=[(size, size) for size in ico_sizes])
    print(f"PNG successfully converted to ICO! Saved as '{output_path}'.")
except FileNotFoundError:
    print("Error: The specified PNG file was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

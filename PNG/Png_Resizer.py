from PIL import Image

try:
    # Open the image using the provided path
    file_path = input("Path to PNG: ")
    image = Image.open(file_path)
    x = input("Pixel Width: ")
    y = input("Pixel Hight: ")
    print(x, ", ", y)
    # Keep asking for a valid option until the user selects either 1 or 2
    while True:
        optionHW = input("Choose resizing mode (1: Confirm, 2: Retry): ")
        if optionHW == "1":
            break
        elif optionHW == "2":
            # Retype x and y 
            x = input("Pixel Width:")
            y = input("Pixel Hight: ")
            
        else:
            print("Invalid option. Please enter 1 to Confirm: ", x, ", ", y, " 2 to Retry")



    # Define the new size (e.g., 128x128 for an icon)
    intx = int(x)
    inty = int(y)
    new_size = (intx, inty)

    # Keep asking for a valid option until the user selects either 1 or 2
    while True:
        option = input("Choose resizing mode (1: Sharp, 2: Soft): ")
        if option == "1":
            # Resize image using nearest-neighbor interpolation for sharp edges
            resized_image = image.resize(new_size, Image.NEAREST)
            break
        elif option == "2":
            # Resize image with high-quality resampling for smooth edges
            resized_image = image.resize(new_size, Image.LANCZOS)
            break
        else:
            print("Invalid option. Please enter 1 for Sharp or 2 for Soft.")
        
    # Save the resized image
    resized_image.save("resized_image.png")
    print("Image resized successfully! Saved as 'resized_image.png'.")

except FileNotFoundError:
    print("Error: The file was not found. Please check the path and try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

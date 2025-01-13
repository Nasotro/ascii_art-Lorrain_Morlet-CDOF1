import cv2
import numpy as np

# Path to the input image
image_path = 'images/monalisa.jpg'
image = cv2.imread(image_path)

#Check that the image was successfully loaded
if image is None:
    print("Error: Image not found!")
else:
    print("Image loaded successfully!")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert the grayscale image to a NumPy array
intensity_matrix = np.array(gray_image)

# Define the ASCII characters to represent different intensity levels
densities = " .:-=+*#%@"

# Normalize the intensity matrix to the range of the densities length
intensity_matrix = intensity_matrix / (intensity_matrix.max() / (len(densities) -1))
# Convert the normalized intensity values to integers
intensity_matrix = intensity_matrix.astype(int)


# Open a file to write the ASCII art
with open('images/monalisa.txt', 'w', encoding='utf-8') as f:
    # Iterate over each intensity value in each row
    for row in intensity_matrix:
        for intensity in row:
            # Print the corresponding ASCII character to the console
            print(densities[intensity], end='')
            # Write the corresponding ASCII character to the file
            f.write(densities[intensity])
        
        f.write('\n')
        print()

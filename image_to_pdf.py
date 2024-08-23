import img2pdf
import os

# List of image files
image_files = ['image1.jpg', 'image2.jpg', 'image3.jpg']

# Check if all files exist
for file in image_files:
    if not os.path.exists(file):
        print(f"Error: {file} does not exist.")
        exit(1)

# Convert images to PDF
with open("output.pdf", "wb") as f:
    f.write(img2pdf.convert(image_files))

print("PDF created successfully.")

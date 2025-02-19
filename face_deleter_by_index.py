import os
import sys


def delete_images(base_folder):
    # Paths to the subfolders
    face_to_keep_folder = os.path.join(base_folder, 'face_to_keep')
    aligned_folder = os.path.join(base_folder, 'data_dst/aligned')
    
    # Get the first image file name from 'face_to_keep' folder
    first_image = os.listdir(face_to_keep_folder)[0]
    
    # Extract the number after the underscore in the file name
    keep_number = first_image.split('_')[1].split('.')[0]
    
    # Loop through the images in the 'aligned' folder and delete those that don't match the number
    for image in os.listdir(aligned_folder):
        # Get the number after the underscore in the image name
        image_number = image.split('_')[1].split('.')[0]
        
        # If the number does not match the one we want to keep, delete the image
        if image_number != keep_number:
            image_path = os.path.join(aligned_folder, image)
            os.remove(image_path)
            print(f"Deleted from aligned: {image}")
    
    # Finally, delete the image from 'face_to_keep' folder
    first_image_path = os.path.join(face_to_keep_folder, first_image)
    os.remove(first_image_path)
    print(f"Deleted from face_to_keep: {first_image}")


# Main entry point
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python face_deleter_by_index.py <base_folder>")
        sys.exit(1)

    # Read the base folder from the command-line argument
    base_folder = sys.argv[1]
    delete_images(base_folder)

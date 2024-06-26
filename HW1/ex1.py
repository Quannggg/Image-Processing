import cv2 
import matplotlib.pyplot as plt


# Load an image from file as function
def load_image(image_path):
    """
    Load an image from file, using OpenCV
    """
    pass 
    img = cv2.imread(image_path)
    return img

# Display an image as function
def display_image(image, title="Image"):
    """
    Display an image using matplotlib. Rembember to use plt.show() to display the image
    """
    pass
    plt.imshow(image)
    plt.title(title)
    plt.axis("off")
    plt.show()


# grayscale an image as function
def grayscale_image(image):
    """
    Convert an image to grayscale. Convert the original image to a grayscale image. In a grayscale image, the pixel value of the
    3 channels will be the same for a particular X, Y coordinate. The equation for the pixel value
    [1] is given by:
        p = 0.299R + 0.587G + 0.114B
    Where the R, G, B are the values for each of the corresponding channels. We will do this by
    creating an array called img_gray with the same shape as img
    """
    pass
    red_channel = image[:, :, 0]
    green_channel = image[:, :, 1]
    blue_channel = image[:, :, 2]
    img_gray = 0.299 * red_channel + 0.587 * green_channel + 0.114 * blue_channel
    return img_gray

# Save an image as function
def save_image(image, output_path):
    """
    Save an image to file using OpenCV
    """
    pass
    # Save an image to file using OpenCV
    cv2.imwrite(output_path, image)


# flip an image as function 
def flip_image(image):
    """
    Flip an image horizontally using OpenCV
    """
    pass
    # Flip an image horizontally using OpenCV
    img_flipped = cv2.flip(image, 1)
    return img_flipped



# rotate an image as function
def rotate_image(image, angle):
    """
    Rotate an image using OpenCV. The angle is in degrees
    """
    pass
    # Rotate an image using OpenCV. The angle is in degrees
    (h, w) = image.shape[:2]
    rotate_matrix = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1.0)
    img_rotated = cv2.warpAffine(image, rotate_matrix, (w, h))
    return img_rotated


if __name__ == "__main__":
    # Load an image from file
    img = load_image("images/uet.png")

    # Display the image
    display_image(img, "Original Image")

    # Convert the image to grayscale
    img_gray = grayscale_image(img)

    # Display the grayscale image
    display_image(img_gray, "Grayscale Image")

    # Save the grayscale image
    save_image(img_gray, "images/lena_gray.jpg")

    # Flip the grayscale image
    img_gray_flipped = flip_image(img_gray)

    # Display the flipped grayscale image
    display_image(img_gray_flipped, "Flipped Grayscale Image")
    
    #save the flipped grayscale image
    save_image(img_gray_flipped, "images/lena_gray_flipped.jpg")

    # Rotate the grayscale image
    img_gray_rotated = rotate_image(img_gray, 45)

    # Display the rotated grayscale image
    display_image(img_gray_rotated, "Rotated Grayscale Image")

    # Save the rotated grayscale image
    save_image(img_gray_rotated, "images/lena_gray_rotated.jpg")

    # Show the images
    plt.show() 

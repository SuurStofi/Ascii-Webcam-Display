import cv2
import time
from colorama import init, Fore

# Initialize colorama
init()

# ASCII characters used to represent different intensity levels
ASCII_CHARS = '@%#*+=-:.'

# Function to convert a grayscale pixel value to an ASCII character
def pixel_to_ascii(pixel_value):
    # Determine the ASCII character corresponding to the pixel intensity
    return ASCII_CHARS[int(pixel_value / 256 * len(ASCII_CHARS))]

# Function to convert a frame to ASCII art
def frame_to_ascii(frame):
    # Resize frame to make it smaller
    resized_frame = cv2.resize(frame, (80, 25))

    # Convert resized frame to grayscale
    gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

    ascii_art = ""
    for row in gray_frame:
        for pixel in row:
            # Append ASCII character representing the pixel to the ASCII art
            ascii_art += pixel_to_ascii(pixel)
        ascii_art += '\n'  # Add newline character at the end of each row

    return ascii_art

# Main function
def main():
    # Open webcam capture
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert frame to ASCII art
        ascii_art = frame_to_ascii(frame)

        # Print ASCII art with colorama
        print(Fore.WHITE + ascii_art, end='\r')

        # Add delay for smooth animation (adjust the value as needed)
        time.sleep(0.1)

        # Check for 'q' keypress to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

import cv2
import time
from colorama import init, Fore


init()


ASCII_CHARS = '@%#*+=-:.'


def pixel_to_ascii(pixel_value):
    return ASCII_CHARS[int(pixel_value / 256 * len(ASCII_CHARS))]


def frame_to_ascii(frame):

    resized_frame = cv2.resize(frame, (80, 25))


    gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

    ascii_art = ""
    for row in gray_frame:
        for pixel in row:
      
            ascii_art += pixel_to_ascii(pixel)
        ascii_art += '\n'  

    return ascii_art


def main():
 
    cap = cv2.VideoCapture(0)

    while True:
      
        ret, frame = cap.read()

     
        ascii_art = frame_to_ascii(frame)

      
        print(Fore.WHITE + ascii_art, end='\r')

      
        time.sleep(0.1)

      
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

  
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

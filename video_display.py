import sys

import cv2


def display_webcam():
    """
    Capture and display video from USB webcam.
    Press 'q' to quit.
    """
    # Initialize video capture from the first webcam device (usually 0)
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam")
        sys.exit(1)

    try:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Check if frame is valid
            if not ret:
                print("Error: Can't receive frame from webcam")
                break

            # Display the frame
            cv2.imshow("USB Webcam", frame)

            # Break the loop when 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        # Release resources
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    display_webcam()

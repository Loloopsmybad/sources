import cv2
import numpy as np

# List to store the positions of detected pink balls
trail_positions = []

def detect_pink_balls(frame):
    # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range for the color pink in HSV
    lower_pink = np.array([140, 50, 50])  # Lower bound of pink
    upper_pink = np.array([180, 255, 255])  # Upper bound of pink

    # Create a mask for pink color
    mask = cv2.inRange(hsv, lower_pink, upper_pink)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes around detected pink balls
    for contour in contours:
        if cv2.contourArea(contour) > 100:  # Filter out small contours
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw rectangle
            
            # Store the center of the detected pink ball
            center = (x + w // 2, y + h // 2)
            trail_positions.append(center)

    return frame

def draw_trail(frame):
    # Draw the trail for the last few frames
    for pos in trail_positions:
        cv2.circle(frame, pos, 5, (0, 0, 255), -1)  # Draw a filled circle for the trail

    # Limit the trail length to the last 30 positions
    if len(trail_positions) > 10:
        trail_positions.pop(0)

def main():
    # Open a video capture object (0 for the default camera)
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect pink balls and draw bounding boxes
        output_frame = detect_pink_balls(frame)

        # Draw the trail behind the detected pink balls
        draw_trail(output_frame)

        # Display the resulting frame
        cv2.imshow('Pink Ball Detection with Trail', output_frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()
 
if __name__ == "__main__":
    main()
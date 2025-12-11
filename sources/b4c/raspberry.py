import pyfirmata
import cv2
import numpy as np
import torch
from torchvision.transforms import Compose, Resize, ToTensor, Normalize
from PIL import Image

# Initialize Arduino board
comport = 'COM5'
board = pyfirmata.Arduino(comport)

# Define motor control pins
in1 = board.get_pin('d:4:o')  # MOTOR 4
in2 = board.get_pin('d:5:o')  # MOTOR 4
in3 = board.get_pin('d:6:o')  # MOTOR 3
in4 = board.get_pin('d:7:o')  # MOTOR 3
in5 = board.get_pin('d:8:o')  # MOTOR 2
in6 = board.get_pin('d:9:o')  # MOTOR 2
in7 = board.get_pin('d:10:o')  # MOTOR 1
in8 = board.get_pin('d:11:o')  # MOTOR 1

# Load the MiDaS model
model_type = "DPT_Large"
midas = torch.hub.load("intel-isl/MiDaS", model_type)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
midas.to(device)
midas.eval()

# Define transformation for input image
transform = Compose([
    Resize((384, 384), interpolation= Image.BILINEAR),
    ToTensor(),
    Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]),
])

# Initialize video capture
cap = cv2.VideoCapture(0)

# Define color ranges for red and green blocks in HSV
lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([180, 255, 255])
lower_green = np.array([40, 100, 100])
upper_green = np.array([80, 255, 255])

def control(inp):
    if inp == 'w':  # forward
        in1.write(0)
        in2.write(1)
        in3.write(0)
        in4.write(1)
        in5.write(0)
        in6.write(1)
        in7.write(0)
        in8.write(1)
    elif inp == 's':  # backward
        in1.write(1)
        in2.write(0)
        in3.write(1)
        in4.write(0)
        in5.write(1)
        in6.write(0)
        in7.write(1)
        in8.write(0)
    elif inp == 'd':  # left
        in1.write(0)
        in2.write(0)
        in3.write(0)
        in4.write(1)
        in5.write(0)
        in6.write(1)
        in7.write(0)
        in8.write(0)
    elif inp == 'a':  # right
        in1.write(0)
        in2.write(1)
        in3.write(0)
        in4.write(0)
        in5.write(0)
        in6.write(0)
        in7.write(0)
        in8.write(1)
    elif inp == 'e':  # stop
        in1.write(0)
        in2.write(0)
        in3.write(0)
        in4.write(0)
        in5.write(0)
        in6.write(0)
        in7.write(0)
        in8.write(0)

def preprocess_frame(frame):
    pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    input_tensor = transform(pil_image).unsqueeze(0)
    return input_tensor.to(device)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess the frame for depth estimation
    input_tensor = preprocess_frame(frame)

    # Predict depth
    with torch.no_grad():
        depth_output = midas(input_tensor)
        depth_map = depth_output.squeeze().cpu().numpy()

    # Normalize depth map
    depth_map = (depth_map - depth_map.min()) / (depth_map.max() - depth_map.min()) * 255
    depth_map = depth_map.astype(np.uint8)

    # Convert depth map to color
    depth_colored = cv2.applyColorMap(depth_map, cv2.COLORMAP_JET)

    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create masks for red and green colors
    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)

    # Find contours
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Variables to control the robot's movement
    closest_red_distance = float('inf')
    closest_green_distance = float('inf')
    action = 'e'  # Default action is stop

    # Loop over red contours
    for contour in contours_red:
        if cv2.contourArea(contour) < 500:  # Filter small contours
            continue

        (x, y, w, h) = cv2.boundingRect(contour)
        x_depth = int(x * (384 / frame.shape[1]))
        y_depth = int(y * (384 / frame.shape[0]))

        if 0 <= y_depth + h // 2 < depth_map.shape[0] and 0 <= x_depth + w // 2 < depth_map.shape[1]:
            block_depth = depth_map[y_depth + h // 2, x_depth + w // 2]
            distance = block_depth if block_depth > 0 else 0
            
            # Draw rectangle around detected red block
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, f"Red: {distance:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            # Update closest red distance
            if distance < closest_red_distance:
                closest_red_distance = distance
                action = 'w'  # Move forward towards the red block

    # Loop over green contours
    for contour in contours_green:
        if cv2.contourArea(contour) < 500:
            continue

        (x, y, w, h) = cv2.boundingRect(contour)
        x_depth = int(x * (384 / frame.shape[1]))
        y_depth = int(y * (384 / frame.shape[0]))

        if 0 <= y_depth + h // 2 < depth_map.shape[0] and 0 <= x_depth + w // 2 < depth_map.shape[1]:
            block_depth = depth_map[y_depth + h // 2, x_depth + w // 2]
            distance = block_depth if block_depth > 0 else 0
            
            # Draw rectangle around detected green block
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"Green: {distance:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Update closest green distance
            if distance < closest_green_distance:
                closest_green_distance = distance
                action = 's'  # Move backward towards the green block

    # Control the robot based on detected blocks
    control(action)

    # Show the depth map and the original frame
    cv2.imshow("Depth Map", depth_colored)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()



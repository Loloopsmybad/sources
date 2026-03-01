import mediapipe as mp
import cv2
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pose_detection = mp_pose.Pose()
img=cv2.imread('kkboi.jpg')
#image = mp.Image.from_bytes(
    #image_format=mp.ImageFormat.RGB,
    #data=image_data
    #)

pose_results = pose_detection.process(img)

if pose_results.pose_landmarks:
    for landmark1 in pose_results.pose_landmarks.landmark:
        print(f"'{landmark1.visibility}' x: {landmark1.x}, y: {landmark1.y}")
        
    mp_drawing.draw_landmarks(img, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

cv2.imshow('Pose Detection', img)
cv2.waitKey(0)
import cv2
import pygame
import numpy as np
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Glowing Blue Sphere")

# Load OpenCV's face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Function to draw the glowing sphere
def draw_glowing_sphere(surface, position, radius, intensity):
    """
    Draws a glowing blue sphere with fading effects.
    - position: Tuple (x, y) for center of the sphere.
    - radius: Radius of the sphere.
    - intensity: 0 (invisible) to 1 (fully visible) for alpha transparency.
    """
    glow_surface = pygame.Surface((radius * 4, radius * 4), pygame.SRCALPHA)
    for i in range(20):  # Create glow layers
        alpha = max(0, int(intensity * (255 - i * 12)))  # Fading outer layers
        color = (0, 100, 255, alpha)  # Blue glow color with transparency
        pygame.draw.circle(glow_surface, color, (radius * 2, radius * 2), radius - i * 3)
    surface.blit(glow_surface, (position[0] - radius * 2, position[1] - radius * 2))

# Main function
def main():
    # Video capture
    cap = cv2.VideoCapture(0)

    # Fade in/out parameters
    alpha = 0  # Current sphere visibility (0 = invisible, 1 = fully visible)
    fade_speed = 0.05  # Speed of fading in/out
    face_detected = False

    clock = pygame.time.Clock()

    running = True
    while running:
        # Handle Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Read video frame
        ret, frame = cap.read()
        if not ret:
            continue

        # Convert frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

        # Check for face detection
        face_detected = len(faces) > 0

        # Update alpha based on face detection
        if face_detected:
            alpha = min(1, alpha + fade_speed)  # Fade in
        else:
            alpha = max(0, alpha - fade_speed)  # Fade out

        # Clear screen
        screen.fill((0, 0, 0))  # Black background

        # Draw glowing sphere if alpha > 0
        if alpha > 0:
            sphere_position = (WIDTH // 2, HEIGHT // 2)
            sphere_radius = 150
            draw_glowing_sphere(screen, sphere_position, sphere_radius, alpha)

        # Update Pygame display
        pygame.display.flip()

        # Limit frame rate
        clock.tick(30)

    # Release video capture and quit Pygame
    cap.release()
    pygame.quit()

if __name__ == "__main__":
    main()

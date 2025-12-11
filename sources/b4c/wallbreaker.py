import pygame
import sys
import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller

cap = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.7, maxHands=1)
keyboard = Controller()

# Pygame Initialization
pygame.init()

# Screen size
screen = pygame.display.set_mode((800, 600))

# Title of the window
pygame.display.set_caption("Breakout")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle properties
paddle_width = 300
paddle_height =20
paddle_x = 350
paddle_y = 530
paddle_speed = 15

# Ball properties
ball_diameter = 15
ball_x = 375
ball_y = 510
ball_speed_x = 4
ball_speed_y = -4

# Brick properties
brick_width = 60
brick_height = 30
brick_space = 5
bricks = []
for i in range(2):
    for j in range(10):
        bricks.append(pygame.Rect(j * (brick_width + brick_space) + 50, i * (brick_height + brick_space) + 50, brick_width, brick_height))

# Game loop
while True:
    
    _, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        finger = detector.fingersUp(hands[0])
        if finger == [0, 0, 0, 0, 0]  :
          #  keyboard.press(Key.left)
           # keyboard.release(Key.right)
            if  paddle_x > 0:
                paddle_x -= paddle_speed

        elif finger == [1, 1, 1, 1, 1] :
           # keyboard.press(Key.right)
            #keyboard.release(Key.left)
            if paddle_x < 700:
                 paddle_x += paddle_speed
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get a list of all keys currently being pressed down
    keys = pygame.key.get_pressed()


    # Move the paddle
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < 700:
        paddle_x += paddle_speed

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Collision with walls
    if ball_x < 0 or ball_x > 780:
        ball_speed_x = -ball_speed_x
    if ball_y < 0 or ball_y>600:
        ball_speed_y = -ball_speed_y

    # Collision with paddle
    if ball_y > 520 and ball_x > paddle_x and ball_x < paddle_x + paddle_width:
        ball_speed_y = -ball_speed_y

    # Collision with bricks
    for brick in bricks:
        if ball_x > brick.x and ball_x < brick.x + brick_width and ball_y > brick.y and ball_y < brick.y + brick_height:
            bricks.remove(brick)
            ball_speed_y = -ball_speed_y

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, ball_diameter, ball_diameter))
    for brick in bricks:
        pygame.draw.rect(screen, WHITE, brick)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(1000 // 60)
    
    
    cv2.imshow("Wall Breaker Game", img)
    if cv2.waitKey(1) == ord("q"):
        break
    
    
    
    
    
    
    
    
    
    
    


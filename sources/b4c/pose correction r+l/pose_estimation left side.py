import cv2
import mediapipe as mp
import pygame 
pygame.init()




mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils # For drawing keypoints

# Initialize the camera
cap = cv2.VideoCapture(2)
 

ldm=[0,11,12,13,14,15,16]


while True:
    # Capture a frame from the camera
    ret, frame = cap.read()
  
    # Preprocess the frame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame.flags.writeable = False
    results = pose.process(frame)

    # Draw the pose landmarks on the frame
    frame.flags.writeable = True
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    
    lmList=[]
    
    if results.pose_landmarks:
        for lm in results.pose_landmarks.landmark:
            x, y = int(lm.x * frame.shape[1]), int(lm.y * frame.shape[0])
            #print(landmark.x)
            #print(landmark.y)
            #print(f"Landmark {lm} at ({x}, {y})")
            lmList.append([lm,x,y])
            
            
            
        mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

   # num_o_landmark=[]

    if len(lmList)!=0:
            n_x=lmList[ldm[0]][1]
            n_y=lmList[ldm[0]][2]
            
            sh_x=lmList[ldm[2]][1]
            sh_y=lmList[ldm[2]][2]
            
            lsh_x=lmList[ldm[2]][1]
            lsh_y=lmList[ldm[2]][2]
            

            rb_x=lmList[ldm[6]][1]
            rb_y=lmList[ldm[6]][2]

            lbk_x=lmList[ldm[5]][1]
            lbk_y=lmList[ldm[5]][2]

            rlbow_x=lmList[ldm[4]][1]
            rlbow_y=lmList[ldm[4]][2]
            
            
            
            
            #diff_elbow=abs(rlbow_y-rb_y)
            
            #print(diff_elbow)
            
            #print(lmList[16][0])
            
            
            if n_x - sh_x  and sh_x-rb_x != 0 :    
                    
                    slope= abs((n_y - lsh_y)/(n_x-lsh_x))
                    #slope_back =abs((sh_y-lb_y)/(sh_x-lb_x))
                    #print(slope_back)
                    #print (slope)
                    dif_lb_sh=abs(lsh_x - lbk_x)
                    print(dif_lb_sh)
                    
                    if slope > 0.8 and slope < 1.5 and dif_lb_sh < 160  :
                        #cv2.rectangle(frame, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                        cv2.putText(frame, "correct posture", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,2, (255, 0, 0), 5)
                    
                    else:
                        #cv2.rectangle(frame, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                        cv2.putText(frame, "wrong posture", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,2, (0, 0, 255), 5)
                    
            else:
                    #cv2.rectangle(frame, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                    cv2.putText(frame, "wrong posture", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,2, (0, 0, 255), 5)    
                
    #                total=num_o_landmark.count(1)
     #               
      #              ##now to write 
       #             if total==0:
        #                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
         #               cv2.putText(image, "0", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,2, (255, 0, 0), 5)
          #          elif total==1:
           #             cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
            #            cv2.putText(image, " 1", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,2, (255, 0, 0), 5)
             #       elif total==2:
              #          cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
               #         cv2.putText(image, " 2", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,2, (255, 0, 0), 5)
                #    elif total==3:
                 #       cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                  #      cv2.putText(image, " 3", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,2, (255, 0, 0), 5)
                   # elif total==4:
                    #    cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                     #   cv2.putText(image, " 4", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,2, (255, 0, 0), 5)
                   # elif total==5:
                    #    cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)        
                     #   cv2.putText(image, " 5", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,2, (255, 0, 0), 5)




    # Display the frame
    cv2.imshow('Pose Detection', frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release the camera and destroy all windows
cap.release()
cv2.destroyAllWindows()
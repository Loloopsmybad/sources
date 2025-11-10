import math

from random import choice

lol_1 = input("\n DO you want to find are a of a 2D figure or 3D figure --> ")

if lol_1 == '2D':
    
    lol_shape_gg =input("\n what do you want to find area or peremeter ? -->")

    if lol_shape_gg == 'AREA':
            
            lol_shape = input("\n of which shape do you want to find area of ? -->")
            
            if lol_shape == 'RECTANGLE' :

                RC_LENGTH = int(input("\n WHAT IS THE LENGTH --> "))

                RC_BREADTH = int(input("\n WHAT IS THE BREADTH --> "))

                AREA_RC_AQ = RC_LENGTH*RC_BREADTH

                print("AREA OF RECTANGLE-->",AREA_RC_AQ)

            elif lol_shape == 'SQUARE' :

                SQ_SIDE = int(input("\nSIDE OF THE SQUARE --> "))

                AREA_SQ_AQ = SQ_SIDE**2 

                print("\nAREA OF SQUARE --> ",AREA_SQ_AQ)

            elif lol_shape == 'TRIANGLE':

                CHOICE_AREA =input("\n By which way do you want to find the are 1: Heron's formula or 2:The regular base height formula ?", '\n' , "type number 1 or 2 ")

                if CHOICE_AREA == '1':

                    SIDE_TR_1 = int(input("\nSIDE 1 --> "))

                    SIDE_TR_2 = int(input(" \nSIDE 2 --> "))

                    SIDE_TR_3 = int(input("\nSIDE 3 --> "))

                    AREA_TR_SP = (SIDE_TR_1+SIDE_TR_2+SIDE_TR_3)/2

                    AREA_TR_SP_1 = AREA_TR_SP*(AREA_TR_SP - SIDE_TR_1)*(AREA_TR_SP - SIDE_TR_2)*(AREA_TR_SP - SIDE_TR_3)

                    AREA_TR_AQ = math.sqrt(AREA_TR_SP_1)
                    
                    print("\nAREA OF TRIANGLE USNING HERON'S FORMULA --> ", AREA_TR_AQ)

                elif CHOICE_AREA == '2' :

                    SIDE_BASE = int(input("\nwhat is the BASE --> "))

                    SIDE_HEIGHT = int(input("\nWhat is the --> "))

                    AREA_TR_RG = 1/2*SIDE_BASE*SIDE_HEIGHT

                    print("\nAREA OF TRIANGLE --> ",AREA_TR_RG)
            
            elif lol_shape == 'CIRCLE':

                AREA_RADIUS = int(input("\nwhat is the radius --> "))

                AREA_CR_AQ = 22/7*(AREA_RADIUS**2)

                print("\nArea of cicle --> ", AREA_CR_AQ)
            
            elif lol_shape == 'RHOMBUS' :
                
                choice = input(" \n By which way do you want to find the area of the rhombus 1:IF YOU HAVE DIAGONALS OR 2: IF YOU HAVE HEIGHT AND BASE OF RHOMBUS -->")
              
                if choice == '1':

                    AREA_D1 = int(input("\nwhat is your lenght of the diagonal 1 --> "))

                    AREA_D2 = int(input("\nwhat is  the lenth of the diagonal 2--> "))

                    AREA_RH_AQ = 1/2*AREA_D1*AREA_D2

                    print("\nAREA of rhombus is --> ",AREA_RH_AQ)
                
                elif choice == '2':

                    AREA_RH_BASE = int(input("\nwhat is the lenght of the base? --> "))

                    AREA_RH_HEIGHT = int(input("\nwhat is the HEIGHT? --> "))

                    AREA_RH_AQ = AREA_RH_BASE* AREA_RH_HEIGHT

                    print("\nAREA of rhombus is -->",AREA_RH_AQ)

            elif lol_shape == 'TRAPEZIUM':

                    AREA_TRP_1 = int(input("\nwhat is the length of first parallel side --> "))

                    AREA_TRP_2 = int(input("\nwhat is the length of the second prallel side --> "))

                    AREA_HG = int(input("\nwhat is the measure of the HEIGHT --> "))

                    AREA_TRP_AQ = 1/2*(AREA_TRP_1+AREA_TRP_2)*AREA_HG

                    print("\nAREA of trapezium is -->" , AREA_TRP_AQ )

    elif lol_shape_gg == 'PERIMETER':

            lol_shape = input("\nof which shape do you want to find perimeter of?  -->")

            if lol_shape == 'SQUARE' :

                    PERI_SQ = int(input("\nwhat is the length of the side? -->"))

                    PERI_SQ_AQ = 4*PERI_SQ

                    print("\nthe perimeter of square is -->", PERI_SQ_AQ)

            elif lol_shape == 'RECTANGLE' :

                    PERI_RC_1 = int(input("\nWhat is the length? --> "))

                    PERI_RC_2 = int(input("\nwhat is the breadth? --> "))

                    PERI_RC_AQ = 2*(PERI_RC_1+PERI_RC_2)

                    print("\nThe perimeter is -->", PERI_RC_AQ)


            elif lol_shape == 'TRIANGLE' :

                    PERI_TR_1 = int(input("\nwhat is lenght of first side? --> "))

                    PERI_TR_2 = int(input("\nwhat is the length of second side? --> "))

                    PERI_TR_3 = int(input("\nwhat is the length of third side? --> "))

                    PERI_TR_AQ = PERI_TR_1+PERI_TR_2+PERI_TR_3

                    print("\nthe perimeter is --> ",PERI_TR_AQ)

            elif lol_shape == 'CIRCLE':

                    PERI_CR = int(input("\nWhat is the radius? --> "))

                    PERI_CR_AQ = 2*22/7*PERI_CR

                    print("\nThe perimeter is --> ",PERI_CR_AQ)

            elif lol_shape == 'RHOMBUS':

                    PERI_RH_SIDE = int(input("\nwhat is the length of the side? --> "))

                    PERI_RH_AQ = 4*PERI_RH_SIDE

                    print("\nThe perimeter is --> ",PERI_RH_AQ)

            elif lol_shape == 'TRAPEZIUM':

                    PERI_TP_1 = int(input("\nwhat is the length of first side? --> "))

                    PERI_TP_2 = int(input("\nwhat is the length of second side? --> "))

                    PERI_TP_3 = int(input("\nwhat is the length of third side? --> "))

                    PERI_TP_4 = int(input("\nwhat is the lenght of fourth side? --> "))

                    PERI_TP_AQ = PERI_TP_1 + PERI_TP_2 + PERI_TP_3 + PERI_TP_4

                    print("\nThe Perimeter if --> ",PERI_TP_AQ)

elif lol_1 == '3D':

    ANSHUK_THE_BOI = input("\nName of shape of which you want SURFACE AREA OR VOLUME of ? --> ")
 
    if ANSHUK_THE_BOI == 'CUBE':

        CUBE_CHOICE = input("\nwhat do you want TSA or CSA or VOLUME ? --> ")

        if CUBE_CHOICE == 'TSA':
            
            SIDE_CUBE = int(input("\nWhat is the measure of side of cube? --> "))

            CUBE_AQ = 6*SIDE_CUBE

            print("\nThe TSA of CUBE is -->",CUBE_AQ)

        elif CUBE_CHOICE == 'CSA' :

            SIDE_CUBE = int(input("\nWhat is the measure of side of cube? --> "))

            CUBE_AQ = 4*SIDE_CUBE

            print("\nThe CSA of CUBE is -->",CUBE_AQ)
        
        elif CUBE_CHOICE == 'VOLUME':
            
            SIDE_CUBE = int(input("\nwhat is the measure of the side of cube? -->"))

            CUBE_AQ = SIDE_CUBE**3

            print("\nThe VOLUME of cube is --> " , CUBE_AQ)
            
            
    elif ANSHUK_THE_BOI == 'CUBOID':

            CUBOID_CHOICE = input("\nwhat do you want TSA or CSA or VOLUME ? --> ")
             
            if CUBOID_CHOICE == 'TSA' :
                CUBOID_S_1 = int(input("\nwhat is the LENGTH? --> "))

                CUBOID_S_2 = int(input("\nWhat is the BREADTH? --> "))

                CUBOID_S_3 = int(input("\nWhat is the HEIGHT? --> "))

                CUBOID_TSA = 2*(CUBOID_S_1*CUBOID_S_2+ CUBOID_S_2*CUBOID_S_3 + CUBOID_S_1*CUBOID_S_3)

                print("\nThe TSA of CUBOID is -->",CUBOID_TSA)

            elif CUBOID_CHOICE == 'CSA':
                
                CUBOID_S_1 = int(input("\nWhat is the LENGTH? -->"))

                CUBOID_S_2 = int(input("\nWhat is the BREADTH? -->"))

                CUBOID_S_3 = int(input("\nWhat is the HEIGHT? -->"))

                CUBOID_CSA = 2*(CUBOID_S_1*CUBOID_S_3+CUBOID_S_2*CUBOID_S_3)

                print("\nThe CSA of cuboid is -->", CUBOID_CSA)

            
            elif CUBOID_CHOICE == 'VOLUME':

                CUBOID_S_1 = int(input("\nWhat is the LENGTH? -->"))

                CUBOID_S_2 = int(input("\nWhat is BREADTH? -->"))
                
                CUBOID_S_3 = int(input("\nWhat is the HEIGHT -->"))

                CUBOID_VOLUME = CUBOID_S_1*CUBOID_S_2*CUBOID_S_3

                print("\nThe volume of CUBOID is -->", CUBOID_VOLUME)
        
    elif ANSHUK_THE_BOI == 'CONE':

        CONE_CHOICE = input("\nWaht do you want to find TSA or CSA or VOLUME of CONE? ")

        if CONE_CHOICE == 'CSA':

                CONE_SH = int(input("\nwhat is the slant length? --> "))

                CONE_R = int(input("\nWhat is the radius? --> "))

                CONE_CSA = 22/7*CONE_R*CONE_SH

                print("\nThe CSA is -->",CONE_CSA)

        elif CONE_CHOICE == 'TSA':

                
                CONE_SH = int(input("\nwhat is the slant length? --> "))

                CONE_R = int(input("\nWhat is the radius? --> "))

                CONE_TSA = (22/7*CONE_R*CONE_SH) + (22/7*CONE_R**2)

                print("\nThe TSA is -->",CONE_TSA)

        elif CONE_CHOICE == 'VOLUME':

                CONE_SH = int(input("\nwhat is the slant length? --> "))

                CONE_R = int(input("\nWhat is the radius? --> "))

                CONE_HEIGHT = int(input("\nWant is the HEIGHT? -->"))

                CONE_VOLUME = 1/3*22/7*(CONE_R**2)*CONE_HEIGHT

                print("\nThe volume is -->", CONE_VOLUME)

    elif ANSHUK_THE_BOI == 'CYLINDER': 
                
                CYL_CHOICE = input("\nwhatdo you want to find TSA or CSA or VOLUME of cylinder?")

                if CYL_CHOICE == 'TSA':
                    
                    CYL_H = int(input("\nWhat is the Lenght? -->"))

                    CYL_R = int(input("\nWhat is the Radius? -->"))

                    CYL_TSA = (2*22/7*CYL_R*CYL_H) + (2*22/7*CYL_R**2)

                    print("\nThe TSA is --> ", CYL_TSA)

                elif CYL_CHOICE =='CSA':

                    CYL_H = int(input("\nWhat is the Lenght? -->"))

                    CYL_R = int(input("\nWhat is the Radius? -->"))

                    CYL_CSA = (2*22/7*CYL_R*CYL_H) 

                    print("\nThe CSA is --> ", CYL_CSA)

                elif CYL_CHOICE == 'VOLUME':

                    CYL_H = int(input("\nWhat is the Lenght? -->"))

                    CYL_R = int(input("\nWhat is the Radius? -->"))

                    CYL_VOLUME = 22/7*(CYL_R**2)*CYL_H

                    print("\nThe VOLUME is -->",CYL_VOLUME)
    
    elif ANSHUK_THE_BOI == 'SHPERE':

            SHP_CHOICE = input("\nwhat do you want to find TSA or CSA or VOLUME of SPHERE ? -->")
            
            if SHP_CHOICE == 'TSA':

                    SPH_R = int(input("\nWhat is the RADIUS? -->"))

                    SPH_TSA = 4*22/7*SPH_R**2

                    print("\nThe TSA of sphere is --> ",SPH_TSA)
            
            elif SHP_CHOICE == 'CSA':

                    SPH_R = int(input("\nWhat is the RADIUS? -->"))

                    SPH_CSA = 4*22/7*SPH_R**2

                    print("\nThe CSA of sphere is --> ",SPH_CSA)

            elif SHP_CHOICE == 'VOLUME':

                    SPH_R = int(input("\nWhat is the RADIUS? -->"))

                    SPH_VOL = 4/3*(SPH_R**3)

                    print("\nThe volume is -->", SPH_VOL)
    
    elif ANSHUK_THE_BOI == 'HEMI-SPHERE':

            HSP_CHOICE = input("\nwhat do you want to find TSA or CSA or VOLUME of HEMI-SPHERE?")

            if HSP_CHOICE == 'TSA' :
                     
                    HSP_R = int(input("\nWht is the RADIUS? --> "))

                    HSP_TSA = 3*(HSP_R**2)

                    print("\nThe TSA is -->",HSP_TSA )

            elif HSP_CHOICE == 'CSA':

                    HSP_R = int(input("\nWht is the RADIUS? --> "))

                    HSP_CSA = 3*(HSP_R**2)

                    print("\nThe TSA is -->",HSP_CSA )

            elif HSP_CHOICE == 'VOLUME':

                    HSP_R = int(input("\nWht is the RADIUS? --> "))

                    HSP_VOL = 2/3*(HSP_R**3)

                    print("\nThe TSA is -->",HSP_VOL )


print("\nHave an awesome day!!!!!!!!!!!!!!!")

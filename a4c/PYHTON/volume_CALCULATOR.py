HEIGHT_OF_SAHAPE_AQ=0

Q_A =input("in which unit do you want the final answer m^3, km^3, cm^3--->")

if Q_A == 'm^3' :

    LENGTH_OF_SHAPE = int(input("length of the shape--->"))
    UNIT_VALUE_L = input("what is the unit --------->")
    if UNIT_VALUE_L == 'km' :
        LENGTH_OF_SHAPE_AQ= LENGTH_OF_SHAPE*1000
    elif UNIT_VALUE_L == 'cm':
        LENGTH_OF_SHAPE_AQ= LENGTH_OF_SHAPE/100
    else : 
        LENGTH_OF_SHAPE_AQ = LENGTH_OF_SHAPE
            
    BREADTH_OF_SHAPE = int(input("Breadth of the shape --->"))
    UNIT_VALUE_B = input("what is the unit --------->")
    if UNIT_VALUE_B == 'km' :
        BREADTH_OF_SAHAPE_AQ= BREADTH_OF_SHAPE*1000
    elif UNIT_VALUE_B == 'cm':
        BREADTH_OF_SHAPE_AQ = BREADTH_OF_SHAPE/100  
    else : 
        BREADTH_OF_SHAPE_AQ =BREADTH_OF_SHAPE

    HEIGHT_OF_SHAPE =int(input("Height of the shape --->"))
    UNIT_VALUE_H = input("what is the unit --------->")
    if UNIT_VALUE_H == 'km' :
        HEIGHT_OF_SHAPE_AQ= HEIGHT_OF_SHAPE*1000
    elif UNIT_VALUE_H == 'cm':
        HEIGHT_OF_SHAPE_AQ = HEIGHT_OF_SHAPE/100
    else :
        HEIGHT_OF_SHAPE_AQ = HEIGHT_OF_SHAPE

    VOLUME_OF_SHAPE = (LENGTH_OF_SHAPE_AQ*BREADTH_OF_SHAPE_AQ*HEIGHT_OF_SHAPE_AQ)

    print(VOLUME_OF_SHAPE,"m^3")

elif Q_A == 'km^3':
    LENGTH_OF_SAHAPE = int(input("length of the shape--->"))
    UNIT_VALUE_L = input("what is the unit --------->")
    if UNIT_VALUE_L == 'm' :
        LENGTH_OF_SAHAPE_AQ= LENGTH_OF_SAHAPE/1000
    elif  UNIT_VALUE_L == 'cm' :
        LENGTH_OF_SAHAPE_AQ = LENGTH_OF_SAHAPE/100000 
    else : 
        LENGTH_OF_SAHAPE_AQ = LENGTH_OF_SAHAPE
            
    BREADTH_OF_SHAPE = int(input("Breadth of the shape--->"))
    UNIT_VALUE_B = input("what is the unit --------->")
    if UNIT_VALUE_B == 'm' :
        BREADTH_OF_SAHAPE_AQ= BREADTH_OF_SHAPE/1000
    elif  UNIT_VALUE_B == 'cm' :
        LENGTH_OF_SAHAPE_AQ = BREADTH_OF_SHAPE/100000    
    else : 
        BREADTH_OF_SAHAPE_AQ =BREADTH_OF_SHAPE

    HEIGHT_OF_SHAPE =int(input("Height of the shape--->"))
    UNIT_VALUE_H = input("what is the unit --------->")
    if UNIT_VALUE_H == 'm' :
        HEIGHT_OF_SAHAPE_AQ= HEIGHT_OF_SHAPE/1000
    elif  UNIT_VALUE_H == 'cm' :
        LENGTH_OF_SAHAPE_AQ = HEIGHT_OF_SHAPE/100000     
    else :
        HEIGHT_OF_SAHAPE_AQ = HEIGHT_OF_SHAPE

    VOLUME_OF_SHAPE = (LENGTH_OF_SAHAPE_AQ*BREADTH_OF_SAHAPE_AQ*HEIGHT_OF_SAHAPE_AQ)

    print(VOLUME_OF_SHAPE, "km^3")

elif Q_A == 'cm^3':
    LENGTH_OF_SHAPE = int(input("length of the shape--->"))
    UNIT_VALUE_L = input("what is the unit --------->")
    if UNIT_VALUE_L == 'km' :
        LENGTH_OF_SHAPE_AQ= LENGTH_OF_SHAPE*100000
    elif UNIT_VALUE_L == 'cm':
        LENGTH_OF_SHAPE_AQ= LENGTH_OF_SHAPE*100
    else : 
        LENGTH_OF_SHAPE_AQ = LENGTH_OF_SHAPE
            
    BREADTH_OF_SHAPE = int(input("Breadth of the shape --->"))
    UNIT_VALUE_B = input("what is the unit --------->")
    if UNIT_VALUE_B == 'km' :
        BREADTH_OF_SAHAPE_AQ= BREADTH_OF_SHAPE*100000
    elif UNIT_VALUE_B == 'cm':
        BREADTH_OF_SHAPE_AQ = BREADTH_OF_SHAPE*100  
    else : 
        BREADTH_OF_SHAPE_AQ =BREADTH_OF_SHAPE

    HEIGHT_OF_SHAPE =int(input("Height of the shape --->"))
    UNIT_VALUE_H = input("what is the unit --------->")
    if UNIT_VALUE_H == 'km' :
        HEIGHT_OF_SHAPE_AQ= HEIGHT_OF_SHAPE*100000
    elif UNIT_VALUE_H == 'm':
        HEIGHT_OF_SHAPE_AQ = HEIGHT_OF_SHAPE*100
    else :
        HEIGHT_OF_SHAPE_AQ = HEIGHT_OF_SHAPE

    VOLUME_OF_SHAPE = (LENGTH_OF_SHAPE_AQ*BREADTH_OF_SHAPE_AQ*HEIGHT_OF_SHAPE_AQ)

    print(VOLUME_OF_SHAPE,"cm^3")
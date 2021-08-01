# Check the type of triangle

def triangle(d,e,f):
    '''Gives the type of triangle, Right, Acute or Obtuse
       d,e, and f are sides of triangle'''

    n1 = [d,e,f]
    n2 = sorted(n1)
    
    a = n2[0]
    b = n2[1]
    c = n2[2]
    
    #Right-angled triangle
    if a**2 + b**2 == c**2:
        return 'R' 

    #Acute-angled triangle
    elif a**2 + b**2 > c**2:
        return 'A'

    #Obtuse-angled triangle 
    elif a**2 + b**2 < c**2:
        return 'O' 

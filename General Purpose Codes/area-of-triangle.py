def side_length(c):
    
    '''This function gives the side-length of triangle from given coordinates.
    Co-ordinates are given in the form of a list (x1,y1,x2,y2,x3,y3).'''

    x = ((c[2] - c[0])**2 + (c[3] - c[1])**2) ** 0.5
    y = ((c[4] - c[0])**2 + (c[5] - c[1])**2) ** 0.5
    z = ((c[4] - c[2])**2 + (c[5] - c[3])**2) ** 0.5
    
    return x,y,z

def area_triangle(a,b,c):
    
    # a, b, c here are sides and Area is calculated by Heron's Formula
    
    s = (a+b+c) / 2    # s = semiperimeter
    y = s * (s-a) * (s-b) * (s-c)
    area = y ** (0.5)
    
    return area


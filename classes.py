def max(a,b):
    if a>b: return a
    else: return b

def min(a,b):
    if a>b: return b
    else: return a

def fixcolor(color):
    a = [color.r,color.g,color.b]
    for i in range(len(a)):
        if a[i]>255:
            a[i] = 255
        elif a[i]<0:
            a[i] = 0
    return Color(a[0],a[1],a[2])

class Vector:
    """Vector basic library"""
    def __init__(self,x=0,y=0,z=0):
        """init func, vector will be origin if no inputs"""
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,other):
        """define vector + operator"""
        return Vector(self.x+other.x,self.y+other.y,self.z+other.z)

    def __sub__(self,other):
        """define vector - operator"""
        return Vector(self.x-other.x,self.y-other.y,self.z-other.z)

    def __mul__(self,other):
        """define vector * operator as dot product or scalar"""
        if type(other) is Vector:
            return(self.x*other.x + self.y*other.y + self.z*other.z)
        else:
            return(Vector(self.x*other,self.y*other,self.z*other))
    
    def __rmul__(self,other):
        """reverse multiplication protection"""
        return self.__mul__(other)

    def __truediv__(self,other):
        return(Vector(self.x/other,self.y/other,self.z/other))
    
    def __str__(self):
        """define str() method"""
        return str((self.x,self.y,self.z))

    def size(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def normalize(self):
        return self/self.size()

class Color:
    def __init__(self,r=0,g=0,b=0):
        self.r = r
        self.b = b
        self.g = g
    
    def __mul__(self,other):
        return fixcolor(Color(int(self.r*other),int(self.g*other),int(self.b*other)))
    
    def __add__(self,other):
        return Color((self.r+other.r)//2,(self.g+other.g)//2,(self.b+other.b)//2)

    def __sub__(self,other):
        return Color((self.r-other.r)//2,(self.g-other.g)//2,(self.b-other.b)//2)

    def __str__(self):
        return str(self.r)+' '+str(self.g)+' '+str(self.b)

class Ray:
    def __init__(self,origin=Vector(),destination=Vector()):
        self.o = origin
        self.d = destination

class Sphere:
    def __init__(self,center=Vector(),r=0,color=Color()):
        self.center = center
        self.color = color
        self.r = r

    def intersect(self,ray:Ray):
        """check if a ray is intersecting the sphere and where"""
        o = ray.o   #ray origin
        d = ray.d   #ray destination
        oc = o - self.center    #vector from ray origin to center
        b = 2*(oc*d)
        c = oc*oc - self.r**2
        disc = b**2-4*c
        if disc<0:
            return False,-1
        else:
            disc **=0.5
            t0 = -b-disc
            t1 = -b+disc
            return True,max(t0,t1)
    
    def getNormal(self,point:Vector):
        return (self.center-point)/self.r
            

red = Color(255, 0, 0)
green = Color(0, 255, 0)
blue = Color(0, 0, 255)
black = Color(0, 0, 0)
white = Color(255, 255, 255)
gray = Color(125, 125, 125)
yellow = Color(255,255,0)
from classes import *

H = 600  # height of photo
W = 600  # width of photo
D = 600  # depth of photo

light = Sphere(Vector(0,0,D//2),1,white)
intensity = 1.5
backgrond = (black)  # bg color

objectlist = []

objectlist.append(Sphere(Vector(W//4, H//4, 100), W//6, red))
objectlist.append(Sphere(Vector(3*W//4, 3*H//4, 100), W//6, blue))

photopath = 'p.ppm'  # output file path
photo = open(photopath, 'w')

photo.write('P3\n')
photo.write(str(W)+' '+str(H)+' 255\n')  # print header of file

for i in range(W):
	print("rendering... {0}%".format((i/W)*100))
	for j in range(H):
		o=Vector(j, i, 0)
		d=Vector(0, 0, 1)
		ray=Ray(o, d)
		hits = []
		for obj in objectlist:
			hit, point = obj.intersect(ray)
			if hit:
				pi = o+d*point
				L = light.center - pi
				N = obj.getNormal(pi)
				dt = L.normalize() * N.normalize()
				hits.append((str(obj.color + (light.color*dt*intensity) )+'\n',obj.center.z+obj.r))
			else:
				hits.append((str(backgrond)+'\n',10000))
			photo.write(closesthit(hits))

photo.close()
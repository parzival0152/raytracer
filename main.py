from classes import *

H = 600  # height of photo
W = 600  # width of photo
D = 600  # depth of photo

light = Sphere(Vector(W,H,300),1,white)
backgrond = black  # bg color

redball = Sphere(Vector(W/2, H/2, 0), 200, red)

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
		hit, point = redball.intersect(ray)
		if hit:
			pi = o+d*point
			L = light.center - pi
			N = redball.getNormal(pi)
			dt = L.normalize() * N.normalize()
			photo.write(str(redball.color+ (light.color*dt*2) )+'\n')
		else:
			photo.write(str(backgrond)+'\n')

photo.close()
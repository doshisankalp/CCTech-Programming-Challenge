
def checkInside(polygon,p):
	"line parallel to x-axis from p is considered like for how much times it will intersect the sides of polygon. The line parallel to x-axis will be y=0*x + p[1]. If line intersects with even sides of polygon then the point is outside the polygon or else it is inside the polygon"
	#print("Check Inside")
	count=0
	N=len(polygon)
	x_intersect=0.0
	#y-intercept will be same for whole line as line is parallel to x-axis so only to find x-intercestion
	p1=[]
	p2=[]
	
	#Iterating along sides of polygon
	p1=polygon[0]
	#print(N)
	for i in range(1,N+1):
		p2=polygon[i%N]
		if(p[1]>min(p1[1],p2[1])):
			if(p[1]<=max(p1[1],p2[1])):
				if(p[0]<=max(p1[0],p2[0])):
					if(p1[1]!=p2[1]):
						x_intersect=(p[1]-p1[1])*(p2[0]-p1[0])+p1[0] 
						"formula (y3-y1)*(x2-x1)+x1 where p(x3,y3), p1(x1,y1), p2(x2,y2)"
						if(p1[0]==p2[0] or p[0]<=x_intersect):
							count+=1
		p1=p2
	if(count%2==0):
		return "False"
	else:
		return "True"

	
'''
if __name__ == "__main__":
	#print("Hello")
	polygon = [ ] 
	n = int(input("Enter number of elements : ")) 
	for i in range(0, n):
		ele=[float(input("x - ")),float(input("y - "))]
		polygon.append(ele)
	#print(polygon)
	print("Enter point P which needs to be checked")
	P=[float(input("x - ")),float(input("y - "))]
	#print(P)
	result = checkInside(polygon,P)
	print(result)
'''

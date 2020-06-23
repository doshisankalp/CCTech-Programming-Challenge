
def distanceBetween(p,q):
	"To calculate distance between points p an q"
	return (((abs(p[0]-q[0])**2)+(abs(p[1]-q[1])**2)) ** 0.5)
	
def minDistance(lst,p):
	"lst=[[,],[,],[,]] and p=[,] returns index of point which is at minimum distance from point p"
	minimum=0
	index=0
	for i in range(0,4):	#4 is length of lst i.e building coordinates
		if(minimum>distanceBetween(lst[i],p)):
			minimum=distanceBetween(lst[i],p)
			index=i
	return index
			

def buildingExposed(society,p):
	#print(len(society))
	ret_distance=0
	for i in range(0,len(society)):
		near_index=minDistance(society[i],p) #near_index is nearest index to point p
		edge1=distanceBetween(society[i][(near_index+3)%4],society[i][near_index])
		edge2=distanceBetween(society[i][(near_index+5)%4],society[i][near_index])
		ret_distance+=(edge1+edge2) #distance between the nearest point and the before and after point
		#print(ret_distance)
		
	for i in range(0,len(society)-1):
		if(distanceBetween(society[i][1],society[i][0])<=distanceBetween(society[i+1][1],society[i+1][0])):	#If before building is shorter than equal to next building
			society1=society[i]
			society2=society[i+1]

			#print(society1,society2,y_intersect)
			#a,b,c for line 1 i.e. a1x + b1y = c1
			a1 = society[i][3][1] - p[1] 
			b1 = p[0] - society[i][3][0] 
			c1 = a1*p[0] + b1*p[1]

			#a,b,c for line 1 i.e. a2x + b2y = c2
			a2 = society[i+1][1][1] - society[i+1][0][1]
			b2 = society[i+1][0][0] - society[i+1][1][0] 
			c2 = a2*society[i+1][0][0] + b2*society[i+1][0][1]
			
			determinant = a1*b2 - a2*b1
			
			x_intersect = (b2*c1 - b1*c2)/determinant
			y_intersect = (a1*c2 - a2*c1)/determinant
			intersection_point=[]
			intersection_point.append(x_intersect)
			intersection_point.append(y_intersect)
			#print(a1,b1,c1,a2,b2,c2)
			#print(intersection_point)
			#print(x_intersect,y_intersect)
			ret_distance-=distanceBetween(intersection_point,society[i+1][1])
			
		if(distanceBetween(society[i][1],society[i][0])>distanceBetween(society[i+1][1],society[i+1][0])):	#If before building is taller than next building
			society1=society[i]
			society2=society[i+1]

			#print(society1,society2,y_intersect)
			#a,b,c for line 1 i.e. a1x + b1y = c1

			a1 = society[i][3][1] - p[1] 
			b1 = p[0] - society[i][3][0] 
			c1 = a1*p[0] + b1*p[1]
			
			#a,b,c for line 1 i.e. a2x + b2y = c2
			a2 = society[i+1][3][1] - society[i+1][0][1]
			b2 = society[i+1][0][0] - society[i+1][3][0] 
			c2 = a2*society[i+1][0][0] + b2*society[i+1][0][1]
			
			determinant = a1*b2 - a2*b1
			if(determinant==0):
				#Both the lines are parallel
				ret_distance-=distanceBetween(society[i+1][0],society[i+1][3])	#Shadow part of first building that is falling on second building
			else:
				x_intersect = (b2*c1 - b1*c2)/determinant
				y_intersect = (a1*c2 - a2*c1)/determinant
				intersection_point=[]
				intersection_point.append(x_intersect)
				intersection_point.append(y_intersect)
				#print(a1,b1,c1,a2,b2,c2)
				#print(intersection_point)
				ret_distance-=distanceBetween(intersection_point,society[i+1][0])	#Shadow part of first building that is falling on second building
			ret_distance-=distanceBetween(society[i+1][0],society[i+1][1])	#Height of 2nd building that is under shadow of 1st building
			
	return ret_distance



'''
if __name__ == "__main__":
	#print(distanceBetween([1,4],[1,0]))
	#quit()
	society = [ ] 
	n = int(input("Enter number of elements : ")) 
	for i in range(0, n):
		building = [] 
		print("Enter",i+1,"th building co-ordinates")
		for i in range(0,4):
			ele=[float(input("x - ")),float(input("y - "))]
			building.append(ele)
		society.append(building)
	#print(society)
	print("Enter position of sun: ")
	p=[float(input("x - ")),float(input("y - "))]
	result=buildingExposed(society,p)
	
	print("Output:",result)
	print("END")
	
	

Sample Input 2(3 buildings in descending order of their heights):

sankalp@sankalp:~$ python3 sunlight.py 
Enter number of elements : 3
Enter 1 th building co-ordinates
x - 0 
y - 4
x - 0
y - 0
x - 4
y - 0
x - 4
y - 4
Enter 2 th building co-ordinates
x - 6
y - 6
x - 6
y - 0
x - 8
y - 0
x - 8
y - 6
Enter 3 th building co-ordinates
x - 10
y - 7
x - 10
y - 0
x - 12
y - 0
x - 12
y - 7
Enter position of sun: 
x - -2
y - 10
Output: 17.8
END

Sample Input 1(2 buildings where 1st building is taller than first): 

sankalp@sankalp:~$ python3 sunlight.py 
Enter number of elements : 2
Enter 1 th building co-ordinates
x - 0
y - 8
x - 0
y - 0
x - 2
y - 0
x - 2
y - 8
Enter 2 th building co-ordinates
x - 4
y - 4
x - 4
y - 0
x - 8
y - 0
x - 8
y - 4
Enter position of sun: 
x - -2
y - 12 
Output: 12.0

'''

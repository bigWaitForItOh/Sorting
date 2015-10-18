#A generic implementation of Quick Sort
##IF YOU ARE PASSING A USER-DEFINED OBJECT, MAKE SURE THE CLASS HAS THE OPERATORS '==', '<' & '>' OVERLOADED IN ORDER FOR THE COMPARISON TO WORK. YOU CAN DO THIS AS FOLLOWING INSIDE THE CLASS:
#def __eq__ (self, otherObject):
	#LOGIC TO DETERMINE WHETHER 2 OBJECTS ARE EQUAL OR NOT
#def __gt__ (self, otherObject):	
	#LOGIC TO DETERMINE WHETHER self > otherObject
#def __lt__ (self, otherObject):
	#LOGIC TO DETERMINE WHETHER self < otherObject

def partition (array, start, end):
	#THE LAST ELEMENT IN THE LIST IS ALWAYS SELECTED AS THE PIVOT
	i = start - 1;
	for j in range (start, end):
		#THE INEQUALITY SIGN BELOW DETERMINES WHETHER THE SORT IS IN ASCENDING (<=) OR DESCENDING (>=) ORDER
		if (array [j] <= array [end]):
			i += 1;
			array [j], array [i] = array [i], array [j];

	array [end], array [i + 1] = array [i + 1], array [end];
	return (i + 1);

def quick_sort (array, start, end):
	if (start < end):
		pivotPoint = partition (array, start, end);
		quick_sort (array, start, pivotPoint - 1);
		quick_sort (array, pivotPoint + 1, end);

#USAGE:
#quick_sort (array_name, starting_position, ending_position);
#example:

#arr = [-2, 2, 4, 7, 5, 3];
#quick_sort (arr, 0, len (arr) - 1);
#print (arr);

def insertion_sort (array):
	size = len (array) + 1;
	array = [-float ('inf')] + array;

	for upper in range (2, size):
		last = array [upper];
		for i in range (upper - 1, -1, -1):
			if (array [i] > last):
				array [i + 1] = array [i];
			else:
				array [i + 1] = last;
				break;

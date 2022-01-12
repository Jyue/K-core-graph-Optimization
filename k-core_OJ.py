import sys
vertex_degree = {}
vertex_relation = []


# Return key in vertex_degree for any value.
def get_key_in_vertex_degree(val):
	global vertex_degree
	goal = []

	for key, value in vertex_degree.items():
		if val == value:
			goal.append(key)

	if goal:
		return goal

	else:
		#print("key doesn't exist")
		return -1


def remove_vertex(v):
	global vertex_degree
	global vertex_relation
	#global vertex_relation_tmp
	#vertex_relation_tmp = vertex_relation.copy() # vertex_relation_tmp: Store the vertex_relation status before removal.

	# TEST
	"""
	print("[BEFORE] remove_vertex TEST")
	for key,value in vertex_degree.items():
	    print('vertex {key}:{value}'.format(key = key, value = value))
	for relation in vertex_relation:
		print(relation)

	print("-------------------------")

	"""
	
	adjacent = []
	remove_edges = []

	# 1. Find pairs in vertex_relation 
	for edge in vertex_relation:

		if edge[0] == v or edge[1] == v:

			# Collect all the adjacent vertex of v and v itsetf.
			if edge[0] not in adjacent:
				adjacent.append(edge[0])
			if edge[1] not in adjacent:
				adjacent.append(edge[1])
			remove_edges.append(edge)
	# 2. Remove these pairs in vertex_relation.
	for edge in remove_edges:
		vertex_relation.remove(edge)


	# 3. All the degree af adjacnet vertex (include itself) -1 in vertex_degree.
	for vertex in adjacent:
		vertex_degree[vertex] -= 1



	# 4. If vertex_degree <= 0, Remove it.
	for pair in list(vertex_degree.items()):
		if pair[1] <= 0:
			vertex_degree.pop(pair[0])
			#del vertex_degree[pair[0]]



	# 5. Remove v.
	if v in vertex_degree:
		vertex_degree.pop(v)



	# TEST
	"""
	print("-------------------------")
	print("[AFTER]remove_vertex TEST")
	for key,value in vertex_degree.items():
	    print('vertex {key}:{value}'.format(key = key, value = value))
	for relation in vertex_relation:
		print(relation)

	"""



# Update vertex_degree dict according to the given node.
def update_degree(v):
	global vertex_degree

	if v in vertex_degree:
		vertex_degree[v] += 1

	else:
		vertex_degree[v] = 1 


# Update update_relation list according to the given node pair.
def update_relation(a,b):
	global vertex_relation

	if (a,b) not in vertex_relation:
		vertex_relation.append((a,b))




def remove_vertex_with_degree(k):
	global vertex_degree
	global vertex_relation

	#print("remove_vertex_with_degree" , k)
	# print key with val k

	remove_key = get_key_in_vertex_degree(k)
	#print(remove_key)
	if remove_key == -1:
		return 0
	else:
		for key in remove_key:
			# TEST
			#print("Remove key = ",key)

			remove_vertex(key)

			
		return 1


def kcore_based():
	k = 2
	while(vertex_degree):

		for d in reversed(range(1,k)):
			while(remove_vertex_with_degree(d)!=0):
				pass
				#print("Remove the vertex with degree ",d)
			

		if (vertex_degree):	# Pass the TEST
			vertex_relation_print = vertex_relation.copy()
			#print(k, " - core graph exist.")
			k += 1
		else:
			k -= 1
			break
	return vertex_relation_print, k

def OUTPUT(vertex_relation_print, k):
	print(str(k)+"-core")
	for relation in vertex_relation_print:
		print(relation[0], relation[1])
			


vertex_relation_print = []

#filename = 'input2.txt'
#with open(filename) as f:


while True:

	line = sys.stdin.readline()

	
	try:

		line = line.split()
		a = int(line[0])
		b = int(line[1])

		update_degree(a)
		update_degree(b)
		update_relation(a,b)

	except:
		
		vertex_relation_print, k = kcore_based()
		# OUTPUT
		OUTPUT(vertex_relation_print, k)
		
from sys import stdin, stdout
vertex_degree = {}
vertex_relation = []
flag = {}


class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
	def __init__(self, num):
				self.V = num
				self.graph = [None] * self.V

	# Add edges
	def add_edge(self, s, d):
		node = AdjNode(d)
		node.next = self.graph[s]
		self.graph[s] = node

		node = AdjNode(s)
		node.next = self.graph[d]
		self.graph[d] = node

	# Print the graph
	def print_agraph(self):
		for i in range(self.V):
			if (i > 10):
				break
			print("Vertex " + str(i) + ":", end="")
			temp = self.graph[i]
			while temp:
				print(" -> {}".format(temp.vertex), end="")
				temp = temp.next
			print(" \n")
	
	def minus_degree(self,v):
		global vertex_degree
		global vertex_relation

			
		# All the degree af adjacnet vertex (include itself) -1 in vertex_degree.
		vertex_degree[v] -= 1

		temp = self.graph[v]
		while temp:
			vertex_degree[temp.vertex] -= 1
			temp = temp.next


def vertex_relation_sort():
	global vertex_relation
	vertex_relation.sort(key=lambda x: (x[0],x[1]))  # sorts in place


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

"""
def minus_degree(v,):
	global vertex_degree
	global vertex_relation

			
	# All the degree af adjacnet vertex (include itself) -1 in vertex_degree.
	vertex_degree[vertex] -= 1

	temp = self.graph[v]
	while temp:
		vertex_degree[temp.vertex] -= 1
		temp = temp.next
"""

def flag_vertex_with_degree(k, flag, graph):
	global vertex_degree
	global vertex_relation


	flag_key = get_key_in_vertex_degree(k)

	# If its flag = 1, ignore
	if flag_key == -1:
		return 0

	else:
		flag_key = [i for i in flag_key if flag[i] == 0]

		if not flag_key:
			return 0

		flag_count = len(flag_key)

		for key in flag_key:

			flag[key] = 1
			graph.minus_degree(key)
			#minus_degree(key)

			
		return flag_count




def kcore_only_labeled(graph): # "Scalable K-Core Decomposition for Static Graphs Using a Dynamic Graph Data Structure"
	global flag
	k = 2
	num_active = len(vertex_degree)

	flag = vertex_degree.fromkeys(vertex_degree, 0); # Record states of every node. 1 -> Remove.(Not explicit)
	while(num_active>0):

		for d in reversed(range(1,k)):
			while(True):
				count = flag_vertex_with_degree(d, flag, graph)
				#print("flag status = ",[i for i in flag if flag[i]==1])
				if(count<=0):
					break
				num_active -= count
				if(num_active<=0):
					break
				#print("num_active = ",num_active)	
			#print(vertex_degree)
	
			

		if (num_active>0):	# Pass the TEST
			#print(k, " - core graph exist.\n")
			final_flag = [i for i in flag if flag[i]==1]
			k += 1
		else:
			k -= 1
			break

	vertex_relation_print = []
	for edge in vertex_relation:

		if (edge[0] in final_flag) or (edge[1] in final_flag):
			continue
		else:
			vertex_relation_print.append(edge)

	return vertex_relation_print, k


def OUTPUT(vertex_relation_print, k):
	ans=''
	if vertex_relation_print:
		print(str(k)+"-core")
		for relation in vertex_relation_print:
			ans += str(relation[0]) + " " + str(relation[1]) + '\n'
			#print(relation[0], relation[1])
		stdout.write(ans + '\n')
	# Clean all the data
	global vertex_degree
	global vertex_relation
	global flag
	vertex_degree.clear() 
	vertex_relation.clear() 
	flag.clear() 
	#print("vertex_relation = ",vertex_relation)

			




vertex_relation_print = []

#filename = 'input2.txt'
#with open(filename) as f:

i = 10

while (i>0):

	try:
		line = stdin.readline().strip()

		#print(line)
		line = line.split()
		a = int(line[0])
		b = int(line[1])
		
		# Update vertex_degree dict according to the given node.
		if a in vertex_degree:
			vertex_degree[a] += 1
		else:
			vertex_degree[a] = 1

		if b in vertex_degree:
			vertex_degree[b] += 1
		else:
			vertex_degree[b] = 1 

		# Update update_relation list according to the given node pair.
		if (a,b) not in vertex_relation:
			vertex_relation.append((a,b))
		
		


	except:
		#print("EOF! i = ",i)
		vertex_relation_sort()
		# Build Adjencency List list according to the given node pair.
		graph = Graph(1000)
		for a,b in vertex_relation:
			graph.add_edge(a, b)
		
		#graph.print_agraph()
		
		vertex_relation_print, k = kcore_only_labeled(graph)
		# OUTPUT
		OUTPUT(vertex_relation_print, k)

		i -= 1


		
			

	
	

		
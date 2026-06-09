class Node:
	def __init__(self, key, value):
		self.key, self.value = key, value
		self.prev = self.next = None
		
class LRUCache:
	def __init__(self, capacity: int):
		# initialize data structures
		self.cap = capacity
		self.cache = {}
		
		#Left = LRU, right= most recent
		self.left, self.right = Node(0,0), Node(0,0)
		self.left.next, self.right.prev = self.right, self.left 
		
	def remove(self, node):
		prev, nxt = node.prev, node.next
		prev.next, nxt.prev = nxt, prev
	
	def insert(self ,node):
		prev, nxt = self.right.prev, self.right
		prev.next = nxt.prev =node
		node.next, node.prev = nxt, prev
				
	def get(self, key)-> int:
		# main return value, update to most recent
		if key in self.cache:
			#TODO : update most recent
			self.remove(self.cache[key])
			self.insert(self.cache[key])
			return self.cache[key].value
		return -1
	
	def put(self, key: int, value: int) -> None:
		# main: add or update, evict LRU if over capacity
		if key in self.cache:
			self.remove(self.cache[key])
		self.cache[key] = Node(key, value)
		self.insert(self.cache[key])
				
		if len(self.cache) > self.cap:
			# remove from the list and delete the LRU from the hashmap
			lru = self.left.next
			self.remove(lru)
			del self.cache[lru.key]
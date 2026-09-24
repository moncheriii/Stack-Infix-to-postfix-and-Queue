"""ITECC04 Laboratory 4, Part D: the circular queue and the deque.

This part is on your own. No guided walkthrough, and the tests are the only
feedback you get, exactly as in the coding quiz.

WHY CIRCULAR. A queue over a plain list, dequeuing with pop(0), shifts every
remaining element one place left. That is O(n) for an operation that should
be O(1). Moving the FRONT INDEX forward instead of moving the data is the
whole idea, and the modulo operator is what makes the index wrap back to 0
when it runs off the end.

The queue holds a fixed number of slots. It does not grow.
"""

class CircularQueue:
	def __init__(self, capacity):
		if capacity < 1:
			raise ValueError("capacity must be at least 1")
		self.capacity = capacity
		self._items = [None] * capacity
		self.front = 0
		self.count = 0

	"""Step 1. A list of `capacity` Nones, a front index, and a count.
	
	Raise ValueError if capacity is less than 1.
	Keep a COUNT, not a rear index alone. With only front and rear you
	cannot tell a full queue from an empty one: both give front == rear.
	A count answers both questions with no ambiguity.
	"""

	def enqueue(self, item):
		if self.count == self.capacity:
			raise OverflowError("enqueue on a full queue")
		rear = (self.front + self.count) % self.capacity
		self._items[rear] = item
		self.count += 1
    #"""Step 2. Add at the rear. Raise OverflowError when full.
	
    #You are not storing a rear index, so compute it:
    # rear = (front + count) % capacity
	#Write the item there, then increase the count.
    # #"""
	
    
	def dequeue(self):
		if self.is_empty():
			raise IndexError("dequeue from an empty queue")
		item = self._items[self.front]
		self._items[self.front] = None
		self.front = (self.front + 1) % self.capacity
		self.count -= 1
		return item
    #"""Step 3. Remove and return the front item. IndexError when empty.
	
    #Read the item at front, clear that slot to None so nothing stale is
    #left behind, advance front with modulo, decrease the count, return.
    #"""

	def peek(self):
		
		if self.is_empty():
			raise IndexError("peek on an empty queue")
		return self._items[self.front]
	
    #"""Step 4. Return the front item without removing it."""
	
	def is_empty(self):
		return self.count == 0

	# """Step 5. True when the count is 0."""

	def is_full(self):
		return self.count == self.capacity

	# """Step 6. True when the count has reached the capacity."""

	def size(self):
		return self.count
	# """Step 7. Return the count."""

	def slots(self):
		# """Written for you. Returns a copy of the raw list.

		# For inspecting wraparound during the demonstration. Not part of the
		# ADT, and your other methods must never call it.
		# """
		return list(self._items)

    
class Deque:
	def __init__(self):
		self._list = []

	def add_front(self, item):
		self._list.insert(0, item)

	def add_rear(self, item):
		self._list.append(item)

	def remove_front(self):
		if self.is_empty():
			raise IndexError("remove_front from an empty deque")
		return self._list.pop(0)

	def remove_rear(self):
		if self.is_empty():
			raise IndexError("remove_rear from an empty deque")
		return self._list.pop()

	def is_empty(self):
		return len(self._list) == 0

	def size(self):
		return len(self._list)


def is_palindrome(text):
	letters = Deque()
	for ch in text:
		if ch.isalpha():
			letters.add_rear(ch.lower())
	while letters.size() > 1:
		if letters.remove_front() != letters.remove_rear():
			return False
	return True
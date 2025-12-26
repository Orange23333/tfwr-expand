def init_array(n, default_value=0):
	new_array = []
	for _ in range(n):
		new_array.append(default_value)
	return new_array

# === Quick Sort ===:
# Impelement of quick sort algorithm refers to https://www.cnblogs.com/kevinbee/p/18678275 .

def _swap(a, b):
	return b, a


def _qsort_partition(arr, low, high):
	pivot = arr[high]
	
	i = low - 1
	for j in range(low, high):
		if arr[j] < pivot:
			i += 1
			arr[i], arr[j] = _swap(arr[i], arr[j])

	arr[i + 1], arr[high] = _swap(arr[i + 1], arr[high])
	return i + 1


def _qsort(arr, low, high):
	if low < high:
		pi = _qsort_partition(arr, low, high)

		_qsort(arr, low, pi - 1)
		_qsort(arr, pi + 1, high)


def qsort(arr):
	qsort(arr, 0, len(arr) - 1)

# :=== Quick Sort ===

# === Heap ===:
# Impelement of heap algorithm refers to https://www.runoob.com/w3cnote/heap-sort.html .

def _heap_node_parent(index):
	# index should be greater than 0
    return (index - 1) // 2


def _heap_node_left_child(index):
    return 2 * index + 1


def _heap_node_right_child(index):
	return 2 * index + 2


def _min_heapify(arr, n, i):
    pass


def heap_sort(arr):
    pass


def add_to_heap(heap, value):
	pass

# :=== Heap ===

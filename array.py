#declare an array in python.
class Array:
    def __init__(self, arr=None, capacity=None):
        if isinstance(arr, list):
            self._data = arr[:]
            self._size = len(arr)
            return
        self._data = [None] * capacity
        self._size = 0
        
    #get the size of array
    def get_size(self):
        return self._size
        
    #get the length of array
    def get_capacity(self):
        return len(self._data)
        
    #set array size as 0
    def is_empty(self):
        return self._size == 0
        
    #add element to an array at the end
    def add_element_end(self, ele):
        return self._data.append(ele)
        
    #add element to an array at index
    def add_ele_index(self, ele, index):
        return self._data.insert(index, ele)

    #add element to at the front of an array
    def add_ele_front(self,ele):
        self._data.insert(0, ele)
        
    #replace element at index
    def replace_ele(self, ele, i):
        self._data[i] = ele

    #show element at index
    def show_ele(self, index):
        return self._data[index]

    #remove an ele at index
    def remove_ele(self, index):
        self._data.pop(index)
        
    #swap ele
    def swap_ele(self,ele1, ele2):
        temp = self._data[ele1]
        self._data[ele1] = self._data[ele2]
        self._data[ele2] = temp
        
    #sort array
    def sort_ele(self):
        self._data.sort()

    #if ele in arr
    def is_involved(self, ele):
        count = 0
        for i in range(len(self._data)):
            if self._data[i] == ele:
                count += 1

        return str(count) + ' times ' +  str(ele) + ' in array'







def r_child(i):
    return i*2 + 1
def l_child(i):
    return i*2
def parent(i):
    return i//2
def size(tab):
    return tab[0]
def is_minlvl(tab,i):
    if l_child(i) < size(tab):
        if tab[l_child(i)] > tab[i]:    return True
        else: return False
    elif parent(i) < size(tab):
        if tab[parent(i)] > tab[i]:     return True
        else: return False

def heapify(t,i):
    pass

def buildHeap():
    pass
def get_min():
    pass
def get_max():
    pass
def insert():
    pass



t = [2,4,21,7,5,1,87,23,6,12]
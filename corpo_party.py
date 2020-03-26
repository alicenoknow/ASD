class Employee:
    def __init__(self, fun, name):
        self.emp = []
        self.fun = fun          # party lvl
        self.f = -1             # best party we can get with or without self
        self.g = -1             # best party without self
        self.name = name
        self.f_guestlist = []
        self.g_guestlist = []


def f(v):
    if v.f >= 0:
        return v.f
    x = v.fun
    v.f_guestlist.append(v.self)
    for vi in v.emp:
        x += g(vi)      # best party with self
        v.f_guestlist.extend(vi.g_guestlist)
    y = g(v)            # best party without self
    if y > x:
        v.f_guestlist = v.g_guestlist
    v.f = max(x, y)     # best possible party
    return v.f


def g(v):
    if v.g >= 0:
        return v.g
    v.g = 0
    for vi in v.emp:
        v.g += f(vi)    # sum of parties of subordinates -> self not going
        v.g_guestlist.extend(vi.f_guestlist)
    return v.g


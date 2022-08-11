from package import LogicDoor


class Binary:
    def __init__(self, rgt1: list, rgt2: list):
        self.door = LogicDoor()
        self.equalRgt = self.equal_len_number(rgt1, rgt2)
        self.rgt1 = self.equalRgt[0]
        self.rgt2 = self.equalRgt[1]
        self.rgt3 = []
        self.after_c = 0

        self.rgt1.reverse()
        self.rgt2.reverse()

    def binary_addition(self, a, b, Cin):
        s = self.door.logic_xor(a, b)
        c = self.door.logic_and(a, b)
        S = self.door.logic_xor(s, Cin)
        d1 = self.door.logic_and(s, Cin)
        Cout = self.door.logic_or(d1, c)
        return S, Cout

    def exe(self):
        for i in range(len(self.rgt1)):
            calcul = self.binary_addition(self.rgt1[i], self.rgt2[i], self.after_c)
            self.rgt3.append(calcul[0])
            self.after_c = calcul[1]

        self.rgt3.reverse()
        return self.rgt3

    def equal_len_number(self, a: list, b: list):
        l1 = len(a)
        l2 = len(b)
        if len(a) > len(b):
            for i in range(l1 - l2):
                b.insert(0, 0)
        elif len(b) > len(a):
            for i in range(l2 - l1):
                a.insert(0, 0)
        return a, b

    def log(self):
        b1 = "".join(list(map(str, self.rgt1)))
        b2 = "".join(list(map(str, self.rgt2)))
        n1 = int(b1, 2)
        n2 = int(b2, 2)
        r = "".join(list(map(str, list(self.rgt3))))
        print(int(r, 2))


# 00101111
# 00001010
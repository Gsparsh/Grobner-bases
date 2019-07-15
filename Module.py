from Poly import Poly
from mono import mono
import random as r
from itertools import permutations

class Module(Poly, mono):

    def __init__(self):
        """
        To initialize a module list containing zero polynomial

        """

        self.module = []

    def getValuesModules(self):
        """
        To input polynomials in a module

        """

        self.module = []
        n = int(input('How many Polynomials ?'))
        for i in range(n):
            print("Enter Details for Polynomial", i + 1)
            p = Poly()
            p.getValuesPoly()
            self.module.append(p)

    def repr_module(self, x):
        """
        This function represents a module containing polynomials

        :param x: module to be represented
        :return: string representation of a module

        """
        string = '( '
        # print(' < ')
        for i in range(len(x.module)):
            p = Poly()
            if i < len(x.module) - 1:
                string = string + str(p.repr_poly(x.module[i]))
                string = string + str(' , ')
            else:
                string = string + str(p.repr_poly(x.module[i]))
                string = string + str(' )')
        print(string)

    def add_module(self, first, second):
        """
        This function is used to add two modules of equal length.
        :param first: module
        :param second: module
        :return: result module

        """
        self.module = []
        l1 = len(first.module)
        l2 = len(second.module)
        if l1 != l2:
            print('Error!!, bases of both modules should be of same length')
            exit()
        else:
            for i in range(len(first.module)):
                p = Poly()
                p.poly = []
                p.add(first.module[i], second.module[i])
                self.module.append(p)
        return self

    def sub_module(self, first, second):
        """
        This function returns the subtraction of one module from another.
        :param first: module
        :param second: module
        :return: result module

        """
        self.module = []
        l1 = len(first.module)
        l2 = len(second.module)
        if l1 != l2:
            print('Error!!, bases of both modules should be of same length')
            exit()
        else:
            for i in range(len(first.module)):
                p = Poly()
                p.poly = []
                p.sub(first.module[i], second.module[i])
                self.module.append(p)
        return self

    def mult_module(self, first, second):
        """
        this function returns the product of two modules.
        :param first: module
        :param second: module
        :return: product of two modules

        """
        self.module = []
        l1 = len(first.module)
        l2 = len(second.module)
        if l1 != l2:
            print('Error!!, bases of both modules should be of same length')
            exit()
        else:
            for i in range(len(first.module)):
                p = Poly()
                p.poly = []
                p.mult(first.module[i], second.module[i])
                self.module.append(p)
        return self

    def lt_in_module(self, preff, choice):
        """
        This function returns the leading term and index according to deglex ordering
        :param preff: between x > y > z and more cases
        :param choice: between Term over position or Position over term
        :return: monomial

        """

        ch = 0
        x = preff[0]
        y = preff[1]
        z = float(preff[2])
        while ch == 0:

            if choice == 1:
                ch = ch + 1
                p = Poly()
                p.poly = []

                for i in range(len(self.module)):
                    e = mono()
                    e = self.module[i].leading_term(preff)
                    p.poly.append(e)
                # -----------------------------------------------------------
                m = mono()
                a = Poly()
                a.poly = []
                for i in range(len(p.poly)):
                    lo = mono()
                    lo.x = x * p.poly[i].x
                    lo.y = y * p.poly[i].y
                    lo.z = z * p.poly[i].z
                    a.poly.append(lo)

                if p.poly[0].c == 0:
                    sum0 = 0
                else:
                    sum0 = (a.poly[0].x + a.poly[0].y + a.poly[0].z)
                    index = 0
                big = mono()
                big = p.poly[0]
                index = 0
                for i in range(len(a.poly)):
                    sum = (a.poly[i].x + a.poly[i].y + a.poly[i].z)

                    if sum > sum0 and p.poly[i].c != 0:
                        sum0 = sum
                        big = p.poly[i]
                        index = i
                    else:
                        pass
                m = big
                #  -----------------------------------------------------------
                # m = p.leading_term(preff)
                return m, index

            elif choice == 2:
                ch = ch + 1
                while char == 0:

                    char = int(input('Choose any one: \nMenu \n1. First Base at Highest \n2. Last base at Highest'))
                    if char == 1:
                        m = mono()
                        m = self.module[0].leading_term(preff)
                        return m

                    elif char == 2:
                        l = len(self.module)
                        n = l - 1
                        m = mono()
                        m = self.module[n].leading_term(preff)
                        return m

                    else:
                        print('Wrong Input!! Try Again ')
                        char = 0
            else:
                print('Wrong Input!! Try Again ')
                ch = 0

    def leader_in_modules(self, lead):

        m = mono()
        if lead == 1:
            m, index = self.lt_in_module([3, 2, 1], 1)
        elif lead == 2:
            m, index = self.lt_in_module([2, 3, 1], 1)
        elif lead == 3:
            m, index = self.lt_in_module([1, 2, 3], 1)
        return m, index

    def is_div_by_mod(self, other):

        flag = 0
        for i in other:
            for j in i.module:
                for k in self.module:
                    if k.is_div_by_poly(j):
                        flag = 1
        if flag == 1:
            return True
        else:
            return False

    def simplified_module(self):
        """
        This function simplifies a given function.

        :return: Simplied module
        """
        for i in range(len(self.module)):
            self.module[i].simplified()

        return self

    def isNotEmpty(self):
        for i in range(len(self.module)):
            for j in range(len(self.module[i].poly)):
                if self.module[i].poly[j].c != 0:
                    return True
        return False

    def s_polynomial_for_modules(self, f, g, preff, choice):
        lt_f, index = f.lt_in_module(preff, choice)
        lt_g, index = g.lt_in_module(preff, choice)
        l = mono()
        l = l.lcm(lt_f, lt_g)
        t1 = mono()
        t1.monoDiv(l, lt_f)
        t2 = mono()
        t2.monoDiv(l, lt_g)

        T1 = Module()
        T2 = Module()
        for i in f.module:
            p = Poly()
            p.monoMultPoly(t1, i)
            T1.module.append(p)
        for i in g.module:
            p = Poly()
            p.monoMultPoly(t2, i)
            T2.module.append(p)

        return self.sub_module(T1, T2)

    def division_in_modules(self, f, G, preff, choice):
        """
        This algorithm returns boolean True if f is reducible by G, otherwise it returns boolean False
        :param choice:
        :param preff:
        :param f: module containing polynomials
        :param G: set of Modules.
        :return: reduced remainder
        """

        a = Poly()
        b = Poly()
        c = Poly()
        z = mono()
        a.poly.append(z)
        b.poly.append(z)
        c.poly.append(z)
        r = Module()
        r.module = []
        r.module.append(a)
        r.module.append(b)
        r.module.append(c)

        h = Module()
        h.module = f.module
        lt_h = mono()
        lt_h, index1 = h.lt_in_module(preff, choice)
        Flag_r = 0
        o = 0
        while o < 10 and h.isNotEmpty():
            o = o + 1
            for i in G:
                lt_Gi = mono()
                lt_Gi, index2 = i.lt_in_module(preff, choice)
                Flag_r = 0

                if lt_h.is_divisible_by(lt_Gi) and index1 == index2:

                    m = Module()
                    e = Poly()
                    ind = Poly()
                    mulP = Poly()
                    div = mono()
                    d = Module()
                    s = Module()
                    k = Module()
                    m.module = []
                    e.poly = []
                    for j in i.module:
                        m.module.append(j)
                    ind = i.module[index1]
                    div.monoDiv(lt_h, lt_Gi)
                    mulP = mulP.monoMultPoly(div, ind)
                    m.module[index1] = mulP
                    k = s.sub_module(h, m)
                    d = k.simplified_module()
                    h = d
                    lt_h, index1 = h.lt_in_module(preff, choice)
                    Flag_r = 1

            if Flag_r == 0 and h != 0:

                lt_h, index1 = h.lt_in_module(preff, choice)
                # ---------------------------------------------
                # r = r + lt(h)
                x = mono()
                x = lt_h
                if index1 == 0:
                    a.poly.append(x)

                elif index1 == 1:
                    b.poly.append(x)

                elif index1 == 2:
                    c.poly.append(x)
                # ------------------------------------------------
                # h = h - lt(h)
                w = Poly()
                u = Poly()
                l = Poly()
                w.poly.append(x)
                l = h.module[index1]
                u.sub(l, w)
                u.simplified()
                h.module[index1] = u
                lt_h, index1 = h.lt_in_module(preff, choice)

        return r

    def groebner_modules(self, F, preff, choice):
        """
        f = [ f1, f2, ...., fn ]
        where fi is a module

        """
        g = []
        for i in range(len(F) - 1):
            for j in range(i + 1, len(F)):
                x = [F[i], F[j]]
                lt_fi, index1 = F[i].lt_in_module(preff, choice)
                lt_fj, index2 = F[j].lt_in_module(preff, choice)
                if index1 == index2:
                    g.append(x)

        G = F
        while len(g) != 0:
            random_num = r.randint(0, len(g))
            y = Module()
            y.module = []
            y.s_polynomial_for_modules(g[random_num-1][0], g[random_num-1][1], preff, choice)
            h = Module()
            h.module = []
            h = h.division_in_modules(y, G, preff, choice)
            g.remove(g[random_num - 1])

            if h.isNotEmpty():
                for j in range(len(G)):
                    x = [h, G[j]]
                    lt_h, index1 = h.lt_in_module(preff, choice)
                    lt_gj, index2 = G[j].lt_in_module(preff, choice)
                    if index1 == index2:
                        g.append(x)
                G.append(h)
        return G

    def reduced_grobner_sev_terms(self, G, n):
        q = []
        g = Module()
        g.module = self.module
        print('In part 1')
        print("g ", g.repr_module(g))
        i = 0
        while i < n and g.is_div_by_mod(G):
            i = i+1
            print('In Part 2')
            t11 = mono()
            t21 = mono()
            t31 = mono()
            index11 = 0
            index21 = 0
            index31 = 0
            t11, index11 = g.leader_in_modules(1)
            t21, index21 = g.leader_in_modules(2)
            t31, index31 = g.leader_in_modules(3)
            print('t11 ', t11.repr())
            print('t21 ', t21.repr())
            print('t31 ', t31.repr())
            for j in G:
                t12 = mono()
                t22 = mono()
                t32 = mono()
                index12 = 0
                index22 = 0
                index32 = 0
                t12, index12 = j.leader_in_modules(1)
                t22, index22 = j.leader_in_modules(2)
                t32, index32 = j.leader_in_modules(3)
                print('t12 ', t12.repr())
                print('t22 ', t22.repr())
                print('t32 ', t32.repr())
                if t11.is_divisible_by(t12) and t21.is_divisible_by(t22) and t31.is_divisible_by(t32) and index11 == index12:
                    print('In part 3')

                    m = Module()
                    m.module = []
                    ind = Poly()
                    div = mono()
                    mulP = Poly()
                    k = Module()
                    s = Module()
                    d = Module()
                    for a in j.module:
                        m.module.append(a)
                    ind = j.module[index11]
                    div.monoDiv(t11, t12)
                    mulP = mulP.monoMultPoly(div, ind)
                    index23 = 0
                    index33 = 0
                    t23, index23 = mulP.leader_in_poly(2)
                    t33, index33 = mulP.leader_in_poly(3)
                    if t21.is_divisible_by(t23) and t31.is_divisible_by(t33):
                        m.module[index11] = mulP
                        k = s.sub_module(g, m)
                        d = k.simplified_module()
                        g.module = d.module
                        print('g = ', g.repr_module(g))
                    else:
                        pass
        return g

    def example(self, G, preff, choice):
        """
        an example to test reduced grobner bases wrt several term orderings.
        :param G: A set of Grobner bases
        :param preff: preferrence
        :param choice: choice
        :return: Updated set of Grobner bases.
        """

        print("Grobner Bases wrt term order 1)")
        print("G = (g1, g2, g3)")
        for i in range(3):
            G[i].repr_module(G[i])

        g = []
        for i in range(len(G) - 1):
            for j in range(i + 1, len(F)):
                x = [G[i], G[j]]
                lt_gi, index1 = G[i].lt_in_module(preff, choice)
                lt_gj, index2 = G[j].lt_in_module(preff, choice)
                if index1 == index2:
                    g.append(x)

        while len(g) != 0:
            random_num = r.randint(0, len(g))
            y = Module()
            y.module = []
            y.s_polynomial_for_modules(g[random_num - 1][0], g[random_num - 1][1], preff, choice)
            h = Module()
            h.module = []
            h = y.reduced_grobner_sev_terms(G, 3)
            g.remove(g[random_num - 1])

            if h.isNotEmpty():
                for j in range(len(G)):
                    x = [h, G[j]]
                    lt_h, index1 = h.lt_in_module(preff, choice)
                    lt_gj, index2 = G[j].lt_in_module(preff, choice)
                    if index1 == index2:
                        g.append(x)
                G.append(h)

        print("Grobner Bases wrt term order (1, 2)")
        print("G = (g1, g2, g3, g4)")
        for i in range(4):
            G[i].repr_module(G[i])


choice = int(input('Menu \n 1. TOP (Term over Position)\n 2. POT (Position over Term)'))
m = Poly()
preff = m.preferred()

q = Module()
q.getValuesModules()


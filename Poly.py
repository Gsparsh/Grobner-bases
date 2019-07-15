from mono import mono


class Poly(mono):
    def __init__(self):
        """
        To initialise a polynomial list

        """
        self.poly = []

    def getValuesPoly(self):
        """

        To input degrees of monomials

        """
        self.poly = []
        n = int(input('How many terms?'))
        for i in range(n):
            x = mono()
            x.getValues()
            self.poly.append(x)

    def repr_poly(self,x):
        """

        This function will represent the polynomial

        """
        string = ''
        for i in range(len(x.poly)):
            if x.poly[i].c == 0:
                string = string + str('0')
            else:
                string = string + (x.poly[i].repr())
                if i < (len(x.poly) - 1):
                    string = string + ' + '
        #print(string)
        return string

    def mult(self, poly1, poly2):
        """

        This function returns the result of multiplication of two polynomials


        """
        self.poly=[]
        for i in poly1.poly:
            for j in poly2.poly:
                z = mono()
                z.monoMult(i, j)
                self.poly.append(z)
                print(i.repr(),j.repr(),z.repr())
        self.repr_poly(self)
        return self

    def add(self, first, second):
        """

        This function returns the addition of two polynomials

        """
        i = 0
        j = 0
        self.poly = []
        l1 = len(first.poly)
        l2 = len(second.poly)
        while i < l1 or j < l2:
            if (i < l1 and j < l2) and first.poly[i].x == second.poly[j].x and first.poly[i].y == second.poly[j].y and first.poly[i].z == second.poly[j].z:
                z = mono()
#               first.poly[i].c = first.poly[i].c + second.poly[j].c
                z.monoAdd(first.poly[i], second.poly[j])
                self.poly.append(z)
                i = i+1
                j = j+1

            elif i == l1 or j < l2:
                self.poly.append(second.poly[j])
                j = j+1

            else:
                self.poly.append(first.poly[i])
                i = i+1
        return self

    def sub(self, first, second):
        """

        This function returns the subtraction of two polynomials



        """
        i = 0
        j = 0
        self.poly = []
        l1 = len(first.poly)
        l2 = len(second.poly)

        while i < l1 or j < l2:
            if (i < l1 and j < l2) and first.poly[i].x == second.poly[j].x and first.poly[i].y == second.poly[j].y and first.poly[i].z == second.poly[j].z:
                z = mono()
                #first.poly[i].c = first.poly[i].c - second.poly[j].c
                z.monoSub(first.poly[i], second.poly[j])
                self.poly.append(z)
                i = i+1
                j = j+1

            elif i == l1 and j < l2:
                second.poly[j].c = -1 * second.poly[j].c
                self.poly.append(second.poly[j])
                j = j+1

            else:
                self.poly.append(first.poly[i])
                i = i+1
        return self

    def monoMultPoly(self, first, other):
        """

        :param first: monomial
        :param other: polynomial
        ;return self: polynomial


        This function returns the multiplication of a monomial with a polynomial

        """
        self.poly = []
        for i in other.poly:
            mul = mono()
            mul = mul.monoMult(first, i)
            self.poly.append(mul)
        return self

    def is_div_by_poly(self, other):
        flag = 0
        for i in self.poly:
            for j in other.poly:
                if i.is_divisible_by(j):
                    flag = 1
        if flag == 1:
            return True
        else:
            return False

    def leading_term(self, pref):
        """

        This function returns the leading term of the polynomial


        """

        x = pref[0]
        y = pref[1]
        z = pref[2]

        a = Poly()
        a.poly = []
        for i in range(len(self.poly)):
            lo = mono()
            lo.x = x * self.poly[i].x
            lo.y = y * self.poly[i].y
            lo.z = z * self.poly[i].z
            a.poly.append(lo)

        if self.poly[0].c == 0:
            sum0 = 0
        else:
            sum0 = (a.poly[0].x + a.poly[0].y + a.poly[0].z)

        big = mono()
        big = self.poly[0]

        for i in range(len(a.poly)):
            sum = (a.poly[i].x + a.poly[i].y + a.poly[i].z)

            if sum > sum0 and self.poly[i].c != 0:
                sum0 = sum
                big = self.poly[i]
            else:
                pass
        return big

    def leader_in_poly(self, lead):

        m = mono()
        if lead == 1:
            m = self.leading_term([3, 2, 1])
        elif lead == 2:
            m = self.leading_term([2, 3, 1])
        elif lead == 3:
            m = self.leading_term([1, 2, 3])
        return m

    def preferred(self):

        preference = []
        ch = 0
        while ch == 0:
            ch = int(input('MENU \n Choose 1 to 6 \n1. x > y > z \n2. z > y > x \n3. y > z > x \n'
                           '4. y > x > z \n5. x > z > y \n6. z > x > y '))
            if ch == 1:
                preference = [3, 2, 1]

            elif ch == 2:
                preference = [1, 2, 3]

            elif ch == 3:
                preference = [1, 3, 2]

            elif ch == 4:
                preference = [2, 3, 1]

            elif ch == 5:
                preference = [3, 1, 2]

            elif ch == 6:
                preference = [2, 1, 3]

            else:
                print('Wrong Input!! \n please Enter again!! ')
                ch = 0
        return preference

    def simplified(self):
        """

        This function simplifies the given polynomial

        :return:
        """
        for i in range(len(self.poly) - 1):
            for j in range(i + 1, len(self.poly)):
                if (self.poly[j].x == self.poly[i].x and self.poly[j].z == self.poly[i].z and self.poly[j].y == self.poly[i].y):
                    self.poly[i].c = self.poly[i].c + self.poly[j].c
                    self.poly.remove(self.poly[j])
                    break
        return self

    def multi_divide_list(self, f, F):

        """

        This function divides given f by the set of polynomials called F = { f1, f2, ... , fN}
        This function returns the u1, u2, ..., uN for the polynomials where F = u1.f1 + u2.f2 +..... + uN.fN

        """
        preff = []
        m = Poly()
        preff = m.preferred()
        h = Poly()
        r = Poly()
        U = []
        h.poly = f.poly
        lt_h = mono()
        lt_h = h.leading_term(preff)
        Flagr = 0

        while h.poly != 0:

            for i in F:

                lt_Fi = mono()
                lt_Fi = i.leading_term(preff)
                Flagr = 0
                if lt_h.is_divisible_by(lt_Fi):

                    mulP = Poly()
                    d = Poly()
                    div = mono()
                    div.monoDiv(lt_h, lt_Fi)
                    u = Poly()
                    u.poly.append(div)
                    U.append(u)
                    mulP = mulP.monoMultPoly(div, i)
                    s = Poly()
                    r = Poly()
                    r = s.sub(h, mulP)
                    d = s.simplified()
                    h.poly = d.poly
                    lt_h = h.leading_term(preff)
                    Flagr = 1

                if Flagr == 0 and h != 0:

                    r.poly = h.poly
                    h.poly = 0
                    return False

        return True

    def s_polynomial(self, f, g):
        """

        This function returns the S polynomial of two ploynomials.
        formula used:
        S(f,g) = LCM(lt(f), lt(g))         LCM(lt(f), lt(g))
                ----------------- . f  -   ----------------- . g
                    lt(f)                         lt(g)



        """
        preff = []
        m = Poly()
        preff = m.preferred()
        lt_f = mono()
        lt_f = f.leading_term(preff)
        lt_g = mono()
        lt_g = g.leading_term(preff)
        L = mono()
        L.lcm(lt_f, lt_g)
        t1 = mono()
        t1.monoDiv(L, lt_f)
        t2 = mono()
        t2.monoDiv(L, lt_g)
        T1 = Poly()
        T2 = Poly()
        for i in f.poly:
            v = mono()
            v.monoMult(i, t1)
            T1.poly.append(v)
        for i in g.poly:
            v = mono()
            v.monoMult(i, t2)
            T2.poly.append(v)
        return self.sub(T1, T2)

    def grobner(self,f1,f2):
        """
        For a given example, Grobner bases has been generated.

        Grobner bases are:
        x^2.0*y^1.0*z^0.0 + *z^1.0
        x^1.0*y^0.0*z^1.0 + y^1.0*z^
        0-1.0*z^2.0 + x^1.0*y^2.0*z^0.0
        0y^-1.0*z^ + 0y^2.0*z^

        """
        g = [f1, f2]
        f3 = Poly()
        f3.s_polynomial(f2, f1)
        g.append(f3)
        f4 = Poly()
        f4.s_polynomial(f1, f3)
        f5 = Poly()
        f5.s_polynomial(f2, f3)
        g.append(f5)
        f6 = Poly()
        f6.s_polynomial(f4, f1)
        f7 = Poly()
        f7.s_polynomial(f4, f2)
        f8 = Poly()
        f8.s_polynomial(f4, f3)
        print('G are:')
        for i in g:
            i.repr_poly(i)

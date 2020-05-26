import math


class Mono:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.c = 0
        self.id = 0
        self.x1 = 0
        self.y1 = 0
        self.x1_c = 0
        self.y1_c = 0
        self.a1 = 0
        self.a2 = 0

    def get_values(self):
        """
        self is for constants
        :return: constant monomial
        """
        self.id = int(input('Enter identity:'))
        self.x = int(input('Enter power of x:'))
        self.y = int(input('Enter power of y:'))
        self.c = int(input('Enter Coeff:'))

    def get_alpha_values(self):
        """
        self is for alpha values
        :return: alpha monomial
        """

        self.id = int(input('Enter identity:'))
        self.a1 = int(input('Enter power of a1:'))
        self.a2 = int(input('Enter power of a2:'))

    def represent(self):
        """
        self is for constants
        :return: string
        """
        if self.c == 0:
            string = str('0')
            return string
        if self.x1 != 0 and self.y1 != 0:
            string = str(self.c) + '*x^' + str(self.x) + '*y^' + str(self.y) + '(y+' + str(self.y1_c) + ')^' + str(self.y1) + '(x+' + str(self.x1_c) + ')^' + str(self.x1)
            return string
        elif self.x1 != 0 and self.y1 == 0:
            string = str(self.c) + '*x^' + str(self.x) + '*y^' + str(self.y) + '(x+' + str(self.x1_c) + ')^' + str(self.x1)
            return string
        elif self.x1 == 0 and self.y1 != 0:
            string = str(self.c) + '*x^' + str(self.x) + '*y^' + str(self.y) + '(y+' + str(self.y1_c) + ')^' + str(self.y1)
            return string
        else:
            string = str(self.c) + '*x^' + str(self.x) + '*y^' + str(self.y)
            return string

    def represent_both(self, other):
        """
        self is for constants
        :param other is for alpha
        :return: string
        """
        if self.id == other.id:
            if self.c == 0:
                string = str('0')
                return string
            else:
                string = str(self.represent())
                string = string + 'aplha2^' + str(other.a2) + 'aplha1^' + str(other.a1)
                return string
        else:
            print("Error!! alpha and constant have different identity")

    def add_mono(self, first, second):
        """

        :param first: first constant monomial
        :param second: second constant monomial
        :return: result of addition, constant monomial
        """
        if first.x == second.x and first.y == second.y:
            self.x = first.x
            self.y = first.y
            self.c = first.c + second.c
            return self
        else:
            print('It will result in Polynomial')

    def subtract_mono(self, first, second):
        """
        form:   first * second
        :param first: first constant monomial
        :param second: second constant monomial
        :return: result of subtraction, constant monomial
        """
        if first.x == second.x and first.y == second.y:
            self.x = first.x
            self.y = first.y
            self.c = first.c - second.c
            return self
        else:
            print('It will result in Polynomial')

    def multiply_mono(self, first, second):
        """

        :param first: first constant monomial
        :param second: second constant monomial
        :return: result of multiplication, constant monomial
        """
        self.x = first.x + second.x
        self.y = first.y + second.y
        self.c = first.c * second.c
        return self

    def divide_mono(self, first, second):
        """
        form:   first / second
        :param first: first constant monomial
        :param second: second constant monomial
        :return: result of divison, constant monomial
        """
        if second.c == 0:
            self.x = 0
            self.y = 0
            self.c = 0
        else:
            self.x = first.x - second.x
            self.y = first.y - second.y
            self.c = first.c / second.c

        return self

    def add_alpha_mono(self, first, second, third, forth):
        """

        :param first:  first constant monomial
        :param second: second constant monomial
        :param third: first alpha monomial
        :param forth: second alpha monomial
        :return: result of addition, constant monomial and alpha monomial
        """
        if third.a1 == forth.a1 and third.a2 == forth.a2:
            if first.id == third.id and second.id == forth.id:
                self.add_mono(first, second)
            else:
                print("Not possible")

        return self

    def subtract_alpha_mono(self, first, second, third, forth):
        """

        :param first:  first constant monomial
        :param second: second constant monomial
        :param third: first alpha monomial
        :param forth: second alpha monomial
        :return: result of subtraction, constant monomial and alpha monomial
        """
        if third.a1 == forth.a1 and third.a2 == forth.a2:
            if first.id == third.id and second.id == forth.id:
                self.subtract_mono(first, second)
            else:
                print("Not possible")

        return self

    def multiply_alpha_mono(self, other, first, second, third, forth):
        """

        :param other: resultant of alpha monomials
        :param first:  first constant monomial
        :param second: second constant monomial
        :param third: first alpha monomial
        :param forth: second alpha monomial
        :return: self and other result of multiplication, constant monomial and alpha monomial
        """

        if third.a1 == 0 and third.a2 == 0:
            self.multiply_mono(first, second)
            other = forth

        elif third.a1 == 0 and third.a2 != 0:
            self.x = first.x + second.x
            self.y = first.y
            self.y1 = second.y
            self.y1_c = third.a2
            self.c = first.c * second.c
            self.id = second.id
            other.a1 = forth.a1
            other.a2 = third.a2 + forth.a2
            other.id = forth.id

        elif third.a1 != 0 and third.a2 == 0:
            self.x = first.x
            self.x1 = second.x
            self.x1_c = third.a1
            self.y = first.y + second.y
            self.c = first.c * second.c
            self.id = second.id
            other.a1 = third.a1 + forth.a1
            other.a2 = forth.a2
            other.id = forth.id

        elif third.a1 != 0 and third.a2 != 0:
            self.x = first.x
            self.x1 = second.x
            self.x1_c = third.a1
            self.y = first.y
            self.y1 = second.y
            self.y1_c = third.a2
            self.c = first.c * second.c
            self.id = second.id
            other.a1 = third.a1 + forth.a1
            other.a2 = third.a2 + forth.a2
            other.id = forth.id

        return self, other

    def divide_alpha_mono(self, first, second, third, forth):
        """

        :param first:  first constant monomial
        :param second: second constant monomial
        :param third: first alpha monomial
        :param forth: second alpha monomial
        :return: result of division, constant monomial and alpha monomial
        """
        if third.a1 == forth.a1 and third.a2 == forth.a2:
            if first.id == third.id and second.id == forth.id:
                self.divide_mono(first, second)
            else:
                print("Not possible")

        return self

    def lcm(self, first, second):
        """

        :param first: first constant monomial
        :param second: second constant monomial
        :return: lcm of both constant monomials
        """
        if first.x >= second.x:
            self.x = first.x
        else:
            self.x = second.y

        if first.y >= second.y:
            self.y = first.y
        else:
            self.y = second.y

        m = math.gcd(first.c, second.c)
        if m != 0:
            if first.c != 0 and second.c != 0:
                self.c = (first.c * second.c) / m
            elif first.c != 0:
                self.c = first.c
            elif second.c != 0:
                self.c = second.c

        return self

    def gcf(self, first, second):
        """

        :param first: first constant monomial
        :param second: second constant monomial
        :return: gcf of both constant monomials
        """

        self.x = math.gcd(first.x, second.x)
        self.y = math.gcd(first.y, second.y)
        self.c = math.gcd(first.c, second.c)

        return self

    def is_divisible_by(self, other):
        """
        form: a is_divisible_by b
        self is for constant monomial
        :param other: for constant monomial
        :return: true or false
        """

        if self.x >= other.x and self.y >= other.y and self.x1 >= other.x1 and self.y1 >= other.y1:
            return True
        else:
            return False

    def is_alpha_divisible_by(self, other):
        """
        form: a is_divisible_by b
        self is for constant monomial
        :param other: for constant monomial
        :return: true or false
        """

        if self.a1 >= other.a1 and self.a2 >= other.a2:
            return True
        else:
            return False


class Poly(Mono):

    def __init__(self):

        self.poly = []

    def get_values_poly(self):
        """

        :return:
        """

        n = int(input('How many terms?'))
        for i in range(n):
            x = Mono()
            x.get_values()
            self.poly.append(x)

    def get_alpha_values_poly(self):
        """

        :return:
        """

        n = int(input('How many terms?'))
        for i in range(n):
            x = Mono()
            x.get_alpha_values()
            self.poly.append(x)

    def represent_poly(self):
        """

        :return:
        """

        string = ''
        for i in range(len(self.poly)):
            if self.poly[i].c == 0:
                string = string + str('')
            else:
                string = string + str(self.poly[i].represent())
                if i < (len(self.poly) - 1):
                    string = string + str(' + ')
        return string

    def represent_both_poly(self, other):
        """
        self is for constant polynomial
        :param other: for alpha polynomial
        :return:
        """
        flag = 0
        string = ' '
        for i in range(len(other.poly)):
            string = string + 'alpha1^' + str(other.poly[i].a1) + 'alpha2^' + str(other.poly[i].a2)
            string = string + str('(')
            flag = 0
            for j in range(len(self.poly)):
                if other.poly[i].id == self.poly[j].id:
                    if flag == 0:
                        string1 = self.poly[j].represent()
                        string = string + str(string1)
                        flag = 1
                    elif flag == 1:
                        string1 = self.poly[j].represent()
                        string = string + str('+') + str(string1)
            string = string + str(') + ')
        return string

    def add_poly(self, first, second):
        """
        This function returns the addition of two polynomials

        """

        i = 0
        j = 0
        self.poly = []
        l1 = len(first.poly)
        l2 = len(second.poly)
        while i < l1 or j < l2:
            if (i < l1 and j < l2) and first.poly[i].x == second.poly[j].x and first.poly[i].y == second.poly[j].y:
                z = Mono()
                z.add_mono(first.poly[i], second.poly[j])
                self.poly.append(z)
                i = i + 1
                j = j + 1

            elif i == l1 or j < l2:
                self.poly.append(second.poly[j])
                j = j + 1

            else:
                self.poly.append(first.poly[i])
                i = i + 1
        return self

    def subtract_poly(self, first, second):
        """
        This function returns the subtaction of two polynomials

        :param first: constant poly
        :param second: constant poly
        :return: constant poly resultant
        """
        i = 0
        j = 0
        self.poly = []
        l1 = len(first.poly)
        l2 = len(second.poly)

        while i < l1 or j < l2:
            if (i < l1 and j < l2) and first.poly[i].x == second.poly[j].x and first.poly[i].y == second.poly[j].y and \
                    first.poly[i].z == second.poly[j].z:
                z = Mono()
                # first.poly[i].c = first.poly[i].c - second.poly[j].c
                z.subtract_mono(first.poly[i], second.poly[j])
                self.poly.append(z)
                i = i + 1
                j = j + 1

            elif i == l1 and j < l2:
                second.poly[j].c = -1 * second.poly[j].c
                self.poly.append(second.poly[j])
                j = j + 1

            else:
                self.poly.append(first.poly[i])
                i = i + 1
        return self

    def multiply_poly(self, first, second):
        """

        This function returns the result of multiplication of two polynomials


        """
        self.poly=[]
        for i in first.poly:
            for j in second.poly:
                z = Mono()
                z.multiply_mono(i, j)
                self.poly.append(z)
        return self

    def multiply_mono_poly(self, first, other):
        """

        :param first: monomial
        :param other: polynomial
        ;return self: polynomial


        This function returns the multiplication of a monomial with a polynomial

        """
        self.poly = []
        for i in other.poly:
            mul = Mono()
            mul = mul.multiply_mono(first, i)
            self.poly.append(mul)

        return self

    def simplified(self):
        """

        This function simplifies the given polynomial

        :return:
        """
        for i in range(len(self.poly) - 1):
            for j in range(i + 1, len(self.poly)):
                if self.poly[j].x == self.poly[i].x and self.poly[j].y == self.poly[i].y:
                    self.poly[i].c = self.poly[i].c + self.poly[j].c
                    self.poly.remove(self.poly[j])
                    break
        return self

    def add_alpha_poly(self, other, first, second, third, forth):
        """
        self is for resultant constant polynomial
        :param other: for resultant alpha polynomial
        :param first: constant ploynomial
        :param second: constant polynomial
        :param third: alpha polynomial
        :param forth: alpha polynomial
        :return: self, other
        """

        # i represents index of third polynomial
        # j represents index of forth polynomial
        # a represents index of first polynomial
        # b represents index of second polynomial
        # l1 represents length of first polynomial
        # l2 represents length of second polynomial
        # l3 represents length of third polynomial
        # l4 represents length of forth polynomial

        i = 0
        j = 0
        l3 = len(third.poly)
        l4 = len(forth.poly)
        while i < l3 or j < l4:
            if (i < l3 and j < l4) and third.poly[i].a1 == forth.poly[j].a1 and third.poly[i].a2 == forth.poly[j].a2:
                other.poly.append(third.poly[i])
                a = 0
                b = 0
                l1 = len(first.poly)
                l2 = len(second.poly)
                while a < l1 or b < l2:
                    if a == l1 or b < l2:
                        if second.poly[b].id == forth.poly[j].id:
                            second.poly[b].id = third.poly[i].id
                            self.poly.append(second.poly[b])
                            b = b + 1
                        else:
                            b = b + 1
                    elif b == l2 or a < l1:
                        if first.poly[a].id == third.poly[i].id:
                            self.poly.append(first.poly[a])
                            a = a + 1
                        else:
                            a = a + 1
                    elif a < l1 and b < l2:
                        if first.poly[a].id == third.poly[i].id and second.poly[b].id == forth.poly[j].id:
                            if first.poly[a].x == second.poly[b].x and first.poly[a].y == second.poly[b].y:
                                z = Mono()
                                z.add_mono(first.poly[a], second.poly[b])
                                self.poly.append(z)
                                a = a + 1
                                b = b + 1
                            else:
                                self.poly.append(first.poly[a])
                                second.poly[b].id = third.poly[i].id
                                self.poly.append(second.poly[b])
                                a = a + 1
                                b = b + 1
                i = i + 1
                j = j + 1
            elif i == l3 or j < l4:
                other.poly.append(forth.poly[j])
                for s in range(len(second.poly)):
                    if forth.poly[j].id == second.poly[s].id:
                        self.poly.append(second.poly[s])
                j = j + 1
            else:
                other.poly.append(third.poly[i])
                print('KAY')
                for s in range(len(first.poly)):
                    if third.poly[i].id == first.poly[s].id:
                        self.poly.append(first.poly[s])
                i = i + 1
        return self, other

    def subtract_alpha_poly(self, other, first, second, third, forth):
        """
        self is for resultant constant polynomial
        :param other: for resultant alpha polynomial
        :param first: constant ploynomial
        :param second: constant polynomial
        :param third: alpha polynomial
        :param forth: alpha polynomial
        :return: self, other
        """
        # i represents index of third polynomial
        # j represents index of forth polynomial
        # a represents index of first polynomial
        # b represents index of second polynomial
        # l1 represents length of first polynomial
        # l2 represents length of second polynomial
        # l3 represents length of third polynomial
        # l4 represents length of forth polynomial

        i = 0
        j = 0
        l3 = len(third.poly)
        l4 = len(forth.poly)
        print('YO!')
        while i < l3 or j < l4:
            if (i < l3 and j < l4) and third.poly[i].a1 == forth.poly[j].a1 and third.poly[i].a2 == forth.poly[j].a2:
                other.poly.append(third.poly[i])
                a = 0
                b = 0
                l1 = len(first.poly)
                l2 = len(second.poly)
                print('YES!!')
                while a < l1 or b < l2:
                    print('YOYO!!')
                    if a == l1 or b < l2:
                        if second.poly[b].id == forth.poly[j].id:
                            second.poly[b].id = third.poly[i].id
                            second.poly[b].c = -1 * second.poly[b].c
                            self.poly.append(second.poly[b])
                            b = b + 1
                            print('KOKO')
                        else:
                            b = b + 1
                    elif b == l2 or a < l1:
                        if first.poly[a].id == third.poly[i].id:
                            self.poly.append(first.poly[a])
                            a = a + 1
                            print('OK!')
                        else:
                            a = a + 1
                    elif a < l1 and b < l2:
                        if first.poly[a].id == third.poly[i].id and second.poly[b].id == forth.poly[j].id:
                            print('NONO')
                            if first.poly[a].x == second.poly[b].x and first.poly[a].y == second.poly[b].y:
                                print('YAY!')
                                z = Mono()
                                z.subtract_mono(first.poly[a], second.poly[b])
                                self.poly.append(z)
                                a = a + 1
                                b = b + 1
                                print('HO0RAY')

                            else:
                                self.poly.append(first.poly[a])
                                second.poly[b].id = third.poly[i].id
                                self.poly.append(second.poly[b])
                                print('HMM!')
                                a = a + 1
                                b = b + 1
                i = i + 1
                j = j + 1
                print('WOW')
            elif i == l3 or j < l4:
                other.poly.append(forth.poly[j])
                print('NICE')
                for s in range(len(second.poly)):
                    if forth.poly[j].id == second.poly[s].id:
                        self.poly.append(second.poly[s])
                        print('XYZ')
                j = j + 1
            else:
                other.poly.append(third.poly[i])
                print('KAY')
                for s in range(len(first.poly)):
                    if third.poly[i].id == first.poly[s].id:
                        self.poly.append(first.poly[s])
                        print('LOW')
                i = i + 1
            print('IN WHILE')
        print('OUT WHILE')
        return self, other

    def multiply_alpha_poly(self, other, first, second, third, forth):
        """
        self is for resultant constant polynomial
        :param other: for resultant alpha polynomial
        :param first: for constant polynomial
        :param second: for constant polynomial
        :param third: for alpha polynomial
        :param forth: for alpha polynomial
        :return: self, other
        """

    def is_not_empty(self):
        """
        self is for any polynomial
        :return: True or False
        """
        l = len(self.poly)
        if l == 0:
            return False
        else:
            return True

    def multiply_alpha_mono_poly(self, other, first, second, third, forth):
        """
        self is for resultant constant polynomial
        :param other: for resultant alpha polynomial
        :param first: for constant monomial
        :param second: for constant polynomial
        :param third: for alpha monomial
        :param forth: for alpha polynomial
        :return: self, other
        """
        # i represents index for constant polynomial
        # j represents true or false value for other polynomial
        # l1 represents length of constant polynomial

        self.poly = []
        other.poly = []
        i = 0
        k = 0
        l1 = len(forth.poly)
        l2 = len(second.poly)
        print('Hello!')
        while i < l1:
            print('YO')
            while k < l2:
                j = 0
                print('YOYO')
                for a in range(len(second.poly)):
                    print('HO')
                    if forth.poly[i].id == second.poly[a].id:
                        print('HOHO')
                        m = Mono()
                        n = Mono()
                        m.multiply_alpha_mono(n, first, second.poly[a], third, forth.poly[i])
                        self.poly.append(m)
                        if j == 0:
                            other.poly.append(n)
                        j = j + 1
                        k = k + 1
                print('HAHA')
                if j == 0:
                    z = Mono()
                    z.a1 = third.a1 + forth.poly[i].a1
                    z.a2 = third.a2 + forth.poly[i].a2
                    other.poly.append(z)
                i = i + 1
            print('HAHAHA')
            z = Mono()
            z.a1 = third.a1 + forth.poly[i].a1
            z.a2 = third.a2 + forth.poly[i].a2
            other.poly.append(z)
            i = i + 1

        return self, other

    def prefered(self):
        preference = []
        ch = 0
        while ch == 0:
            ch = int(input('MENU \n Choose 1 or 2 \n1. a1 > a2  \n2. a2 > a1 \n'))
            if ch == 1:
                preference = [3, 1]

            elif ch == 2:
                preference = [1, 3]
            else:
                print('Wrong Input!! \n please Enter again!! ')
                ch = 0
        return preference

    def leading_term_poly(self, pref):
        """

        This function returns the leading term of the polynomial

        """

        x = pref[0]
        y = pref[1]
        z = pref[2]

        a = Poly()
        a.poly = []
        for i in range(len(self.poly)):
            lo = Mono()
            lo.x = x * self.poly[i].x
            lo.y = y * self.poly[i].y
            lo.z = z * self.poly[i].z
            a.poly.append(lo)

        if self.poly[0].c == 0:
            sum0 = 0
        else:
            sum0 = (a.poly[0].x + a.poly[0].y + a.poly[0].z)

        big = Mono()
        big = self.poly[0]

        for i in range(len(a.poly)):
            sum = (a.poly[i].x + a.poly[i].y + a.poly[i].z)

            if sum > sum0 and self.poly[i].c != 0:
                sum0 = sum
                big = self.poly[i]
            else:
                pass
        return big

    def alpha_leading_term_poly(self, pref):
        """

        This function returns the leading term of the polynomial


        """
        a1 = pref[0]
        a2 = pref[1]

        a = Poly()
        a.poly = []
        for i in range(len(self.poly)):
            lo = Mono()
            lo.a1 = a1 * self.poly[i].a1
            lo.a2 = a2 * self.poly[i].a2
            a.poly.append(lo)

        sum0 = (a.poly[0].a1 + a.poly[0].a2)

        big = Mono()
        big = self.poly[0]

        for i in range(len(a.poly)):
            sum = (a.poly[i].a1 + a.poly[i].a2)

            if sum > sum0:
                sum0 = sum
                big = self.poly[i]
            else:
                pass
        return big

    def leader_poly(self, lead):

        m = Mono()
        if lead == 1:
            m = self.leading_term_poly([3, 2, 1])
        elif lead == 2:
            m = self.leading_term_poly([2, 3, 1])
        elif lead == 3:
            m = self.leading_term_poly([1, 2, 3])
        return m

    def alpha_leader_poly(self, lead):
        m = Mono()
        if lead == 1:
            m = self.alpha_leading_term([3, 1])
        elif lead == 2:
            m = self.alpha_leading_term([1, 3])
        return m


class Module(Poly):

    def __init__(self):
        """
        To initialize a module list containing zero polynomial
        (Updated)

        """

        self.module = []

    def get_values_modules(self):
        """
        To input polynomials in a module
        (Updated)

        """

        self.module = []
        n = int(input('How many Polynomials ?'))
        for i in range(n):
            print("Enter Details for Polynomial", i + 1)
            p = Poly()
            p.get_values_poly()
            self.module.append(p)

    def represent_module(self, x):

        """
        This function represents a module containing polynomials

        :param x: module to be represented
        :return: string representation of a module
        (Updated)

        """
        string = '( '

        for i in range(len(x.module)):
            if i < len(x.module) - 1:
                string = string + str(x.module[i].represent_poly())
                string = string + str(' , ')
            else:
                string = string + str(x.module[i].represent_poly())
                string = string + str(' )')
        print(string)

    def add_module(self, first, second):
        """
        This function is used to add two modules of equal length.
        :param first: module
        :param second: module
        :return: result module
        (Updated)

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
                p.add_poly(first.module[i], second.module[i])
                self.module.append(p)
        return self

    def subtract_module(self, first, second):
        """
        This function returns the subtraction of one module from another.
        :param first: module
        :param second: module
        :return: result module
        (Updated)

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
                p.subtract_poly(first.module[i], second.module[i])
                self.module.append(p)
        return self

    def multiply_module(self, first, second):
        """
        this function returns the product of two modules.
        :param first: module
        :param second: module
        :return: product of two modules
        (Updated)

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
                p.multiply_poly(first.module[i], second.module[i])
                self.module.append(p)
        return self

    def leading_term_module(self, preff, choice):
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
                    e = Mono()
                    e = self.module[i].leading_term_poly(preff)
                    p.poly.append(e)
                # -----------------------------------------------------------
                m = Mono()
                a = Poly()
                a.poly = []
                for i in range(len(p.poly)):
                    lo = Mono()
                    lo.x = x * p.poly[i].x
                    lo.y = y * p.poly[i].y
                    lo.z = z * p.poly[i].z
                    a.poly.append(lo)

                if p.poly[0].c == 0:
                    sum0 = 0
                else:
                    sum0 = (a.poly[0].x + a.poly[0].y + a.poly[0].z)
                    index = 0
                big = Mono()
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
                char = 0
                while char == 0:

                    char = int(input('Choose any one: \nMenu \n1. First Base at Highest \n2. Last base at Highest'))
                    if char == 1:
                        m = Mono()
                        m = self.module[0].leading_term_poly(preff)
                        return m

                    elif char == 2:
                        l = len(self.module)
                        n = l - 1
                        m = Mono()
                        m = self.module[n].leading_term_poly(preff)
                        return m

                    else:
                        print('Wrong Input!! Try Again ')
                        char = 0
            else:
                print('Wrong Input!! Try Again ')
                ch = 0

    def leader_modules(self, lead):
        """
        (Updated)
        :param lead:
        :return:
        """
        index = 0
        m = Mono()
        if lead == 1:
            m, index = self.leading_term_module([3, 2, 1], 1)
        elif lead == 2:
            m, index = self.leading_term_module([2, 3, 1], 1)
        elif lead == 3:
            m, index = self.leading_term_module([1, 2, 3], 1)
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








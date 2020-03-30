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

    def alpha_leading_term(self, pref):
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







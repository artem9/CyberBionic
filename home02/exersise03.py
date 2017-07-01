class A:
    def my_method(self):
        print('This is A.')


class B(A):
    def mult(self, a, b):
        return 'Multiply a({}) on b({}) = {}'.format(a, b, a * b)


class C(A):
    def my_method(self):
        print('This is C')


class D(C, B):
    def my_method(self):
        print('This is D')

print(A.__mro__)
print(B.__mro__)
print(C.__mro__)
print(D.__mro__)

my_obj = D()
print(my_obj.mult(6, 5))

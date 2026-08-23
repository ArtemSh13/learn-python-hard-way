def print_separator() -> None:
    print('\n===============================================\n')


class Parent1(object):
    def foo(self) -> None:
        print("This is foo() by Parent1.")
        print_separator()


class Parent2(object):
    def foo(self) -> None:
        print("This is foo() by Parent2.")
        print_separator()


class Child1(Parent1):
    def foo(self) -> None:
        print("This is foo() by Child1.")
        print("and...")
        super().foo()
        print_separator()


class Child2(Parent2):
    def foo(self) -> None:
        print("This is foo() by Child2.")
        print("and...")
        super().foo()
        print_separator()


class Child12(Parent1, Parent2):
    def foo(self) -> None:
        print("This is foo() by Child12.")
        print("and...")
        super().foo()
        print_separator()


if __name__ == '__main__':

    p1: Parent1 = Parent1()
    p2: Parent2 = Parent2()

    ch1: Child1 = Child1()
    ch2: Child2 = Child2()
    ch12: Child12 = Child12()

    p1.foo()
    p2.foo()
    ch1.foo()
    ch2.foo()
    ch12.foo()


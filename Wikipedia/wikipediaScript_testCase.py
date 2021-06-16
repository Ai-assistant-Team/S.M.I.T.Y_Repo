from main import Wiki_Search


def test0():
    print('----------\n')
    print(Wiki_Search('Alan Turing'))

def test1():
    print('----------\n')
    print(Wiki_Search(1))

def test2():
    print('----------\n')
    print(Wiki_Search('4'))

def test3():
    print('----------\n')
    print(Wiki_Search(None))

def test4():
    print('----------\n')
    print(Wiki_Search('Alan Tusing'))

def test5():
    print('----------\n')
    print(Wiki_Search("Ritchie Blackmore's Rainbow"))

def test6():
    print('----------\n')
    print(Wiki_Search('Ritchie Blackmors Rainbow'))

def test7():
    print('----------\n')
    print(Wiki_Search(' '))

def test8():
    print('----------\n')
    print(Wiki_Search(''))

def test9():
    print('----------\n')
    print(Wiki_Search(3.14))

def test10():
    print('----------\n')
    print(Wiki_Search('Σκυλος'))

def test11():
    print('----------\n')
    print(Wiki_Search('Σκύλος'))

def test12():
    print('----------\n')
    print(Wiki_Search('pi'))



def test():
    print('----------\n')
    test0()
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()
    test11()
    test12()


test()

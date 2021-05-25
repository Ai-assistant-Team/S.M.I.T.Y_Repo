from main import Youtube_Search


def test0():
    print('----------\n')
    print(Youtube_Search('Alan Turing'))

def test1():
    print('----------\n')
    print(Youtube_Search(1))

def test2():
    print('----------\n')
    print(Youtube_Search('4'))

def test3():
    print('----------\n')
    print(Youtube_Search(None))

def test4():
    print('----------\n')
    print(Youtube_Search('Alan Tusing'))

def test5():
    print('----------\n')
    print(Youtube_Search("Ritchie Blackmore's Rainbow"))

def test6():
    print('----------\n')
    print(Youtube_Search('Ritchie Blackmors Rainbow'))

def test7():
    print('----------\n')
    print(Youtube_Search(' '))

def test8():
    print('----------\n')
    print(Youtube_Search(''))

def test9():
    print('----------\n')
    print(Youtube_Search(3.14))

def test10():
    print('----------\n')
    print(Youtube_Search('Σκυλος'))

def test11():
    print('----------\n')
    print(Youtube_Search('Σκύλος'))

def test12():
    print('----------\n')
    print(Youtube_Search('pi'))



def test():
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

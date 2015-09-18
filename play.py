#!/usr/bin/env python
import sys

# todo create a web page with these options and a right panel for google campaigns
# todo contact us form
# todo publish in hacker news
# todo memcache the page
# todo allow to use admin for adding more functions(similar to dev tools)
# todo allow a user to register so they can create their own functions for running later(private and public)
# todo if previous function was created in public mode then name and website of the person should be displayed
#       in the page


def memoizer(memo, formula):
    def recur(n):
        # print "processing:", n
        if n in memo:
            result = memo[n]
        else:
            result = formula(recur, n)
            memo[n] = result
        return result

    return recur


def fib(recur, n):
    return recur(n - 1) + recur(n - 2)


def fact(recur, n):
    return n * recur(n-1)


def catalan_number(recur, n):
    # C0 = 1
    # Cn+1 = (4*n + 3)*Cn/(n+2)
    # (4*(n-1) + 3)*recur(n-1)/(n-1+2)
    return (4*(n-1) + 3)*recur(n-1)/(n+1)


def compound_interes_gen(r):
    # CIk+1 = 1 + (1+r)*CIk
    def compound_interes(recur, k):
        return 1 + (1+r)*recur(k-1)

    return compound_interes


f = memoizer({0: 1}, fact)
catalan = memoizer({0: 1}, catalan_number)
ci = memoizer({0: 1}, compound_interes_gen(4.2/100))


def print_fac(n):
    v = f(n)
    print n, '=>', v
    print "="*10


def main():
    max_recursion = sys.getrecursionlimit() / 4
    if len(sys.argv) < 2:
        n = 250
    else:
        n = int(sys.argv[1])

    print n / max_recursion
    for i in range(n / max_recursion):
        c = (i+1)*max_recursion
        # print i, c
        f(c)
        catalan(c)
    print_fac(n)

    n = 100
    for i in range(n / max_recursion):
        c = (i+1)*max_recursion
        catalan(c)
    for i in range(n):
        print(catalan(i))
    print catalan(n)
    print "="*20
    for i in range(30):
        print i, ci(i)


if __name__ == '__main__':
    main()



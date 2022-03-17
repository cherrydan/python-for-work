#!/usr/bin/python3
# -*- coding: utf-8 -*-

from countfromby import CountFromBy

def main():
    l = CountFromBy()
    print('l = ', l)
    l.increase()
    print('l++ ', l)
    n = CountFromBy(i=15)
    print('n = ', n)
    print('n.incr = ', n.incr)
    n.increase()
    n.increase()
    print('n (incr x 2) = ', n)

if __name__ == '__main__':
    main()

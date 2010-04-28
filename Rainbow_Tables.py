#!/usr/bin/python
###########################
import time
import os
import sys
import hashlib
##########################
a = '\n''a'
b = '\n''b'
c = '\n''c'
d = '\n''d'
e = '\n''e'
ff = '\n''f'
g = '\n''g'
h = '\n''h'
i = '\n''i'
j = '\n''j'
k = '\n''k'
l = '\n''l'
m = '\n''m'
n = '\n''n'
o = '\n''o'
p = '\n''p'
q = '\n''q'
r = '\n''r'
s = '\n''s'
t = '\n''t'
u = '\n''u'
v = '\n''v'
w = '\n''w'
x = '\n''x'
y = '\n''y'
z = '\n''z'
zero = '\n' + str(0)
one = '\n' + str(1)
two = '\n' + str(2)
three = '\n' + str(3)
four = '\n' + str(4)
five = '\n' + str(5)
six = '\n' + str(6)
seven = '\n' + str(7)
eight = '\n' + str(8)
nine ='\n' +  str(9)
#############################################################################################################################
table = (b + c + d + e + ff + g + h + i + j + k + l + m + n + o + p + q + r + s + t + u + v + w + x + y + z + zero + one + two + three + four + five + six + seven + eight + nine)
#######################################################################################
def Create_Table_1_part1():
                f = file("Test_1_Digit.txt", 'a')
                f.write('a')
                f.close()
###################################################################################
def Create_Table_1_part2():
                f = file("Test_1_Digit.txt", 'a')
                f.write(table)
                f.close()
                os.system('sort -u Test_1_Digit.txt > Test_1_Digit_.txt')
                os.system('rm Test_1_Digit.txt')
###################################################################################
def Create_Table_2(): 
            count = 0
            f = file("Test_1_Digit_.txt", 'r')
            g = file("Test_2_Digit.txt", 'a')
            while count < 36:
                    sads = f.readline()
                    count = count + 1
                    a1 = (str(sads) + str('a'))
                    a2 = (str(sads) + str('b'))
                    a3 = (str(sads) + str('c'))
                    a4 = (str(sads) + str('d'))
                    a5 = (str(sads) + str('e'))
                    a6 = (str(sads) + str('f'))
                    a7 = (str(sads) + str('g'))
                    a8 = (str(sads) + str('h'))
                    a9 = (str(sads) + str('i'))
                    a10 = (str(sads) + str('j'))
                    a11 = (str(sads) + str('k'))
                    a12 = (str(sads) + str('l'))
                    a13 = (str(sads) + str('m'))
                    a14 = (str(sads) + str('n'))
                    a15 = (str(sads) + str('o'))
                    a16 = (str(sads) + str('p'))
                    a17 = (str(sads) + str('q'))
                    a18 = (str(sads) + str('r'))
                    a19 = (str(sads) + str('s'))
                    a20 = (str(sads) + str('t'))
                    a21 = (str(sads) + str('u'))
                    a22 = (str(sads) + str('v'))
                    a23 = (str(sads) + str('w'))
                    a24 = (str(sads) + str('x'))
                    a25 = (str(sads) + str('y'))
                    a26 = (str(sads) + str('z'))
                    a27 = (str(sads) + str('0'))
                    a28 = (str(sads) + str('1'))
                    a29 = (str(sads) + str('2'))
                    a30 = (str(sads) + str('3'))
                    a31 = (str(sads) + str('4'))
                    a32 = (str(sads) + str('5'))
                    a33 = (str(sads) + str('6'))
                    a34 = (str(sads) + str('7'))
                    a35 = (str(sads) + str('8'))
                    a36 = (str(sads) + str('9'))
                    g.write(str(a1))
                    g.write(str(a2))
                    g.write(str(a3))
                    g.write(str(a4))
                    g.write(str(a5))
                    g.write(str(a6))
                    g.write(str(a7))
                    g.write(str(a8))
                    g.write(str(a9))
                    g.write(str(a10))
                    g.write(str(a11))
                    g.write(str(a12))
                    g.write(str(a13))
                    g.write(str(a14))
                    g.write(str(a15))
                    g.write(str(a16))
                    g.write(str(a17))
                    g.write(str(a18))
                    g.write(str(a19))
                    g.write(str(a20))
                    g.write(str(a21))
                    g.write(str(a22))
                    g.write(str(a23))
                    g.write(str(a24))
                    g.write(str(a25))
                    g.write(str(a26))
                    g.write(str(a27))
                    g.write(str(a28))
                    g.write(str(a29))
                    g.write(str(a30))
                    g.write(str(a31))
                    g.write(str(a32))
                    g.write(str(a33))
                    g.write(str(a34))
                    g.write(str(a35))
                    g.write(str(a36))
            else:
                    g.close()
                    os.system('sort -u Test_2_Digit.txt > Test_2_Digit_.txt')
                    os.system('rm Test_2_Digit.txt')
                    print "2 is done."
###################################################################################
def Create_Table_3():
            count = 0
            f = file("Test_2_Digit_.txt", 'r')
            g = file("Test_3_Digit.txt", 'a')
            while count < 1296:
                    sads = f.readline()
                    count = count + 1
                    a1 = (str(sads) + str('a'))
                    a2 = (str(sads) + str('b'))
                    a3 = (str(sads) + str('c'))
                    a4 = (str(sads) + str('d'))
                    a5 = (str(sads) + str('e'))
                    a6 = (str(sads) + str('f'))
                    a7 = (str(sads) + str('g'))
                    a8 = (str(sads) + str('h'))
                    a9 = (str(sads) + str('i'))
                    a10 = (str(sads) + str('j'))
                    a11 = (str(sads) + str('k'))
                    a12 = (str(sads) + str('l'))
                    a13 = (str(sads) + str('m'))
                    a14 = (str(sads) + str('n'))
                    a15 = (str(sads) + str('o'))
                    a16 = (str(sads) + str('p'))
                    a17 = (str(sads) + str('q'))
                    a18 = (str(sads) + str('r'))
                    a19 = (str(sads) + str('s'))
                    a20 = (str(sads) + str('t'))
                    a21 = (str(sads) + str('u'))
                    a22 = (str(sads) + str('v'))
                    a23 = (str(sads) + str('w'))
                    a24 = (str(sads) + str('x'))
                    a25 = (str(sads) + str('y'))
                    a26 = (str(sads) + str('z'))
                    a27 = (str(sads) + str('0'))
                    a28 = (str(sads) + str('1'))
                    a29 = (str(sads) + str('2'))
                    a30 = (str(sads) + str('3'))
                    a31 = (str(sads) + str('4'))
                    a32 = (str(sads) + str('5'))
                    a33 = (str(sads) + str('6'))
                    a34 = (str(sads) + str('7'))
                    a35 = (str(sads) + str('8'))
                    a36 = (str(sads) + str('9'))
                    g.write(str(a1))
                    g.write(str(a2))
                    g.write(str(a3))
                    g.write(str(a4))
                    g.write(str(a5))
                    g.write(str(a6))
                    g.write(str(a7))
                    g.write(str(a8))
                    g.write(str(a9))
                    g.write(str(a10))
                    g.write(str(a11))
                    g.write(str(a12))
                    g.write(str(a13))
                    g.write(str(a14))
                    g.write(str(a15))
                    g.write(str(a16))
                    g.write(str(a17))
                    g.write(str(a18))
                    g.write(str(a19))
                    g.write(str(a20))
                    g.write(str(a21))
                    g.write(str(a22))
                    g.write(str(a23))
                    g.write(str(a24))
                    g.write(str(a25))
                    g.write(str(a26))
                    g.write(str(a27))
                    g.write(str(a28))
                    g.write(str(a29))
                    g.write(str(a30))
                    g.write(str(a31))
                    g.write(str(a32))
                    g.write(str(a33))
                    g.write(str(a34))
                    g.write(str(a35))
                    g.write(str(a36))
            else:
                    g.close()
                    os.system('sort -u Test_3_Digit.txt > Test_3_Digit_.txt')
                    os.system('rm Test_3_Digit.txt')
                    print "3 is done."
###################################################################################
def Create_Table_4():
            count = 0
            f = file("Test_3_Digit_.txt", 'r')
            g = file("Test_4_Digit.txt", 'a')
            while count < 46656:
                    sads = f.readline()
                    count = count + 1
                    a1 = (str(sads) + str('a'))
                    a2 = (str(sads) + str('b'))
                    a3 = (str(sads) + str('c'))
                    a4 = (str(sads) + str('d'))
                    a5 = (str(sads) + str('e'))
                    a6 = (str(sads) + str('f'))
                    a7 = (str(sads) + str('g'))
                    a8 = (str(sads) + str('h'))
                    a9 = (str(sads) + str('i'))
                    a10 = (str(sads) + str('j'))
                    a11 = (str(sads) + str('k'))
                    a12 = (str(sads) + str('l'))
                    a13 = (str(sads) + str('m'))
                    a14 = (str(sads) + str('n'))
                    a15 = (str(sads) + str('o'))
                    a16 = (str(sads) + str('p'))
                    a17 = (str(sads) + str('q'))
                    a18 = (str(sads) + str('r'))
                    a19 = (str(sads) + str('s'))
                    a20 = (str(sads) + str('t'))
                    a21 = (str(sads) + str('u'))
                    a22 = (str(sads) + str('v'))
                    a23 = (str(sads) + str('w'))
                    a24 = (str(sads) + str('x'))
                    a25 = (str(sads) + str('y'))
                    a26 = (str(sads) + str('z'))
                    a27 = (str(sads) + str('0'))
                    a28 = (str(sads) + str('1'))
                    a29 = (str(sads) + str('2'))
                    a30 = (str(sads) + str('3'))
                    a31 = (str(sads) + str('4'))
                    a32 = (str(sads) + str('5'))
                    a33 = (str(sads) + str('6'))
                    a34 = (str(sads) + str('7'))
                    a35 = (str(sads) + str('8'))
                    a36 = (str(sads) + str('9'))
                    g.write(str(a1))
                    g.write(str(a2))
                    g.write(str(a3))
                    g.write(str(a4))
                    g.write(str(a5))
                    g.write(str(a6))
                    g.write(str(a7))
                    g.write(str(a8))
                    g.write(str(a9))
                    g.write(str(a10))
                    g.write(str(a11))
                    g.write(str(a12))
                    g.write(str(a13))
                    g.write(str(a14))
                    g.write(str(a15))
                    g.write(str(a16))
                    g.write(str(a17))
                    g.write(str(a18))
                    g.write(str(a19))
                    g.write(str(a20))
                    g.write(str(a21))
                    g.write(str(a22))
                    g.write(str(a23))
                    g.write(str(a24))
                    g.write(str(a25))
                    g.write(str(a26))
                    g.write(str(a27))
                    g.write(str(a28))
                    g.write(str(a29))
                    g.write(str(a30))
                    g.write(str(a31))
                    g.write(str(a32))
                    g.write(str(a33))
                    g.write(str(a34))
                    g.write(str(a35))
                    g.write(str(a36))
            else:
                    g.close()
                    os.system('sort -u Test_4_Digit.txt > Test_4_Digit_.txt')
                    os.system('rm Test_4_Digit.txt')
                    print "4 is done."
###################################################################################
def Create_Table_5():
            count = 0
            f = file("Test_4_Digit_.txt", 'r')
            g = file("Test_5_Digit.txt", 'a')
            while count < 1679616:
                    sads = f.readline()
                    count = count + 1
                    a1 = (str(sads) + str('a'))
                    a2 = (str(sads) + str('b'))
                    a3 = (str(sads) + str('c'))
                    a4 = (str(sads) + str('d'))
                    a5 = (str(sads) + str('e'))
                    a6 = (str(sads) + str('f'))
                    a7 = (str(sads) + str('g'))
                    a8 = (str(sads) + str('h'))
                    a9 = (str(sads) + str('i'))
                    a10 = (str(sads) + str('j'))
                    a11 = (str(sads) + str('k'))
                    a12 = (str(sads) + str('l'))
                    a13 = (str(sads) + str('m'))
                    a14 = (str(sads) + str('n'))
                    a15 = (str(sads) + str('o'))
                    a16 = (str(sads) + str('p'))
                    a17 = (str(sads) + str('q'))
                    a18 = (str(sads) + str('r'))
                    a19 = (str(sads) + str('s'))
                    a20 = (str(sads) + str('t'))
                    a21 = (str(sads) + str('u'))
                    a22 = (str(sads) + str('v'))
                    a23 = (str(sads) + str('w'))
                    a24 = (str(sads) + str('x'))
                    a25 = (str(sads) + str('y'))
                    a26 = (str(sads) + str('z'))
                    a27 = (str(sads) + str('0'))
                    a28 = (str(sads) + str('1'))
                    a29 = (str(sads) + str('2'))
                    a30 = (str(sads) + str('3'))
                    a31 = (str(sads) + str('4'))
                    a32 = (str(sads) + str('5'))
                    a33 = (str(sads) + str('6'))
                    a34 = (str(sads) + str('7'))
                    a35 = (str(sads) + str('8'))
                    a36 = (str(sads) + str('9'))
                    g.write(str(a1))
                    g.write(str(a2))
                    g.write(str(a3))
                    g.write(str(a4))
                    g.write(str(a5))
                    g.write(str(a6))
                    g.write(str(a7))
                    g.write(str(a8))
                    g.write(str(a9))
                    g.write(str(a10))
                    g.write(str(a11))
                    g.write(str(a12))
                    g.write(str(a13))
                    g.write(str(a14))
                    g.write(str(a15))
                    g.write(str(a16))
                    g.write(str(a17))
                    g.write(str(a18))
                    g.write(str(a19))
                    g.write(str(a20))
                    g.write(str(a21))
                    g.write(str(a22))
                    g.write(str(a23))
                    g.write(str(a24))
                    g.write(str(a25))
                    g.write(str(a26))
                    g.write(str(a27))
                    g.write(str(a28))
                    g.write(str(a29))
                    g.write(str(a30))
                    g.write(str(a31))
                    g.write(str(a32))
                    g.write(str(a33))
                    g.write(str(a34))
                    g.write(str(a35))
                    g.write(str(a36))
            else:
                    g.close()
                    os.system('sort -u Test_5_Digit.txt > Test_5_Digit_.txt')
                    os.system('rm Test_5_Digit.txt')
                    print "5 is done."			
####################################################################################
def Create_Table_6():
            count = 0
            f = file("Test_5_Digit_.txt", 'r')
            g = file("Test_6_Digit.txt", 'a')
            while count < 60466176:
                    sads = f.readline()
                    count = count + 1
                    a1 = (str(sads) + str('a'))
                    a2 = (str(sads) + str('b'))
                    a3 = (str(sads) + str('c'))
                    a4 = (str(sads) + str('d'))
                    a5 = (str(sads) + str('e'))
                    a6 = (str(sads) + str('f'))
                    a7 = (str(sads) + str('g'))
                    a8 = (str(sads) + str('h'))
                    a9 = (str(sads) + str('i'))
                    a10 = (str(sads) + str('j'))
                    a11 = (str(sads) + str('k'))
                    a12 = (str(sads) + str('l'))
                    a13 = (str(sads) + str('m'))
                    a14 = (str(sads) + str('n'))
                    a15 = (str(sads) + str('o'))
                    a16 = (str(sads) + str('p'))
                    a17 = (str(sads) + str('q'))
                    a18 = (str(sads) + str('r'))
                    a19 = (str(sads) + str('s'))
                    a20 = (str(sads) + str('t'))
                    a21 = (str(sads) + str('u'))
                    a22 = (str(sads) + str('v'))
                    a23 = (str(sads) + str('w'))
                    a24 = (str(sads) + str('x'))
                    a25 = (str(sads) + str('y'))
                    a26 = (str(sads) + str('z'))
                    a27 = (str(sads) + str('0'))
                    a28 = (str(sads) + str('1'))
                    a29 = (str(sads) + str('2'))
                    a30 = (str(sads) + str('3'))
                    a31 = (str(sads) + str('4'))
                    a32 = (str(sads) + str('5'))
                    a33 = (str(sads) + str('6'))
                    a34 = (str(sads) + str('7'))
                    a35 = (str(sads) + str('8'))
                    a36 = (str(sads) + str('9'))
                    g.write(str(a1))
                    g.write(str(a2))
                    g.write(str(a3))
                    g.write(str(a4))
                    g.write(str(a5))
                    g.write(str(a6))
                    g.write(str(a7))
                    g.write(str(a8))
                    g.write(str(a9))
                    g.write(str(a10))
                    g.write(str(a11))
                    g.write(str(a12))
                    g.write(str(a13))
                    g.write(str(a14))
                    g.write(str(a15))
                    g.write(str(a16))
                    g.write(str(a17))
                    g.write(str(a18))
                    g.write(str(a19))
                    g.write(str(a20))
                    g.write(str(a21))
                    g.write(str(a22))
                    g.write(str(a23))
                    g.write(str(a24))
                    g.write(str(a25))
                    g.write(str(a26))
                    g.write(str(a27))
                    g.write(str(a28))
                    g.write(str(a29))
                    g.write(str(a30))
                    g.write(str(a31))
                    g.write(str(a32))
                    g.write(str(a33))
                    g.write(str(a34))
                    g.write(str(a35))
                    g.write(str(a36))
            else:
                    g.close()
                    os.system('sort -u Test_6_Digit.txt > Test_6_Digit_.txt')
                    os.system('rm Test_6_Digit.txt')
                    print "6 is done."			
####################################################################################
def Create_Table_7():
            count = 0
            f = file("Test_6_Digit_.txt", 'r')
            g = file("Test_7_Digit.txt", 'a')
            while count < 2176782336:
                    sads = f.readline()
                    count = count + 1
                    a1 = (str(sads) + str('a'))
                    a2 = (str(sads) + str('b'))
                    a3 = (str(sads) + str('c'))
                    a4 = (str(sads) + str('d'))
                    a5 = (str(sads) + str('e'))
                    a6 = (str(sads) + str('f'))
                    a7 = (str(sads) + str('g'))
                    a8 = (str(sads) + str('h'))
                    a9 = (str(sads) + str('i'))
                    a10 = (str(sads) + str('j'))
                    a11 = (str(sads) + str('k'))
                    a12 = (str(sads) + str('l'))
                    a13 = (str(sads) + str('m'))
                    a14 = (str(sads) + str('n'))
                    a15 = (str(sads) + str('o'))
                    a16 = (str(sads) + str('p'))
                    a17 = (str(sads) + str('q'))
                    a18 = (str(sads) + str('r'))
                    a19 = (str(sads) + str('s'))
                    a20 = (str(sads) + str('t'))
                    a21 = (str(sads) + str('u'))
                    a22 = (str(sads) + str('v'))
                    a23 = (str(sads) + str('w'))
                    a24 = (str(sads) + str('x'))
                    a25 = (str(sads) + str('y'))
                    a26 = (str(sads) + str('z'))
                    a27 = (str(sads) + str('0'))
                    a28 = (str(sads) + str('1'))
                    a29 = (str(sads) + str('2'))
                    a30 = (str(sads) + str('3'))
                    a31 = (str(sads) + str('4'))
                    a32 = (str(sads) + str('5'))
                    a33 = (str(sads) + str('6'))
                    a34 = (str(sads) + str('7'))
                    a35 = (str(sads) + str('8'))
                    a36 = (str(sads) + str('9'))
                    g.write(str(a1))
                    g.write(str(a2))
                    g.write(str(a3))
                    g.write(str(a4))
                    g.write(str(a5))
                    g.write(str(a6))
                    g.write(str(a7))
                    g.write(str(a8))
                    g.write(str(a9))
                    g.write(str(a10))
                    g.write(str(a11))
                    g.write(str(a12))
                    g.write(str(a13))
                    g.write(str(a14))
                    g.write(str(a15))
                    g.write(str(a16))
                    g.write(str(a17))
                    g.write(str(a18))
                    g.write(str(a19))
                    g.write(str(a20))
                    g.write(str(a21))
                    g.write(str(a22))
                    g.write(str(a23))
                    g.write(str(a24))
                    g.write(str(a25))
                    g.write(str(a26))
                    g.write(str(a27))
                    g.write(str(a28))
                    g.write(str(a29))
                    g.write(str(a30))
                    g.write(str(a31))
                    g.write(str(a32))
                    g.write(str(a33))
                    g.write(str(a34))
                    g.write(str(a35))
                    g.write(str(a36))
            else:
                    g.close()
                    os.system('sort -u Test_7_Digit.txt > Test_7_Digit_.txt')
                    os.system('rm Test_7_Digit.txt')
                    print "7 is done."
###################################################################################
def Menu_part1():
    print '-----------------'
    print '1-Generate-Tables'
    print '2-Hash-Tables----'
    print '3-Search-Tables--'
    print '4-BruteForcer----'
    print '5-About----------'
    print '-----------------'
###################################################################################
def Menu_part2():
    choice = (str(raw_input("Input:")))
    if choice == str('1'):
	    Generate_Tables()
    elif choice == str('2'):
	    Hash_Tables()
    elif choice == str('3'):
	    Search_Tables()
    elif choice == str('4'):
	    BruteForcer()
    elif choice == str('5'):
	    About()
###################################################################################
def Generate_Tables():
    print "Must be on Linux for this."
    time.sleep(1)
    print "How many chacters long do you want?"
    time.sleep(1)
    print "All possible combos for 1,2,3,4,5,6, or 7 chacters long."
    time.sleep(1)
    print "Lowercase a-z, and 0-9 are ONLY supported."
    tables = (str(raw_input("Input:")))
    if tables == str('1'):
        print "This will take up less than 1kilobyte of space."
        time.sleep(2)
        print "Estimate time to take: 1 second."
        Create_Table_1_part1()
        Create_Table_1_part2()
        print "Converting to Hashable file."
        os.system('cat Test_1_Digit_.txt > Table_To_Hash.txt')
        print "Done."
    elif tables == str('2'):
        print "This will take up 3.9 kilobytes of space."
        print "Estimate time to take: 2 seconds."
        Create_Table_1_part1()
        Create_Table_1_part2()
        Create_Table_2()
        print "Converting to Hashable file."
        os.system('cat Test_1_Digit_.txt > Table_To_Hash.txt')
        os.system('cat Test_2_Digit_.txt >> Table_To_Hash.txt')
        print "Done."
    elif tables == str('3'):
        print "This will take up 186 kilobytes of space."
        print "Estimated time to take: 3 seconds."
        Create_Table_1_part1()
        Create_Table_1_part2()
        Create_Table_2()
        Create_Table_3()
        print "Converting to Hashable file."
        os.system('cat Test_1_Digit_.txt > Table_To_Hash.txt')
        os.system('cat Test_2_Digit_.txt >> Table_To_Hash.txt')
        os.system('cat Test_3_Digit_.txt >> Table_To_Hash.txt')
        print "Done."
    elif tables == str('4'):
        print "This will take up 8.2 megabytes." 
        print "Estimated time to take: 17 seconds."
        Create_Table_1_part1()
        Create_Table_1_part2()
        Create_Table_2()
        Create_Table_3()
        Create_Table_4()
        print "Converting to Hashable file."
        os.system('cat Test_1_Digit_.txt > Table_To_Hash.txt')
        os.system('cat Test_2_Digit_.txt >> Table_To_Hash.txt')
        os.system('cat Test_3_Digit_.txt >> Table_To_Hash.txt')
        os.system('cat Test_4_Digit_.txt >> Table_To_Hash.txt')
        print "Done."
    elif tables == str('5'):
        print "This will take up 350 megabytes."
        print "Estimated time to take 15-30 mins."
        time.sleep(2)
        Create_Table_1_part1()
        Create_Table_1_part2()
        Create_Table_2()
        Create_Table_3()
        Create_Table_4()
        Create_Table_5()
        print "Converting to Hashable file."
        os.system('cat Test_1_Digit_.txt > Table_To_Hash.txt')
        os.system('cat Test_2_Digit_.txt >> Table_To_Hash.txt')
        os.system('cat Test_3_Digit_.txt >> Table_To_Hash.txt')
        os.system('cat Test_4_Digit_.txt >> Table_To_Hash.txt')
        os.system('cat Test_5_Digit_.txt >> Table_To_Hash.txt')
        print "Done."
    elif tables == str('6'):
        print "This will take up 14.7 gigabytes."
        print "Estimated time to take 1-3 hours."
        time.sleep(2)
        Create_Table_1_part1()
        Create_Table_1_part2()
        Create_Table_2()
        Create_Table_3()
        Create_Table_4()
        Create_Table_5()
        Create_Table_6()
        print "Converting to Hashable file."
        os.system('cat Test_1_Digit_.txt > Table_To_Hash.txt')
        os.system('cat Test_2_Digit_.txt >> Table_To_Hash.txt')
        os.system('cat Test_3_Digit_.txt >> Table_To_Hash.txt')
        os.system('cat Test_4_Digit_.txt >> Table_To_Hash.txt')
        os.system('cat Test_5_Digit_.txt >> Table_To_Hash.txt')
        os.system('cat Test_6_Digit_.txt >> Table_To_Hash.txt')
        print "Done." 
    else:
        print "Please enter I number between 1-6."
###################################################################################
def Hash_Tables():
    print "Hash into,"
    time.sleep(.7)
    print "--------------------"
    print "1-MD5---------------"
    print "2-SHA1--------------"
    print "3-SHA224------------"
    print "4-SHA256------------"
    print "5-SHA384------------"
    print "6-SHA512------------"
    print "7-Rot13-------------" #Hehe. 
    print "--------------------"
    choice = (str(raw_input("Input:")))
    if choice == str('1'):
        MD5()
    elif choice == str('2'):
        SHA1()
    elif choice == str('3'):
        SHA224()
    elif choice == str('4'):
        SHA256()
    elif choice == str('5'):
        SHA384()
    elif choice == str('6'):
        SHA512()
    elif choice == str('7'):
        ROT13()
    else:
        print "Please input I number between 1-7."
###################################################################################
def MD5():
    count = 0
    if os.path.exists("Table_To_MD5.txt"):
        os.remove("Table_To_MD5.txt")
    f = file("Table_To_Hash.txt", 'r')
    g = file("Table_To_MD5.txt", 'a')
    c = f.readline()
    cc = c.replace('\n','')
    hashy = hashlib.md5(str(cc)).hexdigest()
    g.write(cc + ' = ' + hashy)
    while count < 61000000: 
        count = count + 1           
        s = f.readline()
        ss = s.replace('\n','')
        hash_brown = hashlib.md5(str(ss)).hexdigest()
        if hash_brown == 'd41d8cd98f00b204e9800998ecf8427e':
            print "Done."
            break
        g.write('\n' + ss + ' = ' + hash_brown)
    else:
        f.close()
        g.close()
        print "Done."
################################################################################
def SHA1():
    if os.path.exists("Table_To_SHA1.txt"):
        os.remove("Table_To_SHA1.txt")
    count = 0                                   
    f = file("Table_To_Hash.txt", 'r')
    g = file("Table_To_SHA1.txt", 'a')
    c = f.readline()
    cc = c.replace('\n','')
    hashy = hashlib.sha1(str(cc)).hexdigest()
    g.write(cc + ' = ' + hashy)
    while count < 61000000: 
        count = count + 1           
        s = f.readline()
        ss = s.replace('\n','')
        hash_brown = hashlib.sha1(str(ss)).hexdigest()
        if hash_brown == 'da39a3ee5e6b4b0d3255bfef95601890afd80709':
            print "Done."
            break
        g.write('\n' + ss + ' = ' + hash_brown)
    else:
        f.close()
        g.close()
        print "Done."
################################################################################
def SHA224():
    if os.path.exists("Table_To_SHA224.txt"):
        os.remove("Table_To_SHA224.txt")
    count = 0                                   
    f = file("Table_To_Hash.txt", 'r')
    g = file("Table_To_SHA224.txt", 'a')
    c = f.readline()
    cc = c.replace('\n','')
    hashy = hashlib.sha224(str(cc)).hexdigest()
    g.write(cc + ' = ' + hashy)
    while count < 61000000: 
        count = count + 1           
        s = f.readline()
        ss = s.replace('\n','')
        hash_brown = hashlib.sha224(str(ss)).hexdigest()
        if hash_brown == 'd14a028c2a3a2bc9476102bb288234c415a2b01f828ea62ac5b3e42f':
            print "Done."
            break
        g.write('\n' + ss + ' = ' + hash_brown)
    else:
        f.close()
        g.close()
        print "Done."
################################################################################
def SHA256():
    count = 0                                   
    f = file("Table_To_Hash.txt", 'r')
    g = file("Table_To_SHA256.txt", 'a')
    c = f.readline()
    cc = c.replace('\n','')
    hashy = hashlib.sha256(str(cc)).hexdigest()
    g.write(cc + ' = ' + hashy)
    while count < 61000000: 
        count = count + 1           
        s = f.readline()
        ss = s.replace('\n','')
        hash_brown = hashlib.sha256(str(ss)).hexdigest()
        if hash_brown == 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855':
            print "Done."
            break
        g.write('\n' + ss + ' = ' + hash_brown)
    else:
        f.close()
        g.close()
        print "Done."
################################################################################
def SHA384():
    if os.path.exists("Table_To_SHA384.txt"):
        os.remove("Table_To_SHA384.txt")
    count = 0                                   
    f = file("Table_To_Hash.txt", 'r')
    g = file("Table_To_SHA384.txt", 'a')
    c = f.readline()
    cc = c.replace('\n','')
    hashy = hashlib.sha384(str(cc)).hexdigest()
    g.write(cc + ' = ' + hashy)
    while count < 61000000: 
        count = count + 1           
        s = f.readline()
        ss = s.replace('\n','')
        hash_brown = hashlib.sha384(str(ss)).hexdigest()
        if hash_brown == '38b060a751ac96384cd9327eb1b1e36a21fdb71114be07434c0cc7bf63f6e1da274edebfe76f65fbd51ad2f14898b95b':
            print "Done."
            break
        g.write('\n' + ss + ' = ' + hash_brown)
    else:
        f.close()
        g.close()
        print "Done."
################################################################################
def SHA512():
    if os.path.exists("Table_To_SHA384.txt"):
        os.remove("Table_To_SHA384.txt")
    count = 0                                   
    f = file("Table_To_Hash.txt", 'r')
    g = file("Table_To_SHA512.txt", 'a')
    c = f.readline()
    cc = c.replace('\n','')
    hashy = hashlib.sha512(str(cc)).hexdigest()
    g.write(cc + ' = ' + hashy)
    while count < 61000000: 
        count = count + 1           
        s = f.readline()
        ss = s.replace('\n','')
        hash_brown = hashlib.sha512(str(ss)).hexdigest()
        if hash_brown == 'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e':
            print "Done."
            break
        g.write('\n' + ss + ' = ' + hash_brown)
    else:
        f.close()
        g.close()
        print "Done."
################################################################################
def Search_Tables():
    global encrypt
    print "What table is to be search?"
    time.sleep(1)
    print "--------------------"
    print "1-MD5---------------"
    print "2-SHA1--------------"
    print "3-SHA224------------"
    print "4-SHA256------------"
    print "5-SHA384------------"
    print "6-SHA512------------"
    print "7-Rot13-------------" #Rot13,was just more for small space, nothing more.
    print "--------------------"
    choice = (str(raw_input("Input:")))
    if choice == str('1'):
       encrypt = (str('MD5'))
       Uni_Table_Search()
    elif choice == str('2'):
       encrypt = (str('SHA1'))
       Uni_Table_Search()
    elif choice == str('3'):
       encrypt = (str('SHA224'))
       Uni_Table_Search()
    elif choice == str('4'):
       encrypt = (str('SHA256'))
       Uni_Table_Search()
    elif choice == str('5'):
       encrypt = (str('SHA384'))
       Uni_Table_Search()
    elif choice == str('6'):
       encrypt = (str('SHA512'))
       Uni_Table_Search()
    elif choice == str('7'):
       encrypt = (str('ROT13'))
       Uni_Table_Search()
    else:
        print "Please input I number between 1-7."
################################################################################
def Uni_Table_Search():
    count = 0
    print (("Table_To_") + (str(encrypt)) + (".txt"))
    if not os.path.exists(("Table_To_") + (str(encrypt)) + (".txt")):
        print "It seems file is not there, Please go generate and encrypt it."
    else:
        f = file(("Table_To_") + (str(encrypt)) + (".txt"))
        Hash = (str(raw_input("Input_Hash:")))
        while count < 61000000:
            a = f.readline()
            aa = a.find(Hash)
            if not aa == (-1):
                print a
                break
            else:
                "Couldnt be found."

################################################################################    
Menu_part1()
Menu_part2()

#from math import *

def pf(a, nn):
    nn = nn + 1
    print("result " + str(n) + ":\n" + str(a))
    print("=======================")
    return nn


n = 0

valid_parm1 = True
valid_parm2 = True

input_num1 = input("num1: ")

if input_num1.isalpha():
    valid_parm1 = False

input_op = input("+-/*: ")
input_num2 = input("num2: ")

if input_num2.isalpha():
    valid_parm2 = False

print("=====>>> Start <<<=====")
tot = 0

if valid_parm1 & valid_parm2 :
        if input_op == "+":
            tot = float(input_num1) + float(input_num2)
        if input_op == "-":
            tot = float(input_num1) - float(input_num2)
        if input_op == "*":
            tot = float(input_num1) * float(input_num2)
        if input_op == "/":
            tot = float(input_num1) / float(input_num2)
n = pf(input_num1 + " " + input_op + " " + input_num2 + " = " + str(round(tot, 5)), n)

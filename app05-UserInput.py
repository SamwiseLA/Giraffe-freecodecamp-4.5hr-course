def pf(a, n):
    n = n + 1
    print("result " + str(n) + ":\n"+ str(a))
    print("=======================")
    return n

n=0

input_user_name = input("Enter Your Name: ")
input_user_age = input("Enter Your Age: ")

print("=====>>> Start <<<=====")

n=pf("Hey there, " + input_user_name +"!\nI see you're " + input_user_age + " years old.",n)

def hello_python():
    print("Hello Python")

hello_python() # fonksiyonu çağırıyoruz 

# parametreli 

print("*******************")

def hello_param(name):
    print("Hello",name)

inputName = input("Enter ur name: ")
hello_param(inputName)

print("*******************")

def summation(num1,num2):
    return num1 + num2 

sum_result = summation(10,20)
print(sum_result)

# args - parametre sayısını girmeden istediğin kadar parametre verme 
def args_example(*args):
    print(args)

args_example(10,20,30)
args_example("a","b","c",True,3.14,2,65,1)

print("*******************")



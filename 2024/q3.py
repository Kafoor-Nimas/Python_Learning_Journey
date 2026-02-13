def generate_fibonacci(n):
    fibonacci_list = []

    a,b=0,1

    for i in range(n):
        fibonacci_list.append(a)
        a,b=b,a+b
    return fibonacci_list

#main program
n=int(input("Enter number of terms: "))
result=generate_fibonacci(n)

print("Fibonacci series: ")
for num in result:
    print(num, end=" ")
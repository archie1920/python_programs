
def fib(n):
   if type(n) != int:
       raise TypeError("n must be a positive int")
   if n < 0:
       raise TypeError("n must be positive int")

   if n == 0:
      return 0
   elif n == 1:
      return 1
   else:
      return fib(n - 1) + fib(n - 2)


def main():
    # check if the number of terms is valid
    num = input("Enter the number for the Fibonacci series: ")
    print("The Fibonacci series of first", num, "numbers is:")

    for x in range(0, int(num)):
        #print(n, ":", fib(x))
        print(fib(x),end=",")

if __name__ =='__main__':
    main()

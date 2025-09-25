def add_numbers(a, b):
   return a + b
def subtract_numbers(a, b):
   return a - b
def multiply_numbers(a, b):
   return a * b
def divide_numbers(a, b):
   if b == 0:
       return "Error: Division by zero"
   return a / b
if __name__ == "__main__":
   print("Simple Calculator App")
   print("1. Add")
   print("2. Subtract")
   print("3. Multiply")
   print("4. Divide")
   choice = int(input("Enter choice (1-4): "))
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))
   if choice == 1:
       print("Result:", add_numbers(num1, num2))
   elif choice == 2:
       print("Result:", subtract_numbers(num1, num2))
   elif choice == 3:
       print("Result:", multiply_numbers(num1, num2))
   elif choice == 4:
       print("Result:", divide_numbers(num1, num2))
   else:
       print("Invalid choice")

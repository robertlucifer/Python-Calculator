from art import logo
from replit import clear
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations={
  '+':add,
  '-':subtract,
  '*':multiply,
  '/':divide
}
def calculator():
  print(logo)
  value1=float(input("What's the first number?: "))
  for x in operations:
    print(x)
  should_continue=True
  while should_continue: 
    operation=input("Enter the operation you want to perform")
    value2=float(input("What's the next number?: "))
    function=operations[operation]
    answer=function(value1,value2)
    print(f"{value1} {operation} {value2}={answer}")
    what=input(f"Type 'y' to continue  calculating with the {answer}, Type 'n' to start a new calculation, or Type 'stop' to stop the entire process")
    if what=='y':
      value1=answer
    elif what=='n':
      should_continue=False
      clear()
      calculator()
    else:
      should_continue=False
calculator()
def main():
    #write your code below this line
    first = int(input("Give the first number:"))
    second = int(input("Give the second number:"))

    if first > second:
      greatest = first
      print("Greater number is: " + str(greatest))
    elif second > first:
      greatest = second
      print("Greater number is: " + str(greatest))
    else:
      print("The numbers are equal!")

if __name__ == '__main__':
    main()

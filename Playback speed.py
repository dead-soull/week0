def main():
    str = input()
    print(replacer(str))

def replacer(n):
    return n.replace(" ", "...")

main()

#This might not work the right way, but it still works so I'm happy with that

#Type This is CS50 and press Enter. Your program should output:
#This...is...CS50    
#Type This is our week on functions and press Enter. Your program should output:
#This...is...our...week...on...functions
#Type Let's implement a function called hello and press Enter. Your program should output:
#Let's...implement...a...function...called...hello
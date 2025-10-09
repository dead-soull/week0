c = 300000000
csquared = pow(c, 2)

def main():
    number = int(input("m: "))
    print(SpeedOfLight(number))
    

def SpeedOfLight(number):
    return (number * csquared)

main()


#Type 1 and press Enter. Your program should output:
#90000000000000000
#Type 14 and press Enter. Your program should output:
#1260000000000000000
#Type 50 and press Enter. Your program should output
#4500000000000000000
    
import InsectClass as I

def main():
    wings = int(input("How many wings does the insect have?"))
    legs = int(input("How many legs does the insect have?"))
    
    mosquito = I.insect(2,4)
    horsefly = I.insect(3,6)


    mosquito.flight_length()
    horsefly.flight_length()

    print("The mosquito can fly: ", mosquito.get_flight(), "miles")
    print("The horsefly can fly: ", horsefly.get_flight(), "miles")


 

main()
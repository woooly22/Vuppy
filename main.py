#Naming

def primernaming():
    strain1 = int(input("Hello, welcome to Vuppy. Please select your strain (use the corresponding number). "
                        "1.p4c2 \n 2.p3c2 \n 3.p2c2 \n 4.p3c2 \n 5.p2c3 \n 6. I don't know my strain."))

    if strain1 == 1:
        primernum = 4

    elif strain1 == 2 or strain1 == 4:
        primernum = 3

    elif strain1 == 6:
        primernum = int(input("What is your total number of primers? (max 4)"))

    else:
        primernum = 2

    #we're retrieving the number of primers here, so we shoudl 
    return [strain1, primernum]

def ctrlnaming (strain1:int)-> int:
    
    if strain1 == 4 or strain1 == 5: #or strain1 == :
        ctrlnum = 3

    else:
        ctrlnum = 2
    return ctrlnum

def tubenum():
    #tubenum input
    tailnum = int(input("What is your total number of tails?"))

    bonusnum = tailnum/10
    round(bonusnum)

    tubenum = tailnum ++ ctrlnum ++ bonusnum

    print("Your total number of tails is:", tailnum,
        "\n Your total number of ctrls is:", ctrlnum,
        "\n Your total number of bonus is:", bonusnum,
        "\n Your total number of tubes is:", tubenum,
                )


#DON'T FUCKING TOUCH SHIT BELOW HERE

#calculations
#totalmix = tubenum * 50
#emerald = tubenum * 25
#dna = tubenum * 4

#prints
#print("\nHere are your mastermix volumes:")
#print("Emerald:", emerald, "ul.")
#print("DNA:", dna, "ul.")

#if primernum == 1:
    #primers = tubenum * .5
    #Print("Primer:", primers, "ul.")
#else:
    #primers = (tubenum * .5) * primernum
    #print("Primers:", primers, "ul total,(", primers/primernum, "ul per primer.)")

#ddh20 = print("ddH20:", totalmix - (emerald + dna + primers), "ul.")
#print("Your total volume is:", totalmix, "ul.")
#print("\nThank you for using Vuppy.")

def main():
    primer_strain = primernaming()
    ctrlnum = ctrlnaming(primer_strain[0])
    #tubenum()

if __name__ == "__main__":
    main()

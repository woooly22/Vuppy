#Naming
strain1 = int(input("Hello, welcome to Vuppy. Please select your strain (use the corresponding number). "
                    "1.p4c2 \n 2.p3c2 \n 3.p2c2 \n 4.p3c2 \n 5.p2c3 \n 6. I don't know my strain."))

def primernaming()-> int():
    global primernum
    if strain1 == 1:
        primernum = 4

    elif strain1 == 2 or strain1 == 4:
        primernum = 3

    elif strain1 == 6:
        primernum = int(input("What is your total number of primers? (max 4)"))

    else:
        primernum = 2

primernaming()
def ctrlnaming ()-> int():
    global ctrlnum
    if strain1 == 4 or strain1 == 5 or strain1 == :
        ctrlnum = 3

    else:
        ctrlnum = 2
4.00
5.00
7.00
8.00
10.00
11.00
12.00
13.00
18.00
21.00
25.00
26.00
27.00
31.00

ctrlnaming()

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

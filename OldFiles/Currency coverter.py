with open('rates.txt') as txt:
    lines = txt.readlines()
currency = {}
for line in lines:
    parsed = line.split("\t")
    currency[parsed[0]] = parsed[1]

a = input("Enter the ammount in INR\n")
print("Type the currnecy you want to convert rupees to.Type exatly as below list. To convert to multiple currencies, type the currency name seprated by comma")
[print(x) for x in currency.keys()]
print("****************************************************")
converto = input().split(",")
for curr in converto:
    print(f"{a} INR to {curr} : {float(a) * float(currency[curr])}")
input("Press any key to close")


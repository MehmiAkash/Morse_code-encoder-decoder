# 0: -----
# 1: .----
# 2: ..---
# 3: ...--
# 4: ....-
# 5: .....
# 6: -....
# 7: --...
# 8: ---..
# 9: ----.

number= input("Enter the number to convert into morse code: ")


def numeric_morse_encoder(number):
    morse_encoded = ""
    for i in number:
        x = int(i)
        n = 5
        if x <= 5:
            sign1 = "."
            sign2 = "-"
        else:
            x = x - n
            sign1 = "-"
            sign2 = "."
        for j in range(0, x):
            morse_encoded += sign1
        for i in range(0, n - x):
            morse_encoded += sign2
        morse_encoded += " "
    return morse_encoded

def numeric_morse_decoded(encoded):
    morse_decoded=""
    x = ""
    for i in encoded:

        if i==" ":

            sign1=0#sign = .
            sign2=0#sign = -
            if x[0]==".":
                cnt=0
            else :
                cnt=1
            for j in x:
                if(j=="."):
                    sign1+=1
                else:
                    sign2+=1
            if cnt==0:
                morse_decoded+=f"{sign1}"
            elif sign2==5:
                morse_decoded+="0"
            else:
                morse_decoded+=f"{5+sign2}"
            x=""
        else:
            x+=i
    return morse_decoded


encoded=numeric_morse_encoder(number)
decoded= numeric_morse_decoded(encoded)
print(f"Morse code Encoded number {encoded}")
print(f"Morse code Decoded number {decoded}")


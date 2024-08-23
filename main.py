# I used International morse format
morse=[  "-----",  ".----",  "..---",  "...--",  "....-",  ".....",  "-....",  "--...",  "---..",  "----."
       ,".-","-...","-.-.","-..",".","..-.","--.","....",
       "..",".---","-.-",".-..","--","-.","---",".--.",
       "--.-",".-.","...","-","..-","...-",".--","-..-",
       "-.--","--.."]
#first 10 elements of morse array represent numbers from 0 to 10
def morse_encoder(word_ascii,key):
       morse_encoded=""
       for i in word_ascii:
              if i == 32:  # ASCII value for space
                     morse_encoded+=" "  # Single space for a gap between letters, will be handled below
              elif i < 97:
                     morse_encoded+=morse[i - 48]
              else:
                 morse_encoded+=morse[i-key]
              morse_encoded += " "
       return morse_encoded

def morse_decoder(encoded,key):
       word=""
       temp=""
       encoded = encoded.replace("   ","  ")  #triple spaces will be two spaces
       for i in encoded:
              if i == " ":
                     if temp:
                            if morse.index(temp) < 10:
                                   word += chr(morse.index(temp) + 48)  # For numbers
                            else:
                                   word += chr(morse.index(temp) + key)  # For letters
                            temp = ""
                     elif word and word[-1] != " ":
                            word += " "  # Add space between words
              else:
                     temp += i
       if temp:  # Handling the last Morse code segment
              if morse.index(temp) < 10:
                     word += chr(morse.index(temp) + 48)
              else:
                     word += chr(morse.index(temp) + key)
       return word

#chr()
word_input=input("Enter the word to covert into morse code : ").lower()
#for upper case key is 65-10
#for lower case key is 97-10
key=87
word_ascii=[]
for i in word_input:
       word_ascii.append(ord(i))

print(word_ascii)

encoded = morse_encoder(word_ascii,key)
decoded= morse_decoder(encoded,key)
print(f"Morse encoded text: {encoded}")
print(f"Morse decoded text: {decoded}")

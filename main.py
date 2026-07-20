# ==============================================================
# Project      : Morse Code Translator
# Author       : Ardhan
# Version      : 1.0 (July 2026)
# Description  : Automatic bi-directional Morse code translator
# ==============================================================

# project 12
# i got a really good idea for my next project
# a morse code

alphabet_to_morse = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': '/'
}

print("=" * 50)
print("📡 AUTOMATIC MORSE CODE TRANSLATOR")
print("   Version 1.0.0 | Developer: Ardhan")
print("=" * 50)
print("[Status] Auto-detect system is active.")
print("[Manual] Enter plain text OR Morse code (use '.' and '-').")
print("[Action] Type 'exit' to close the program.")
print("-" * 50) 

    # SWAPPING SISTEM
morse_to_alphabet = {value: key for key, value in alphabet_to_morse.items()} 
# short cut
    
while True:
    
    user_input = input("\n\nEnter text or Morse code (type 'exit' to quit): ").strip()

    if user_input.lower() == 'exit':
        print("\n[System] Thank you for using my morse translator. Goodbye!")
        break
        
    translated_result = ""

    # MORSE TO ALPHABET    
    if user_input.startswith(".") or user_input.startswith("-"):
        morse_split = user_input.split(" ")
        
        for code in morse_split:
            if code in morse_to_alphabet:
                translated_result += morse_to_alphabet[code]
            else:
                translated_result += code
                
        print(f"\nTranslate to Alphabet: {translated_result}")

    # ALPHABET TO MORSE    
    else:
        user_input = user_input.lower()
        
        for char in user_input:
            if char in alphabet_to_morse:
                translated_result += alphabet_to_morse[char] + " "
            else:
                translated_result += char
                
        print(f"\nTranslate to morse code: {translated_result}")       
     
# 12 juli 2026
# completed

# 18 juli 2026 
# i changed it to english and make it looks
# more professional to upload it to Git hub

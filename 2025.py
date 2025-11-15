import base64

hex_string = "54 68 65 54 72 00 75 74 68 49 1A 73 4E 7F 65 61 72"
# remove spaces, convert hex string to bytes
hex_string = hex_string.replace(" ", "")
message_bytes = bytes.fromhex(hex_string)

# keep only printable ASCII characters
printable_bytes = [b for b in message_bytes if 32 <= b <= 126]

#print characters
for b in printable_bytes:
    print(chr(b), end = "")
print("")

#m3
base64_string = "MjMwMDAwLTMxMS0xMTU="
decoded_bytes = base64.b64decode(base64_string)
decoded_string = decoded_bytes.decode('utf-8')
print(decoded_string)

#m4
nums = "178, 150, 38, 118, 150, 230, 22, 46, 130, 46, 46, 134, 198, 214, 12, 140, 44, 172".split(", ")
binary = [format(int(n), "08b") for n in nums] #pads to 8 bits because for some reason it doesn't work otherwise!!!!
reversed_binary = [b[::-1] for b in binary]
ascii_chars = [chr(int(b, 2)) for b in reversed_binary]
print("".join(ascii_chars))

#m5
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}
morse = "-.. .. ....- .--. ..... -... -. --- .--. .... --.- -... -.. ..-.".split(" ")

decoded = ""
for code in morse:
    for letter, pattern in morse_code.items():
        if pattern == code: #looking up keys from dict morse_code
            decoded += letter
            break

shifted = ""
for ch in decoded:
    if 'A' <= ch <= 'Z': #apply cipher to letters
        shifted += chr(((ord(ch) - ord('A') - 1) % 26) + ord('A'))
    else: #but not numbers!
        shifted += ch

print(shifted)







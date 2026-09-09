'''
Morse Code
Given a Morse code string, return the decoded message using the following table:

Code	Letter	Code	Letter
.-	A	-.	N
-...	B	---	O
-.-.	C	.--.	P
-..	D	--.-	Q
.	E	.-.	R
..-.	F	...	S
--.	G	-	T
....	H	..-	U
..	I	...-	V
.---	J	.--	W
-.-	K	-..-	X
.-..	L	-.--	Y
--	M	--..	Z
Letters are separated by a single space
Words are separated by three spaces

'''


def decode_morse(code):
    morse_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z'
    }
    morse_code = code.strip()

    words = morse_code.split('   ')
    decoded_words = []

    for word in words:
        print(word)
        letters = word.split(' ')
        decoded_letters = []
        for letter in letters:
            if letter:
                decoded_letters.append(morse_dict[letter])
        decoded_words.append(''.join(decoded_letters))

    result = ' '.join(decoded_words)
    print(result)
    code = result
    return code


t = decode_morse("... --- ...")
print(t)

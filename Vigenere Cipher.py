import math
#import sys
#What would you say you do here?
Action = str(raw_input("Encoding or Decoding: "))
#Get the input key
Keyword = str(raw_input("Key: "))
#Get the input (de/en)coding text
if Action == 'Encoding':
    Encoding = str(raw_input("Text to Encode: "))
    n = math.floor(len(Encoding) / len(Keyword))
    m = len(Encoding) % len(Keyword)
elif Action == 'Decoding':
    Encoded = str(raw_input("Encoded text: "))
    n = math.floor(len(Encoded) / len(Keyword))
    m = len(Encoded) % len(Keyword)
#repeat the key to the length of the coded text
Keyword = Keyword * int(n) + Keyword[0:int(m)]
#set up the dictionaries
decoding1 = {
	'a' : 0,
	'b' : 1,
	'c' : 2,
	'd' : 3,
	'e' : 4,
	'f' : 5,
	'g' : 6,
	'h' : 7,
	'i' : 8,
	'j' : 9,
	'k' : 10,
	'l' : 11,
	'm' : 12,
	'n' : 13,
	'o' : 14,
	'p' : 15,
	'q' : 16,
	'r' : 17,
	's' : 18,
	't' : 19,
	'u' : 20,
	'v' : 21,
	'w' : 22,
	'x' : 23,
	'y' : 24,
	'z' : 25
}
decoding2 = {
	0 : 'a', 
	1 : 'b', 
	2 : 'c',
	3 : 'd',
	4 : 'e',
	5 : 'f',
	6 : 'g',
	7 : 'h',
	8 : 'i',
	9 : 'j',
	10 : 'k',
	11 : 'l',
	12 : 'm',
	13 : 'n',
	14 : 'o',
	15 : 'p',
	16 : 'q',
	17 : 'r',
	18 : 's',
	19 : 't',
	20 : 'u',
	21 : 'v',
	22 : 'w',
	23 : 'x',
	24 : 'y',
	25 : 'z'
}
value = []
#print converted values of the key
if Action[0:len(Action)] == 'Decoding':
    for i in range(len(Keyword)):
        value.append(decoding2[((int(decoding1[Encoded[i]]) - decoding1[Keyword[i]])% 26)])
elif Action[0:len(Action)] == 'Encoding':
    for i in range(len(Keyword)):
        value.append(decoding2[((int(decoding1[Encoding[i]]) + decoding1[Keyword[i]])% 26)])   
value = ''.join(value)
print value
raw_input()

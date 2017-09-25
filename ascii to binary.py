word=input("Enter the text you want to be converted ")[:1000000]
no_spaces=True
for x in range(0,len(word)):
  letter=word[x]
  if letter==" ":
    output="00100000"
  elif letter=="!":
    output="00100001"
  elif letter=='"':
    output="00100010"
  elif letter=="'":
    output="00100111"
  elif letter=="#":
    output="00100011"
  elif letter=="$":
    output="00100100"
  elif letter=="£":
    output="10100011"
  elif letter=="%":
    output="00100101"
  elif letter=="&":
    output="00100110"
  elif letter=="(":
    output="00111001"
  elif letter==")":
    output="00110000"
  elif letter=="*":
    output="00101010"
  elif letter=="-":
    output="00101101"
  elif letter==",":
    output="00101100"
  elif letter==":":
    output="00111010"
  elif letter==";":
    output="00111011"
  elif letter=="<":
    output="00111100"
  elif letter==">":
    output="00111110"
  elif letter=="/":
    output="00101111"
  elif letter=="^":
    output="01011110"
  elif letter=="+":
    output="00101011"
  elif letter=="=":
    output="00111101"
  elif letter=="@":
    output="01000000"
  elif letter=="_":
    output="01011111"
  elif letter=="?":
    output="00111111"
  elif letter==".":
    output="00101110"
  elif letter.islower():
    letter_binary=bin(ord(letter)-96)[2:]
    start_binary="011"
    for x in range(0,5-len(letter_binary)):
      start_binary=start_binary+"0"
    output=start_binary+str(letter_binary)
  else:
    letter_binary=bin(ord(letter)-64)[2:]
    start_binary="010"
    for x in range(0,5-len(letter_binary)):
      start_binary=start_binary+"0"
    output=start_binary+str(letter_binary)
  if no_spaces==False:
    print(output, end=' ')
  else:
    print(output, end='')

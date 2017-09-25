word=input("Enter your word")
for x in range(0,len(word)):
  letter=word[x]
  if letter.islower():
    letter_binary=bin(ord(letter)-96)[2:]
    start_binary="011"
    for x in range(0,5-len(letter_binary)):
      start_binary=start_binary+"0"
    output=start_binary+str(letter_binary)
    print(output, end=' ')
  else:
    letter_binary=bin(ord(letter)-64)[2:]
    start_binary="010"
    for x in range(0,5-len(letter_binary)):
      start_binary=start_binary+"0"
    output=start_binary+str(letter_binary)
    print(output, end='')
print("")
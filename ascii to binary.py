word=input("Enter the text you want to be converted ")

# oof what was that
out = ""
for ch in word:
  out = out + " " + bin(ord(ch))
print("Binary: ")
print(out)

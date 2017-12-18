word=input("Enter the text you want to be converted ")

# oof what was that
out = ""
for ch in word:
  out = out + " 0" + bin(ord(ch))[2:].zfill(8)
print("Binary: ")
print(out)

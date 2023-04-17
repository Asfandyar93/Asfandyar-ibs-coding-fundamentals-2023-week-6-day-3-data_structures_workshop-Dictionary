# Create a map with the following key-value pairs:

phone_book_map = {
    "William A. Lathan": "405-709-1865",
    "John K. Miller": "402-247-8568",
    "Hortensia E. Foster": "606-481-6467",
    "Amanda D. Newland": "319-243-5613",
    "Brooke P. Askew": "307-687-2982"
}

# Create an application which prints out the answers to the following questions:
# What is John K. Miller's phone number?
print(phone_book_map.get("John K. Miller"))

# Whose phone number is 307-687-2982?
for name, phone in phone_book_map.items():
    if phone == "307-687-2982":
        print(name)
        break

# Do we know Chris E. Myers' phone number? (yes/no)?
if "Chris E. Myers" in phone_book_map:
    print("Yes")
else:
    print("No")
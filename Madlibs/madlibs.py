# # How to put string together (string concatenation)
# # Create a string that says "follow my  ________"
# instagram = "@syhmiisade"

# # simple idea or ways
# # 1
# print("follow my ig " + instagram)

# #2 Adding any value of instagram inside the curly braces {}
# print("follow my ig {}".format(instagram))  

# #3 Same concept as the number 2
# print(f"follow my ig {instagram}")

# ctrl forward slash (to comment many line) ------------------------------------------------------

# I am using method 3 for this project
# I make this in malay btw

person1 = input("watak 1: ")
person2 = input("watak 2: ")
place1 = input("lokasi 1: ")
food1 = input("makanan 1 : ")
food2 = input("makanan 2 : ")
food3 = input("makanan 3 : ")
things1 = input("barang mahal : ")

madlib = f"Pada suatu hari, {person1} sedang menaiki basikal menuju {place1}. Tiba tiba, dia terserempak dengan {person2}. \
{person2} sedang memancing dengan tenang sambil melihat jorannya. {person1} bertanya kepada {person2}.'Oiii manoi ikan nya?' bertanya {person1}.\
'Mana laa aku tahu. Agak nya dia tengah pancing cacing kot' kata {person2}. Tergelak {person1} mendengar balas {person2}. {person1} meneruskan \
perjalanan nya menuju {place1}. Sampai di {place1}, {person1} sepatutnya membeli {food1}, {food2}, dan {food3} untuk makan malam nya. Apakan daya,\
{person1} terlupa apa yang perlu dibeli. Setelah melihat barang-barang di {place1}, {person1} membeli {things1} sahaja dan pulang ke rumah."

print(madlib)
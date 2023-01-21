#           FILE FOR TESTING FEW CONCEPTS TO AVOID ERRORS..





# Extract rating from the string..

star = "5.0 out of 5 stars"
rating = star.split("out")[0].strip()
print(rating)
print(type(rating))
rating = float(rating)
print(rating)
print(type(rating))

print("\{U+2730}")

#def get_variant(product, review):
#    variant = review.find('span', {'data-hook': 'format-strip-linkless'})
#    product_name = product
#    size = "Not Available"
#    colour = "Not Available"
    # Filtering the 'None' type data..

product = "Apple iPhone 12 (64GB) - (Product) RED"
product1 = "Colour: Space BlackSize: 256 GB"
variant = None

if variant != None:
    variant = variant.text
    temp, product_name = str(variant).split("Pattern name: ")
    temp, size = temp.split("Size: ")
    temp, colour = temp.split("Colour: ")
elif variant == None:
    product_name, size, colour = product.split('(')
    product_name = product_name.strip() + " (Generated_from_Title)"
    size = size.split(')')[0].strip() + " (Generated_from_Title)"
    colour = colour.split(')')[-1].strip() + " (Generated_from_Title)"

if "Apple" in product:
    response = product.index("iPhone")

print(response)

print(product_name, " | ", size, " | ", colour)

a = "Xiaomi 12 Pro  5G (Opera Muave, 12GB RAM, 256GB Storage) Snapdragon 8 Gen 1  50+50+50MP Flagship Cameras (OIS)  10bit 2K+ Curved AMOLED Display  Sound by Harman Kardon(Product Page, Visited on January 20 2023, 23-50-07).csv"
print(len(a))
print(a[0:50])
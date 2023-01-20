# Extract rating from the string..

'''star = "5.0 out of 5 stars"
rating = star.split("out")[0].strip()
print(rating)
print(type(rating))
rating = float(rating)
print(rating)
print(type(rating))

print("\{U+2730}")'''

#def get_variant(product, review):
#    variant = review.find('span', {'data-hook': 'format-strip-linkless'})
#    product_name = product
#    size = "Not Available"
#    colour = "Not Available"
    # Filtering the 'None' type data..

product = "Apple iPhone 12 (64GB) - (Product) RED"
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

print(product_name, " | ", size, " | ", colour)
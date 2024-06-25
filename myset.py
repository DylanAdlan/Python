# set uses {}
# set is modifiable (add, edit and delete)
# set is unordered (not retain its position)
# set set is not indexed
# set does not allow duplicate values

x = {10, 20, 20, 30, 40}
print("Values in set:", x)

# from output, we ot that in set
# 1) numbers is not in same order
# 2) duplicate numbers is missing

# selection and indexing
# since set is not indexed, we cannot 
# retriev values using [] syntax
# to retrieve them from set
# use for loop
print("To retrieve values in set using for loop")
for i in x:
    print(i, end=" ")

print("="*40)

# modifiable
print("Original set values")
fruits = {"apple", "orange", "mango"}
print(fruits)
fruits.add("durian") # add durian randomly in set
# which cannot be used in list (bcs list is ordered)
print("="*40)

print("Add() => after added durian in the set")
print(fruits)

print("="*40)

# to delete an item in the set
print("Remove() => remove orange item in the set")
fruits.remove("orange")
print(fruits)

print("="*40)

# pop => randomly remove an item in the set
print("Pop() => remove randomly in the item")
fruits.pop()
print(fruits)


flowers = ["dahlia", "sunflower", "daffodil", "roses", "roses"]
unique = set(flowers)
print(unique)

overseafruits = {"apple", "orange", "mango", "banana", "grapes"}
localfruits = {"durian", "rambutan", "cempedak", "banana", "mangosteen"}
print(f"Union: {overseafruits.union(localfruits)}") # union
print(f"Intersection: {overseafruits.intersection(localfruits)}") # intersection
print(f"Oversea difference local: {overseafruits.difference(localfruits)}") # intersection
print(f"Local difference oversea: {localfruits.difference(overseafruits)}") # intersection

favfruits = {"durian", "rambutan", "mangosteen"}
print(f"Is fav fruits subset local: {favfruits.issubset(localfruits)}") # intersection
print(f"Is fav fruits superset local: {localfruits.issuperset(favfruits)}") # intersection
print(f"Is fav fruits disjoint oversea: {favfruits.isdisjoint(overseafruits)}") # intersection

emailcontent = """Phishing is a type of online scam that targets 
consumers by sending them an e-mail that appears to be from a well-known source
an internet service provider, a bank, or a mortgage company, for example. It 
asks the consumer to provide personal identifying information. 
Then a scammer uses the information to open new accounts, or 
invade the consumers existing accounts. There are several tips that consumers can follow to avoid phishing scams, 
such as not responding to e-mails or pop-up messages that ask for personal or financial information."""

print(len(emailcontent))
words = emailcontent.split()
print(len(words))

uniques = set(words)
print(uniques)


cleanwords = []
for word in words: 
    # words is instance of string class / word is a string object
    # remove is a method inside the word object
    # remove takes 2 arguments 
    # first arguments is used to find
    # second argument is to replace
    word = word.replace(",", "") # replace comma(,) to empty 
    word = word.replace(".", "") # replace dot(.) to empty 
    word = word.lower() # convert to lowercase
    cleanwords.append(word)

uniques = set(cleanwords)
print(len(uniques))

print(uniques)

commonwords = {"is", "or", "of", "so", "by", "how", "when", "it", "on"\
               , "the", "into", "a", "to", "is", "are", "what", "be", \
                "i", "you", "more", "and", "can", "an"}

uniques = uniques.difference(commonwords)
print(uniques)
print(len(uniques))


spamwords = {"tricked", "trick", "phishing", "security", "criminals"}
howmanyspamworddowehave = uniques.intersection(spamwords)
print(len(howmanyspamworddowehave))



    
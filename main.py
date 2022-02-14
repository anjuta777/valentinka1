a = input("Ievadiet skolēnu vidējo atzīmes: ")
sentence = "Extract 10 , 9 , 8 from this string"
a = [int(a) for in str.split(sentence) if a.isdigit()]
print(a)
sentence1 = "Extract 7 , 6, 5 , 4 from this string"
b = [int(a)for in str.split(sentence1) if a.isdigit()]
print(b)
sentence2 = "Extract 3 , 2 , 1 from this string"
c = [int(a)for in str.split(sentence2) if a.isdigit()]
print(c)
def get_number_of_elements (list):
   count = 0
   for element in list:
       count += 1
    return count
    
print("Number of elements in the list: "), get_number_of_elements(a))


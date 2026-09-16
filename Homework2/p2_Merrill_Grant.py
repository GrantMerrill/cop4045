# Grant Merrill --- Z23813057

# === Problem 2: Comprehensions ===
print("Grant Merrill --- Z23813057")
# === Part a ===
distinct = [(a, b, c, d) 
            for a in range(1, 11) 
            for b in range(1, 11) 
            for c in range(1, 11) 
            for d in range(1, 11) 
            if (a**2 + b**2 == c**2 + d**2)
            and len({a, b, c, d}) == 4]

print("\nResults of Part A:")
print(distinct)
print(len(distinct))

# === Part b ===
example = ['One', 'SEVEN', 'three', 'two', 'Ten']

result = [(x.lower(), len(x)) 
          for x in example 
          if len(x) < 5]

print("\nResults of Part B:")
print(result)

# === Part c ===
names = ['Christopher Ashton Kutcher', 'Elizabeth Stamatina Fey']

result = [f"{name.split()[0]} {name.split()[1][0]}. {name.split()[2]}" 
          for name in names]

print("\nResults of Part C:")
print(result)

# === Part d ===
lst1 = ["Spam", "Trams", "Elbows", "Tops", "Astral"]
lst2 = ["Bowels", "Sample", "Altars", "Stop", "Course", "Smart"]

result = [(w1, w2) 
          for w1 in lst1 
          for w2 in lst2 
          if sorted(w1.lower()) == sorted(w2.lower())]

print("\nResults of Part D:")
print(result)

# === Part e ===
s = ['one', 'two', 'three']

result = {n: len(n) 
          for n in s}

print("\nResults of Part E:")
print(result)

# === Part f ===
text = "Hello World"
vowels = "aeiou"

result = {i: c for i,c in enumerate(text) if c.lower() in vowels}

print("\nResults of Part F:")
print(result)
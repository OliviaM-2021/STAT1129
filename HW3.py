# question 0
marks = {'Andy':88, 'Amy':66, 'James': 90, 'Jules': 55, 'Arthur': 77}

# question 1
for name in marks:
    print(name, marks[name])
    scores = marks.values()
 
# question 2
# mean
print(sum(scores)/len(scores))
# max
print(max(scores))
# min
print(min(scores))

# question 3
for key in marks:
    if 'J' in key:
      break
    print(key)
    
# question 4
for key in marks:
    if 'J' in key:
      continue
    print(key)
    
# question 5
def function(name):
    if name in marks:
        return marks[name]
    else:
        print("you cannot find this student’s name")

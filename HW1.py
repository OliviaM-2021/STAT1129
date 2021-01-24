# question1
my_favorite_colors =["red","blue","white","teal","black"]
print(type(my_favorite_colors))
print(my_favorite_colors)

# question2
nums = list(range(30,61,3))
print(nums)

# question3
weather = {"Sunny":"play","rainy":"watching TV","Cloudy":"walk"}
print(type(weather))
print(weather)

weather.update({"snowy":"ski"})
print(weather)

# question4
def grade(score):
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    else:
        print("F")
       

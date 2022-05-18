question_list=["How many continents are there?","What is the capital of India?","NG mei kaun se course padhaya jaata hai?"]

options_list = [["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],
["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
solution_list = [3, 4, 1]
i=0
while i<len(question_list):
    print(question_list[i])
    print(options_list[i])
    guess=int(input('enter your option  1,2,3,4:-'))
    if guess==solution_list[i]:
        print('correct answer')
    else:
        break
    i=i+1


        





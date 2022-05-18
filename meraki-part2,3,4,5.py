question_list=["How many continents are there?","What is the capital of India?","NG mei kaun se course padhaya jaata hai?"]

options_list = [["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],
["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
solution_list = [3, 4, 1]
print('apka sawal hai:')
i=0
while i<len(question_list):
    print(question_list[i])
    print('apke options hai:-')
    j=0
    while j<=len(options_list):
        print(j+1,options_list[i][j])
        j=j+1
    guess=int(input('enter your option  1,2,3,4:-'))
    if guess==solution_list[i]:
        print('congrats! apka answer sahi hai')
    else:
        print('sadly apka jawab galat hai')
        print('you are out of game now')
        break
    i=i+1
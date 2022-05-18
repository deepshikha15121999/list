question_list=["How many continents are there?","What is the capital of India?","NG mei kaun se course padhaya jaata hai?"]

options_list = [["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],
["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
solution_list = [3, 4, 1]

options_list1= [["Seven", "Eight"],["Chandigarh", "Delhi"],
["Software Engineering","Agriculture"]]

solution_list1= [1, 2, 1]
print('apka sawal hai:')
i=0
c=0
while i<len(question_list):
    print(question_list[i])
    print('apke options hai:-')
    j=0
    while j<=len(options_list):
        print(j+1,options_list[i][j])
        j=j+1
    guess=int(input('enter your option  1,2,3,4 or 5050:-'))
    if guess==5050:
        if c<1:
            print('apke options hai:-')
            k=1
            while k<len(options_list1):
                print(k,options_list1[i][k-1])
                k=k+1
            againguess=int(input('enter 1 and 2 only:-'))
            if againguess==solution_list1[i]:
                print('your answer is correct')
            else:
                ('your answer is wrong')
                break
            c=c+1
        else:
            print('you used your lifeline')
    elif guess==solution_list[i]:
        print('congrats! apka answer sahi hai')
    else:
        print('sadly apka jawab galat hai')
        print('you are out of game now')
        break
    i=i+1
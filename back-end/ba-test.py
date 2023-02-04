# task 1
# def returnDays(totalDays):
#     years = totalDays//365
#     weeks = (totalDays-years*365)//7
#     days = (totalDays-years*365)%7
#     print(f"Years: {years}\nWeeks: {weeks}\nDays: {days}")
# totalDays = int(input("Enter total days:"))
# returnDays(totalDays)

# # task 2
# text = input('Enter the string: ')
# subtext = input('Enter the substring to search: ')
# if subtext in text:
#     print("The substring exists in the string")
# else:
#     print("It does NOT exist.")

# # task 3
# text = input("Enter the text: ")
# lower_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# count=0
# for i in range(len(text)):
#     if text[i] in lower_letters or text[i] in capital_letters:
#         count+=1
# print("True") if count>=26 else print("False")

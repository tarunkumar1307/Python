#KBC(Kon Banega Crorepati) Game
import os
print("\t\t.....Welcome to the Game, Kon Banega Crorepati.....")
print()
print("Rules : ")
print("1.\tEnter your corerct name.\n2.\tThere are total 13 Questions.\n3.\tThere is no Time Limit.")

print("\nAmount list of Questions.")
print("Question 1 \t:\t 10,000\nQuestion 2 \t:\t 50,000\nQuestion 3 \t:\t 1,50,000\nQuestion 4 \t:\t 5,00,000\nQuestion 5 \t:\t 15,00,000\nQuestion 6 \t:\t 30,00,000\nQuestion 7 \t:\t 50,00,000\nQuestion 8 \t:\t 60,00,000\nQuestion 9 \t:\t 70,00,000\nQuestion 10 \t:\t 80,00,000\nQuestion 11 \t:\t 1,00,00,000\nQuestion 12 \t:\t 2,50,00,000\nQuestion 13 \t:\t 7,00,00,000")
print()

name = input("Enter your correct Name : ")
print()
print(f"Hello {name}, Your game starts now, Your first question is on your computer screen.\n")

price=("10,000", "50,000", "1,50,000", "5,00,000", "15,00,000", "30,00,000", "50,00,000", "60,00,000", "70,00,000", "80,00,000", "1,00,00,000", "2,50,00,000", "7,00,00,000")
pric=[10000,50000,150000,500000,1500000,3000000,5000000,6000000,7000000,8000000,10000000,25000000,70000000]
q1="Current Railway Ministery of India is\nA.\tMamta Banarjee\nB.\tRam Vilash\nC.\tAshwini Vaishnaw\nD.\tPityush Goyal"
q2="Which god is also known as \"Gauri Nandan\"?\nA.\tAgni\nB.\tIndra\nC.\tHanuman\nD.\tGanesha"
q3="Who is the founder of the political party Dravida Munnetra Kazhagam (DMK)?\nA.\tC.N. Annadurai\nB.\tM. Karunanidhi\nC.\tM.G. Ramachandran\nD.\tJayalalitha"
q4="Which former Indian President died as a result of a road accident?\nA.\tRajendra Prasad\nB.\tFaqruddin Ali Ahmed\nC.\tGiani Zail Singh\nD.\tR. Venkatraman"
q5="Who wrote India's National Anthem?\nA.\tRabindranath Tagore\nB.\tLal Bahadur Shastri\nC.\tChetna Bhagat\nD.\tRK Narayan"
q6="How many religions are there in India?\nA.\t6\nB.\t7\nC.\t8\nD.\t9"
q7="When is the National Hindi Diwas celebrated?\nA.\t13 September\nB.\t14 September\nC.\t14 July\nD.\t15 August"
q8="How many states are there in India?\nA.\t28\nB.\t29\nC.\t31\nD.\t30"
q9="Which James Bond movie was shot in the Indian city of Udaipur?\nA.\tDiamonds Are Forever\nB.\tLicense to Kill\nC.\tLive and Let Die\nD.\tOctupussy"
q10="Who wrote Vande Mataram?\nA.\tSarat Chandra Chattopadhyay\nB.\tRabindranath Tagore\nC.\tBankim Chandra Chatterjee\nD.\tIshwar Chandra Vidyasagar"
q11="Which one of the following places is famous for the Great Vishnu Temple?\nA.\tBordubar, Indonesia\nB.\tBamiyan, Afganistan\nC.\tPanja Sahib, Pakistan\nD.\tAnkorvat, Cambodia"
q12="The largest Buddhist Monastery in India is located at\nA.\tSarnath, Uttar Pradesh\nB.\tTawang, Arunachal Pradesh\nC.\tDharmashala, Himachal Pradesh\nD.\tGangtok, Sikkim"
q13="Who among the following was killed during 'Operation Bluestar' of 1984?\nA.\tBaba Santa Singh\nB.\tHaji Mastan\nC.\tJarnail Singh Bhindrawale\nD.\tHomi Jehangir Bhabha"

question=[q1, q2, q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13]
answer=["C","D","A","D","A","C","B","A","D","C","D","B","C"]
sum=0
correct=0
for i in range(13):
    print(f"Q{i+1}.\t", question[i])
    an=input("\nEnter the answer (A/a) : ")
    if an.upper()==answer[i]:
        print("Correct Answer, You have won", price[i])
        sum = sum+int(pric[i])
        print(f"Total Amount is {sum}")
        correct = correct+1
        if i<12:
            print("\nLets move to the next Question, next question is on your computer screen.\n")
    else:
        print(f"Incorrect answer, BETTER LUCK NEXT TIME \"{name}\"")
        print("Your final amount is", sum)
        break
if correct==13:
    print(f"\nYou won the Game, CONGRATS \"{name}\", your total amount is {sum}.")

os.system("PAUSE") #to hold the screen
questions=[
    [  
"The International Literacy Day is observed on","Sep 8","Nov 28","May 2","Sep 22",1],
["The language of Lakshadweep. a Union Territory of India, is","Tamil","Hindi","Malayalam","Telugu",3],
["In which group of places the Kumbha Mela is held every twelve years?","Ujjain Haridwar","Prayag Ujjain Nasik","Rameshwaram Dwarika","ChittakootHaridwar",2],
["Bahubali festival is related to","Islam","Hinduism","Buddhism","Jainism",4],
["Which day is observed as the World Standards  Day","June 26","Oct 14","Nov 15","Dec 2",2
        ],
["Which of the following was the theme of the World Red Cross and Red Crescent Day","Dignity for all - focus on women",
"Dignity for all - focus on Children","Focus on health for all",
"Nourishment for all-focus on children",2],

["September 27 is celebrated every year as","Teachers Day",
"National Integration Day","World Tourism Day"
,"International Literacy Day",3
    ],
["Who is the author of 'Manas Ka-Hans","Khushwant Singh",
"Prem Chand","Jayashankar Prasad","Amrit Lal Nagar",4
    ],
[ "The death anniversary of which of the following leaders is observed as Martyrs' Day","Smt. Indira Gandhi","PI. Jawaharlal Nehru","Mahatma Oandhi",
"Lal Bahadur Shastri",3
    ],
["Who is the author of the epic Meghdoot","Vishakadatta","Valmiki","Banabhatta","Kalidas",4
    ],
["Good Friday' is observed to commemorate the event of","birth of Jesus Christ","birth of' St. Peter","crucification 'of Jesus Christ","rebirth of Jesus Christ",3
    ],
["Who is the author of the book Amrit Ki Ore","Mukesh Kumar","Narendra Mohan","Upendra Nath","Nirad C. Choudhary",2
    ],
[ "Which of the following is observed as Sports Day every year","22nd April","26th  july","29th August","2nd October",3
    ],
["World Health Day is observed on","Apr 7","Mar 6","Mat I5"
,"Apr 28",1
    ],
["  Pongal is a popular festival of which state?","Karnataka"
,"Kerala","Tamil Nadu","Andhra Pradesh",1
    ]
        
    ]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
i=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"\n\nQuestion for Rs.{levels[i]}")
    print(question[0])
    print(f"a.{question[1]}     b.{question[2]}")
    print(f"c.{question[3]}     d.{question[4]}")
  
    answer=int(input("enter your answer (1-4):"))
    if(answer==questions[i][5]):
        print("JAWAB SAHI HAI")
        print(f"AUR AAP RECEIVE KARTHE HAIN {levels[i]} RUPI")
        money=0
        if(i==4):
            money=10000
        if(i==9):
            money=320000
        if(i==14):
            money=10000000
            break
    
    else:
        print("WRONG ANSWER")
        break
    
print(f"{money} acheived by you and can be taken to home")

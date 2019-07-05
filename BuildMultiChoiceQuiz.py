from buildquiz import questions

question_list=[
    "1. when was your 1st date\n a.feb 14\n b.feb 15\n c.feb 16\n",
    "2. what's her fav color?\n a.Black\n b.blue\n c.red\n",
    "3. what's her fav food?\n a.Fish curry\n b.Chicken curry\n c.ChickenBir\n",
    "4. what's her fav pastime?\n a.Youtube\n b.Music\n c.shopping\n",
    "5. what's her fav outfit for a party?\n a.Dress\n b.Top and skirt\n c.denim pants\n",
    "6. what's her fav chocolate?\n a.Fabelle\n b.Bournville\n c.Ferrero rocher\n",
    "7. what's her fav ice cream?\n a.cake Iceceam\n b.cone\n c.bar\n",
    "8. what can get on her nerves very easily?\n a.Racism\n b.nosy ppl\n c.people throwing garbage on Streets\n",
    "9. what's her fav chips?\n a.The green snack cheesy jalapeno\n b.kurkure puffcorn\n c.lays\n",
    "10. what does she do for therapy when feeling down?\n a.Beauty pamper\n b.Shopping\n c.eat junk\n"
    ]

questions_obj=[
    questions(question_list[0],"a"),
    
    questions(question_list[1],"a"),
    
    questions(question_list[2],"c"),

    questions(question_list[3],"a"),

    questions(question_list[4],"a"),

    questions(question_list[5],"a"),

    questions(question_list[6],"a"),

    questions(question_list[7],"a"),

    questions(question_list[8],"a"),

    questions(question_list[9],"b"),
    
    ]

def run_test(questions_obj):
    score=0
    for var in questions_obj:
        user_answer=input(var.qprompt)
        if user_answer==var.qanswer:
            score+=10
    print("you know your wife "+ str(score)+ "%")
    if score>=80:
        print("you're an amazing husband,Luv you :*")
    elif score>=50:
        print("you're an average husband")
    else:
        print("you know nothing about your wife,useless man!!")

run_test(questions_obj)
    




    
    


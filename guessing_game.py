
guess_word="hello"
user_ip=""
total_guess=5
guess_count=0


while(user_ip!=guess_word and guess_count<total_guess):
    
    user_ip=input("enter word")
    guess_count+=1
    if(user_ip==guess_word):
        print("you win")
    else:
        print(" out of guesses, you lose")

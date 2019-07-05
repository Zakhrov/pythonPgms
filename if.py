is_dark=False
is_tall=True

if(is_dark and is_tall):
    print("you are tall and dark beautiful woman")
#elif(is_dark or is_tall):
 #   print("you are either dark or tall")
    #????????????????????
elif not(is_dark) and not(is_tall):
    print("you are neither dark nor tall")
elif (is_dark) and not(is_tall):
    print("you are dark but not tall")
elif not(is_dark) and (is_tall):
        print("you are not dark but  tall")

else:
    print("you are beautiful anyway")



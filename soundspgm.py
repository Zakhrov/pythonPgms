import pygame.mixer

def wait_finish(channel):
    while channel.get_busy():
        pass
    
sounds=pygame.mixer
sounds.init()

correct=sounds.Sound("correct.wav")
wrong=sounds.Sound("wrong.wav")

prompt="press 1 for correct,2 for wrong or 0 to quit"

n_asked=0
n_correct=0
n_wrong=0

choice=input(prompt)
while choice!='0':
    if choice=='1':
        n_asked+=1
        n_correct+=1
        wait_finish(correct.play())
    if choice=='2':
        n_asked+=1
        n_wrong+=1
        wait_finish(wrong.play())
    choice=input(prompt)

print("asked questions" + str(n_asked))
print("correct" + str(n_correct))
print("wrong" + str(n_wrong))
        

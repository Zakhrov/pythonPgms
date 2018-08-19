s={}
def scoreProcessFn(id2find):
    res_data=open("scorefile1.txt")
    for eachline in res_data:
        s['id'],s['name'],s['country'],s['average'],s['game'],s['age']=eachline.split(";")
        if id2find==int(s['id']):
            res_data.close()
            return(s)
    res_data.close()
    return({})
lookup_id=int(input("enter the id"))
surfer=scoreProcessFn(lookup_id)
if surfer:
    print("ID:    " + surfer['id'])
    print("Name:    " + surfer['name'])
    print("Country:    " + surfer['country'])
    print("Avg:    " + surfer['average'])
    print("Game:    " + surfer['game'])
    print("Age:    " + surfer['age'])


class MaxNo:
    def findmax(nos):
        maxx=nos[0]
        for n in nos:
            if n>maxx:
                maxx=n
        return maxx

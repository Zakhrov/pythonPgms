
def cal_pow(base,pow_n):
    result=1

    for index in range(pow_n):
        result=result*base
    return result





print(cal_pow(3,4))


emp_cpy=open("emp.txt","a")

emp_cpy.write("\nkelly gjhjkk")
emp_cpy.close()
emp_cpy=open("emp.txt","r")
emp_c=emp_cpy.readlines()
print("ReadLine: %s" %(emp_c))

    

a = 3
def Fuc():   
    global a   # 所以确定要引用并修改全局变量必须加上global关键字
    print ("Func_a = ", a)    # 2输出4
   #要修改函数Func中与全局变量a同名的值，则函数中的该变量就会变成局部变量，在修改之前对该变量的引用自然会出现未分配或未定义的错误
    a = a + 1  
    # print("a+1 =", a)
if __name__ == "__main__":
    print ("main_a = ", a)  # 先输出  3
    a = a + 1
    Fuc()
    print ("main_func", a)  # 3输出5
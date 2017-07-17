
def getSum(mylist):
    if len(mylist)==0:
        return 0
    else:
        return mylist[0] + getSum(mylist[1:]) 

if __name__ == "__main__":
    my_list = [1,2,3]  # dynamic
    print(getSum(my_list))

l = [8, 3, 5, 1] #The input list

result = 0  #create a variable to store the output

nums = len(l) #get the length of the list

#use for loop to iterate the index of each number in the list then add up each number to 'result'
for idx in range(nums):
    result += l[idx] * (10 ** (nums - idx - 1)) #the smaller the index is, the higher the number will be

print(result) # Ultimately, I just print the result

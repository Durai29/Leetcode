    # not efficient
# def dailyTemperatures(temperatures):
#     answer = [0] * len(temperatures)
#     l = 0
#     while l < len(temperatures) - 1:
#         r = l + 1
#         while r < len(temperatures) and temperatures[l] >= temperatures[r]:
#             r += 1
#         if r >= len(temperatures):
#             r = l
#         answer[l] = r-l
#         l += 1
#     return answer

# Monotonic Stack 
def dailyTemperatures(temperatures):                                    # Leetcode : 739
    answer = [0] * len(temperatures)                                    # create the answer array
    stack = []                                                          # create a stack
    for i in range(len(temperatures)):                                  # use for loop to iterate temperatures
        while stack and temperatures[i] > temperatures[stack[-1]]:      # this is the main condition if stack is not empty
            prev = stack.pop()                                          # and the top element in the stack is lesser than current element
            answer[prev] = i - prev                                     # pop the top element and mark the difference of i - perv in the index of perv in answer
        stack.append(i)                                                 # append the element to the stack
    return answer                                                       # return answer

# It's really hard to understand the functioning of the monotonic stack.
# I should probably start practicing more problems based on this topic.
# This one is a problem of type Decreasing monotonic stack.
# I would also link to some reference video for understanding this topic better.

print(dailyTemperatures([73,74,75,71,69,72,76,73]))
print(dailyTemperatures([30,40,50,60]))
print(dailyTemperatures([30,60,90]))
print(dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))
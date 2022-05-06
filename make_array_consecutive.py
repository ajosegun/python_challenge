'''
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

 
Example
For statues = [6, 2, 3, 8], the output should be
makeArrayConsecutive2(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.
'''

def makeArrayConsecutive2(statues):
  '''
  Subtract the number of elements currently in statues from the number of elements that should be in statues.
  
  max(statues) - min(statues) + 1 gives the number of elements that should be in statues
  len(statues) gives the number of elements currently in statues 

  For the first test case: [6,2,3,8]
  The number of elements that should be in statues: 7
  The number of element currently in statues: 4
  
  7 - 4 = 3
  (8-2 + 1) - (4) = 3, which is the correct answer

  '''
  return (max(statues) - min(statues) + 1) - len(statues)


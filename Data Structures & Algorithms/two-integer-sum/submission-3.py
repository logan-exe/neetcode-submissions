class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        myDict = {}
        for i,val in enumerate(nums):
            if val in myDict:
                myDict[val].append(i)
            else:
                myDict[val] = [i]

        print(myDict)       


        for i,val in enumerate(nums):
            if (val <= target or val!=target ) and ((target-val) in myDict):
                print(True, (target-val), target, val)
                for k in myDict[target-val]:
                    if k!=i:
                        return[i,k]
    
        
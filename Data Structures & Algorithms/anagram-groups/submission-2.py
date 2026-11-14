class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        for i in strs:
            cur = sorted(i)
            sorted_curSum = "".join(cur)
            if sorted_curSum in myDict:
                myDict[sorted_curSum].append(i)
            else:
                myDict[sorted_curSum] = [i]
        ans = []
        for key,val in myDict.items():
            ans.append(val)
        return ans


        
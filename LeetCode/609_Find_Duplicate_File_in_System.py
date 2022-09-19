'''
Runtime: 355 ms, faster than 5.08% of Python3 online submissions for Find Duplicate File in System.
Memory Usage: 22.2 MB, less than 99.32% of Python3 online submissions for Find Duplicate File in System.
'''
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contentsDict = dict()
        
        for path in paths:
            splitted = path.split()
            dirPath = splitted[0]
            
            for filename in splitted[1:]:
                content = re.search(r'\(\S+\)', filename).group(0)
                formatted = f'{dirPath}/{filename}'.replace(content, '')
                
                if content in contentsDict:
                    contentsDict[content].append(formatted)
                else:
                    contentsDict[content] = [formatted]
                
        return filter(lambda x: len(x) > 1, contentsDict.values())

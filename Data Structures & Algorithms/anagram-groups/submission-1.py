class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        
        if len(strs) > 0:
            output.append([strs[0]])

        for i in range(1, len(strs)):
            placed = False

            for j in range(len(output)):
                if len(strs[i]) != len(output[j][0]):
                    continue

                temp = {}
                for c in strs[i]:
                    temp[c] = temp.get(c, 0) + 1
                
                ok = True
                for c in output[j][0]:
                    if c not in temp:
                        ok = False
                        break

                    temp[c] -= 1
                    if temp[c] < 0:
                        ok = False
                        break
                if ok:
                    output[j].append(strs[i])
                    placed = True
                    break
            if not placed:
                output.append([strs[i]])

        return output
                                

            

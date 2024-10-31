class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #we want to use sliding window
        #we are creating 2 arrays that has 26 spots 
        #we fill that in with s1 and s2 at the same length check if they have identical spots
        #if they dont then we are going to create match
        #we then take out from the from the right array to and keep checking with matches to see if they ever hit 26
        if len(s1) > len(s2):
            return False

        checkS1, checkS2 = [0]*26, [0]*26

        for i in range(len(s1)):
            checkS1[ord(s1[i]) - ord('a')] += 1 #this will set to 1 of the 26 index in array
            checkS2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0

        for i in range(26):
            if checkS1[i] == checkS2[i]:
                matches += 1
        
        l = 0
        for r in range(len(s1),len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            checkS2[index] += 1
            if checkS1[index] == checkS2[index]:
                matches += 1
            elif checkS1[index] + 1 == checkS2[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            checkS2[index] -= 1
            if checkS1[index] == checkS2[index]:
                matches += 1
            elif checkS1[index] - 1 == checkS2[index]:
                matches -= 1
            l += 1
        return matches == 26
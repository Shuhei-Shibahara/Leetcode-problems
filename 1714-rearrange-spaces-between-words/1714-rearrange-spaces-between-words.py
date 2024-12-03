class Solution:
    def reorderSpaces(self, text: str) -> str:
        space = 0
        curr_word = ''
        words = []
        
        # Count spaces and split words
        for i in range(len(text)):
            if text[i] == " ":
                if curr_word:
                    words.append(curr_word)
                    curr_word = ""
                space += 1
            else:
                curr_word += text[i]
        
        if curr_word:  # Add the last word if there is one
            words.append(curr_word)
        
        # Calculate divide and remaining spaces
        if len(words) > 1:
            divide = space // (len(words) - 1)
            remainder = space % (len(words) - 1)
        else:
            divide = 0
            remainder = space
        
        # Build the result string
        res = ""
        for i in range(len(words) - 1):
            res += words[i]
            res += " " * divide
        
        res += words[-1]  # Add the last word
        res += " " * remainder  # Add remaining spaces at the end
        
        return res
        
            
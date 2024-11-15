# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         else:
#             d = {}
#             for i, j in zip(s, t):
#                 if j in d.values():
#                     continue  # Skip the iteration if the value already exists
#                 d[i] = j
#             #print(d)
#             new_s = ""
#             for char in s:
#                 new_s = new_s + d.get(char, "#") 
#             #print(s, new_s, t)
#             if new_s == t:
#                 return True
#             else:
#                 return False 
    
        
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s, t):
            # Check if there's already a mapping for s -> t
            if char_s in s_to_t and s_to_t[char_s] != char_t:
                return False
            # Check if there's already a mapping for t -> s
            if char_t in t_to_s and t_to_s[char_t] != char_s:
                return False
            
            # Create mappings in both dictionaries
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s
        
        return True

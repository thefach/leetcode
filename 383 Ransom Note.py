# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
#         magazine_dict = {}
#         for char in magazine:
#             magazine_dict[char] = magazine_dict.get(char, 0) + 1
#         print(magazine_dict)

#         note_dict = {}
#         for char in ransomNote:
#             note_dict[char] = note_dict.get(char, 0) + 1
#         print(note_dict)

#         can_be_used_list = []

#         for letter in note_dict:
#             print(letter, note_dict[letter])
#             try:
#                 if note_dict[letter] <= magazine_dict[letter]:
#                     can_be_used_list.append(True)
#                 else:
#                     can_be_used_list.append(False)
#             except:
#                 can_be_used_list.append(False)
#         print(can_be_used_list)
        
#         return all(can_be_used_list)

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count the frequency of each character in both strings
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        # Iterate over each unique character in ransomNote
        for char in ransom_count:
            # If the character count in ransomNote exceeds that in magazine, return False
            if ransom_count[char] > magazine_count.get(char, 0):
                return False
        return True






        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagram = same occurences of letters

        result = defaultdict(list)

        for string in strs:
            key = [0] * 26
            for char in string:
                key[ord(char)-ord('a')] += 1
            result[tuple(key)].append(string)
        return list(result.values())
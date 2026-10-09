class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagram = same occurence of letters

        # use occurence of letters as buckets in a hashmap
        anagrams = defaultdict(list)

        for string in strs:
            key = [0] * 26

            for char in string:
                key[ord(char)-ord('a')] += 1
            anagrams[tuple(key)].append(string)
            
        return list(anagrams.values())
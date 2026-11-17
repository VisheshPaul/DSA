class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = dict()
        res = [[] for _ in range(len(searchWord))]

        products.sort()
        
        curr = trie
        for i, char in enumerate(searchWord):
            curr[char] = (dict(), res[i])
            curr = curr[char][0]

        for word in products:
            curr = trie
            for char in word:
                if char not in curr:
                    break
                
                curr, currValues = curr[char]

                if len(currValues) < 3:
                    currValues.append(word)

        return res
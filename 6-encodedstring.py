class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        decoded = []
        while i < len(s):
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            decoded.append(word)
            i = j + 1 + length
            j = j + 1 + length
        return decoded

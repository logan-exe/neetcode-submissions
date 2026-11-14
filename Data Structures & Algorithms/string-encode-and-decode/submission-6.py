class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i)) + "#" + i 
        return s

    def decode(self, s: str) -> List[str]:
        final = []
        i = 0
        prev_end = 0

        while i < len(s):
            if s[i] == "#":
                start = i - 1
                cur = ""

                # Collect the number before `#`
                while start >= prev_end and s[start].isdigit():
                    cur = s[start] + cur  # Append the digit to the beginning of `cur`
                    start -= 1

                # Extract the substring of specified length
                length = int(cur)
                substring = s[i + 1:i + 1 + length]
                print(substring, i + 1 + length)

                final.append(substring)
                prev_end = i + 1 + length  # Update `prev_end` to avoid reprocessing
                i = prev_end - 1  # Adjust `i` to continue after the substring

            i += 1  # Increment `i` for the next character

        return final
                

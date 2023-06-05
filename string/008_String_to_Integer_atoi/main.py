def readraw():
    return input()


def readtype(typ=None):
    if typ is None:
        return input().strip()
    else:
        return typ(input().strip())


def readarray(typ=None):
    inpt_list = input().split()
    if typ is None:
        return [int(x) if x.lstrip("-").isdigit() else x for x in inpt_list]
    else:
        return list(map(typ, inpt_list))


class Solution:
    # Conduct the clamp 
    def clamp(self, n, smallest=-2**31, largest=2**31-1):
        return max(smallest, min(n, largest))

    # Change method name and definition
    def myAtoi(self, s: str) -> int:
        # Remove whitespace
        s = s.strip()

        # Get the string of number
        sign_str = ''
        num_str = ''
        for ix, c in enumerate(s):
            if ix == 0 and c in '+-':
                sign_str = c
                continue

            if c.isdigit():
                num_str += c
            else:
                break

        # Convert string to integer
        if num_str == '':
            num = 0
        else:
            num = int(sign_str + num_str)
        
        ans = self.clamp(num)
        return ans


if __name__ == "__main__":
    # make parameter from input file 
    param = readraw()
    ans = Solution().myAtoi(param)
    print(ans)

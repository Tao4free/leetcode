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
    # Change method name and definition
    def sol(self, s: str) -> str:
        ans = 'This is a template.'
        return ans


if __name__ == "__main__":
    # make parameter from input file 
    param = readraw()
    # arr = readarray()
    # TODO
    ans = Solution().sol(param)
    print(ans)

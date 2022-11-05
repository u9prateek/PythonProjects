class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        rstr = ""
        for x in strs:
            if rstr =="":
                rstr +=x
            else:
                t=":;"
                rstr = rstr+t+x
        return rstr

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, rstr):
        # write your code here
        strs = list(map(str,rstr.split(':;')))
        return strs

ot = Solution()
ote = ot.encode(["lint","code","love","you"])
print(ote)
print(ot.decode(ote))

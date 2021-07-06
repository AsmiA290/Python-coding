#create a class 
class Solution(object):
    def lettercount(self, letter):
        ''' Counts the number of letters in a str
        input type: str input=letter
        output= int '''
        setv ="".join(set(letter))
        return setv

if __name__=="__main__":
    example= "letteres"
    sol=Solution()
    output=sol.lettercount(example)
    print(output)
    print(example(len))




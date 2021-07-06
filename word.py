def lengthOfLastWord(s):
    
    Split=s.split()
    Split.reverse()
    print(Split)
    Lw=Split[0]
    return len(Lw)
if __name__ == "__main__":
    a =input("Please enter a sentance")
    l=lengthOfLastWord(a)
    print(l)


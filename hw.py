class v:

    def __init__(self,w):
        self.s=w

    def rev(self):
        return self.s[::-1]
    

ob=str(input("Enter the word to reverse:"))
l=v(ob)
result=l.rev()
print("Reversed word:",result)

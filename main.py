class Solution(object):
    def __init__(self, num):
        self.num = num

    def isHappy(self):
        # self.num = list(map(int, str(self.num)))
        #print(self.num)

        while int(self.num) >= 10:
            self.num = str((int(self.num[0]) * int(self.num[0])) + (int(self.num[1]) * int(self.num[1])))
            print(self.num)
            length = len(self.num)

        if self.num == 1 or self.num == "1":
            print("True")
        else:
            print("False")



num = input(">> ")
# num = int(num)
c = Solution(num)
c.isHappy()

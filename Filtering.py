class Filtering(object):
    def __init__(self, slur):
        self.__slur = slur

    def readFile(self):
        slurList = []
        with open("filterList.csv", "r") as csvFile:
            for line in csvFile:
                slurList.append(line)
        return slurList

    def filter(self):
        slurList = self.readFile()
        uText = input("Enter your message: ")
        for i in range(0, len(slurList)-1, 1):
            if any(uText.__contains__, slurList[i]):
                print("Your message was censored because it contained an inappropriate word.")


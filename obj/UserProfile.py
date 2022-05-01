class UserProfile(object):
    def __init__(self, firstName, lastName, age, uName, password, pronouns,
                 interestList, friendList, receivedFriendReq, bio, socialMedia):
        self.__firstName = firstName # String
        self.__lastName = lastName # String
        self.__age = age # int
        self.__uName = uName # String
        self.__password = password # String
        self.__pronouns = pronouns # enum???
        self.__interestList = interestList # make list out of Interest enum
        self.__friendList = friendList
        self.__receivedFriendReq = receivedFriendReq
        self.__bio = bio
        self.__socialMedia = socialMedia

    def getFirstName(self):
        return self.__firstName

    def setFirstName(self, fname):
        self.__firstName = fname.lower.capitalize()

    def getLastName(self):
        return self.__lastName

    def setLastName(self, lname):
        self.__lastName = lname.lower.capitalize()

    def getAge(self):
        return self.__age

    def setAge(self, age):
        if age > 18:
            self.__age = age
        else:
            print("You must be 18 or older to create an account.")

    def getUName(self):
        return self.__uName

    def setUName(self, uName):
        self.__age = uName

    def getPassword(self):
        return self.__password

    def setPassword(self, pw):
        self.__password = pw

    def getPronouns(self):
        return self.__pronouns

    def setPronouns(self, pronouns):
        self.__pronouns = pronouns

    def getInterestList(self):
        return self.__interestList

    def setInterestList(self, interestList):
        self.__interestList = interestList

    def getFriendList(self):
        return self.__friendList

    def setFriendList(self, friendList):
        self.__friendList = friendList

    def getReceivedFriendReq(self):
        return self.__receivedFriendReq

    def setReceivedFriendReq(self, receivedFriendReq):
        self.__receivedFriendReq = receivedFriendReq

    def getBio(self):
        return self.__bio

    def setBio(self, bio):
        self.__bio = bio

    def getSocialMedia(self):
        return self.__socialMedia

    def setSocialMedia(self, sm):
        self.__socialMedia = sm
class Program():

    def __init__(self, *args,**kwargs):

        self.lang = input("What language?: ")
        self.version = float(input("Version?: "))
        self.skill = input("Skill level: ")

    def upgrade(self):

        new_version = float(input("what new version: "))
        print("We have updated the to the new version for", self.lang)
        self.version = new_version

p1 = Program()

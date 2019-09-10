#! picture class


class Picture():
    def __init__(self, picture="", views=0):
        self.picture = picture
        self.views = views

    def toString(self):
        return str(self.views) + " " + self.picture
    

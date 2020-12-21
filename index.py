
from Controller.Employee import ControlEmployee


class Bootstrap():
    def __init__(self):
        self.File = ControlEmployee()

    def showData(self):
        self.File.renderData()


if __name__ == "__main__":
    Bootstrap().showData()

from testinlabel.exportAbstract import ExportAbstract # warning: don't edit this line !!!
from testinlabel.TLA import TLA     # warning: don't edit this line !!!

#import your packages

class Export(ExportAbstract):

    def __init__(self, tla: TLA):       # warning: don't edit this line !!!
        self.tla = tla                  # warning: don't edit this line !!!
        self.tla.SetKey("210723e32ad")  # warning: don't edit this line !!!
        self.tla.GetLabelData()         # warning: don't edit this line !!!

    def exec(self):
        # edit following code to
        for item in self.tla.taskList:
            print(item["imgUrl"])

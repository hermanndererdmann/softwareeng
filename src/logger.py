import pandas as pd

class logger:
    logframe = pd.DataFrame(columns=['Timestamp', 'Pattern', 'Color'])
    def __init__(self):
        pass
    def get_imgdata(self, imgdata):
        self.timestamp = imgdata.timestamp
        self.pattern = imgdata.pattern
        self.color = imgdata.color
        self.__append()

    def export(self, path=None):
        if path is None:
            filename = 'logs.csv'
        else:
            filename = path
        self.logframe.to_csv(filename, index=False)


    def __append(self):
        if self.pattern:
            for i in range(len(self.pattern)):
                new_data = pd.DataFrame({'Timestamp': [self.timestamp], 'Pattern': [self.pattern[i]], 'Color': [self.color[i]]})
                self.logframe = pd.concat([self.logframe, new_data], ignore_index=True)


        



 
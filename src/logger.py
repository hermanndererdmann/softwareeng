import pandas as pd

class logger:
    logframe = pd.DataFrame(columns=['Timestamp', 'Pattern', 'Color'])
    def __init__(self):
        pass
    def get_imgdata(self, imgdata):
        self.timestamp = imgdata.timestamp
        self.pattern = imgdata.pattern
        self.color = imgdata.color
        self._append()

    def export(self, path=None):
        if path is None:
            filename = 'logs.csv'
        else:
            filename = path
        self.logframe.to_csv(filename)


    def _append(self):
        new_data = {'Timestamp': self.timestamp, 'Pattern': self.pattern, 'Color': self.color}
        self.logframe = self.logframe.append(new_data, ignore_index=True)

    



 
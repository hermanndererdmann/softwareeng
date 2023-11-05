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

    def export(self):
        #get path and safe data
        path = input("Please enter the log file path (or press enter to use the current directory): ").strip()
        if path is None:
            filename = 'logs.csv'
        else:
            filename = path + 'logs.csv'
        self.logframe.to_csv(filename, index=False)


    def __append(self):
        #if list is not empty append the new data to the existing list
        if self.pattern:
            for i in range(len(self.pattern)):
                new_data = pd.DataFrame({'Timestamp': [self.timestamp], 'Pattern': [self.pattern[i]], 'Color': [self.color[i]]})
                self.logframe = pd.concat([self.logframe, new_data], ignore_index=True)


        



 
class Parser:
    def __init__(self, logs, debug=False):
        assert type(logs) is str or type(logs) is list, "Log must be a string or list."
        #Create some of our empty instance variables
        self.connections = {}
        #If log is a string convert it to an iterable (list)
        if type(logs) is str:
            self.logs = list(logs)
        else:
            self.logs = logs
        #Read our logs
        self.update()
    def update(self):
        for log in self.logs:
            with open(log, "r") as f:
                #Read the lines
                for l in f:
                    if "Client logged in" not in l:
                        continue
                    #Split our string
                    ldata = l.rsplit('Client logged in: ', 1)[1].split(':')
                    


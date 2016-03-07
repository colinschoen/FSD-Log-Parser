class Connection:
    def __init__(self, cid, server, callsign, client, uid):
        self.cid = cid
        self.server = server
        self.callsign = callsign
        self.client = client
        self.uid = uid

class Parser:
    def __init__(self, logs, debug=False):
        assert type(logs) is str or type(logs) is list, "Log must be a string or list."
        #Create some of our empty instance variables
        self.server2connections = {}
        self.connections = []
        #If log is a string convert it to an iterable (list)
        if type(logs) is str:
            self.logs = [logs]
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
                    #callsign,server,unknown,client,unknown,unknown
                    connection = Connection(ldata[6], ldata[1], ldata[0], ldata[3], ldata[7])
                    #Add our connection
                    if ldata[0] in self.server2connections:
                        self.server2connections[ldata[0]].append(connection)
                    else:
                        self.server2connections[ldata[0]] = []
                        self.server2connections[ldata[0]].append(connection)
                    self.connections.append(connection)
    def get_connections(self):
        #Copy our list so the original can't be mutated
        return list(self.connections)

    def get_connections_by_server(self, server=None):
        #Copy our dictionatry so the original can't be mutated
        if server:
            return dict(self.server2connections[server])
        return dict(self.server2connections)
                    


                    


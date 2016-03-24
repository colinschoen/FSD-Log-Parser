import pprint
class Connection:
    def __init__(self, cid, server, callsign, client, uid, date, time):
        self.cid = cid
        self.server = server
        self.callsign = callsign
        self.client = client
        self.uid = uid
        self.date = date
        self.time = time
    def echo(self):
        pprint.pprint(vars(self))


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
        server = None
        for log in self.logs:
            with open(log, "r") as f:
                #Read the lines
                for l in f:
                    #Nab our server
                    if not server and ": Reading" in l:
                        server = l.rsplit(': Reading', 1)[0].rsplit()[2]
                    if "Client logged in" not in l:
                        continue
                    #Split our string
                    split = l.rsplit('Client logged in: ', 1)
                    ldata = split[1].split(':')
                    connected_at = split[0].split()[0:2]
                    date = connected_at[0]
                    time = connected_at[1]
                    #Is our CID numeric?
                    if not ldata[6].isnumeric():
                        #Glitch in the log, omit this record.
                        continue
                    #cid,server,callsign,client,uid
                    connection = Connection(ldata[6], ldata[1], ldata[0],
                            ldata[3], ldata[7].rstrip(), date, time)
                    #Add our connection
                    if server in self.server2connections:
                        self.server2connections[server].append(connection)
                    else:
                        self.server2connections[server] = []
                        self.server2connections[server].append(connection)
                    self.connections.append(connection)
    def get_connections(self):
        #Copy our list so the original can't be mutated
        return list(self.connections)

    def get_connections_by_server(self, server=None):
        #Copy our dictionatry so the original can't be mutated
        if server:
            return dict(self.server2connections[server])
        return dict(self.server2connections)

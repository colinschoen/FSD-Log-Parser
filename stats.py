import argparse
import parser

def connections(parser, percent):
    connections = parser.get_connections()
    print(len(connections), "logged network connections")

def users(parser, percent):
    #How many unique users have connected to this server?
    seenCIDs = set()
    connections = parser.get_connections()
    for c in connections:
        cid = c.cid
        if cid in seenCIDs:
            continue
        seenCIDs.add(cid)
    print(len(seenCIDs), "unique user connections")

def clients(parser, percent):
    clients2users = {}
    seenConnections = set()
    connections = parser.get_connections()
    for c in connections:
        client = c.client
        cid = c.cid
        #Have we seen this use connect with this client before?
        if (cid, client) in seenConnections:
            #Yes, let's ignore it
            continue
        seenConnections.add((cid, client))
        if client not in clients2users:
            clients2users[client] = 1
        else:
            clients2users[client] += 1
    if percent:
        total = sum(clients2users.values())
        for client,count in clients2users.items():
            print(client + ": " + str(round((count/total) * 100, 2)) + "%")
    else:
        for client, count in clients2users.items():
            print(client + ": " + str(count))

def run(option, percent, *args):
    p = parser.Parser(*args)
    options = {
            "clients": clients,
            "users": users,
            "connections": connections
        }
    options[option](p, percent)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description="FSD Log Statistics")
    argparser.add_argument("type", help="Choose a type: clients", default="clients", type=str)
    argparser.add_argument("logs", help="Provide the log file/s", type=str)
    argparser.add_argument("-percent", help="Compute percentages", action="store_true")
    args = argparser.parse_args()
    run(args.type, args.percent, args.logs)


    

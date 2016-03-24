import argparse
import parser

def dups(parser, percent):
    uid2cids = {}
    connections = parser.get_connections()
    for c in connections:
        uid = c.uid
        cid = c.cid
        if uid not in uid2cids:
            uid2cids[uid] = set()
        uid2cids[uid].add(cid)
    dupesFound = False
    for uid, cids in uid2cids.items():
        if len(cids) > 1:
            dupesFound = True
            print(str(uid) + " used by " + str(cids))
    if not dupesFound:
        print("No dupes found")

def connections(parser, percent):
    servers = parser.get_connections_by_server()
    for server, connections in servers.items():
        print("=====" + server + "=====")
        print("  ", len(connections), "logged network connections")

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
    servers = parser.get_connections_by_server()
    for server, connections in servers.items():
        print("=====" + server + "=====")
        clients2users = {}
        seenConnections = set()
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
                print("   " + client + ": " + str(round((count/total) * 100, 2)) + "%")
        else:
            for client, count in clients2users.items():
                print("   " + client + ": " + str(count))

def run(option, percent, *args):
    p = parser.Parser(*args)
    options = {
            "clients": clients,
            "users": users,
            "connections": connections,
            "dups": dups
        }
    options[option](p, percent)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description="FSD Log Statistics")
    argparser.add_argument("type", help="Choose a type: clients, users, connections, dups " , default="clients", type=str)
    argparser.add_argument("logs", help="Provide the log file/s", nargs="+")
    argparser.add_argument("-percent", help="Compute percentages", action="store_true")
    args = argparser.parse_args()
    run(args.type, args.percent, args.logs)


    

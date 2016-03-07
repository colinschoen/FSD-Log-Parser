import argparse
import parser

def clients(parser):
    clients2users = {}
    connections = parser.get_connections()
    for c in connections:
        client = c.client
        if client not in clients2users:
            clients2users[client] = 1
        else:
            clients2users[client] += 1
    for client, count in clients2users.items():
        print(client + ": " + str(count))

def run(option, *args):
    p = parser.Parser(*args)
    options = {
            "clients": clients    
        }
    options[option](p)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description="FSD Log Statistics")
    argparser.add_argument("t", help="Choose a type: clients", default="clients", type=str)
    argparser.add_argument("logs", help="Provide the log file/s", type=str)
    args = argparser.parse_args()
    run(args.t, args.logs)


    

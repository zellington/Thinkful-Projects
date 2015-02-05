import logging
import csv
import argparse
import sys

# Set the log output file, and the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)

def put(name, snippet, filename):
    """ Store a snippet with an associated name in the CSV file """
    logging.info("Writing {!r}:{!r} to {!r}".format(name, snippet, filename))
    logging.debug("Opening file")
    with open(filename, "a") as f:
        writer = csv.writer(f)
        logging.debug("Writing snippet to file")
        writer.writerow([name, snippet])
    logging.debug("Write sucessful")
    return name, snippet


def get(name):
    """Retrieve the snippet with a given name.

    If there is no such snippet...

    Returns the snippet.

    """
    #return and fill in '...'
    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    logging.info("Retrieving {!r}".format(name))
    logging.debug("Retrieving file")
    #snippet = None
    with open("snippets.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if row[0] == name:
              return row[1]
            else:
              pass
def list():
    logging.error("FIXME: Unimplemented - list")
    logging.info("Retrieving list")
    logging.debug("Retrieving list")
    #snippet = None
    with open("snippets.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            print row[0]

def make_parser():
    """Construct the command line parser """
    logging.info("Construting parser")
    description = "Store and retieve snippets of text"
    parser = argparse.ArgumentParser(description=description)

    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    #Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="The name of the snippet")
    put_parser.add_argument("snippet", help="The snippet text")
    put_parser.add_argument("filename", default="Snippets.csv", nargs="?", help="The snippet filename")
    
    #Subparser for the get command
    logging.debug("Constructing get subparser")
    get_parser = subparsers.add_parser("get", help="Retrieve a snippet")
    get_parser.add_argument("name", help="The name of the snippet")

    #Subparser for list command
    logging.debug("Constructing list subparser")
    list_parser = subparsers.add_parser("list", help="Get list of names")
    
    return parser

def main():
    """ Main function """
    logging.info("Starting snippets")
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "put":
        name, snippet = put(**arguments)
        print "Stored {!r} as {!r}".format(snippet, name)
    elif command == "get":
        #add warning if snippet does not exist
        name = get(**arguments)
        print "Found snippet: {!r}".format(name)
    elif command == "list":
        print "Here are the available snippet names: \n" 
        get_list = list()

if __name__ == "__main__":
    main()
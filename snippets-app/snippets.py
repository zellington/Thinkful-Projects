import logging
import csv
import argparse
import sys
import psycopg2

# Set the log output file, and the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)
logging.debug("Connecting to PostgreSQL")
connection = psycopg2.connect("dbname='snippets' host='localhost'")
logging.debug("Database connection established.")
# Set put function
def put(name, snippet, filename):
    """ Store a snippet with an associated name in the 'snippets' database """
    logging.info("Writing {!r}:{!r} to {!r}".format(name, snippet, filename))
    cursor = connection.cursor()
    try:
        command = "insert into snippets values (%s, %s)"
        cursor.execute(command, (name, snippet))
        print "Stored {!r} as {!r}".format(snippet, name)
    except psycopg2.IntegrityError as e:
        connection.rollback()
        command = "update snippets set message=%s where keyword=%s"
        cursor.execute(command, (snippet, name))
        print "hey!"
    connection.commit()
    logging.debug("Snippet stored successfully.")
    return name, snippet
#Set get functiion
def get(name):
    """Retrieve the snippet with a given name.

    If there is no such snippet...

    Returns the snippet.

    """
    #return and fill in '...'
    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    logging.info("Retrieving {!r}".format(name))
    logging.debug("Retrieving file")
    message = {}
    cursor = connection.cursor()
    command = "select message from snippets where keyword='%s'" % name 
    cursor.execute(command)
    results = cursor.fetchone()
    if results:
        return results
    else:
        print "Sorry, no snippet with that name! Try again"
    #connection.commit()
    logging.debug("Snippet retrieved successfully.")
    
def list():
    logging.error("FIXME: Unimplemented - list")
    logging.info("Retrieving list")
    logging.debug("Retrieving list")
    cursor = connection.cursor()
    command = "select keyword from snippets" 
    cursor.execute(command)
    my_list = cursor.fetchall()
    return my_list

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
    elif command == "get":
        name = get(**arguments)
        if name:
            print "Found snippet: {!r}".format(name)
        else: 
            print "There is no snippet with that name - try again!"
    elif command == "list":
        get_list = list()
        print "Here are the available snippet names: \n" + str(get_list)

if __name__ == "__main__":
    main()
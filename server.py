import rpyc
from constCS import *
from utils import levenshtein
from rpyc.utils.server import ThreadedServer


class Server(rpyc.Service):
    def concat(self, first_string, second_string):
        """Concatenate two strings"""
        return first_string+second_string

    def levenshtein_dist(self, first_string, second_string):
        """Calculates the levenshtein distance between two strings"""
        return levenshtein(first_string, second_string)

    def equal(self, first_string, second_string):
        """Check if two strings are equal or not"""
        return True if first_string==second_string else False


if __name__ == "__main__":
    server = ThreadedServer(
        Server,
        port=PORT
    )
    server.start()
import rpyc
from constCS import *
from utils import levenshtein
from rpyc.utils.server import ThreadedServer


class StringOps(rpyc.Service):
    def exposed_concat(self, first_string, second_string):
        """Concatenate two strings"""
        return first_string+second_string

    def exposed_levenshtein(self, first_string, second_string):
        """Calculates the levenshtein distance between two strings"""
        return levenshtein(first_string, second_string)

    def exposed_equal(self, first_string, second_string):
        """Check if two strings are equal or not"""
        return True if first_string==second_string else False


if __name__ == "__main__":
    server = ThreadedServer(
        StringOps,
        port=PORT
    )
    server.start()
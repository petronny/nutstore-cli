# coding: utf-8


class Context(object):
    should_exit = False

    def __init__(self, client):
        """
        :type client: NutStoreClient
        """

        self.client = client

    @property
    def path(self):
        return self.client.cwd

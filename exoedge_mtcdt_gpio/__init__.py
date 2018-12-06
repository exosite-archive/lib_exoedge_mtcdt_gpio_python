"""
    An ExoEdge source for interfacing with Modbus TCP devices.
"""
# pylint: disable=W1202,C0111
import sys
import os
import logging
import time
from exoedge.sources import ExoEdgeSource
from exoedge import logger
from shownames import SHOWNAMES

LOG = logger.getLogger(__name__)
LOG.setLevel(logging.DEBUG)


class MTCDTGPIOExoEdgeSource(ExoEdgeSource):
    """ Exoedge GPIO source for the Multitech Conduit."""
    def show(self, *args, **kwargs):
        showname = kwargs.get('showname')
        if showname not in SHOWNAMES:
            return "Showname not supported: {}".format(showname)
        with open(os.path.join('/sys/devices/platform/mts-io', showname), 'r') as theshow:
            try:
                return int(theshow.read().strip())
            except:
                pass
            return theshow.read().strip()

    def run(self):

        while not self.is_stopped():
            time.sleep(0.1)
        logging.critical("{} HAS BEEN STOPPED.".format(self.name))

# register instance method with module so "classic" ExoEdge method can be used.
setattr(sys.modules[__name__], 'show', MTCDTGPIOExoEdgeSource().get_source().show)

logging.critical("current module methods: {}".format(dir(sys.modules[__name__])))

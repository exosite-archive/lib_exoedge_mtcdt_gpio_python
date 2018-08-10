"""
    An ExoEdge source for interfacing with Modbus TCP devices.
"""
# pylint: disable=W1202,C0111
import sys
import os
import logging
import time
from exoedge.sources import AsyncSource

logging.getLogger('MTCDT_GPIO')
logging.basicConfig(level=logging.DEBUG)

SHOWNAMES = [
    "ap1/product-id",
    "ap1/adc0",
    "ap1/adc1",
    "ap1/adc2",
    "ap1/din0",
    "ap1/din1",
    "ap1/din2",
    "ap1/din3",
    "ap1/led1",
    "ap1/led2",
    "ap1/device-id",
    "ap1/vendor-id",
    "ap1/dout0",
    "ap1/dout1",
    "ap1/dout2",
    "ap1/dout3",
    "ap1/reset",
    "ap1/dout-enable",
    "ap1/hw-version",
    "capability/adc",
    "capability/din",
    "capability/gps",
    "capability/dout",
    "capability/lora",
    "capability/wifi",
    "capability/bluetooth",
    "device-id",
    "eth-reset",
    "gpiob/product-id",
    "gpiob/adc0",
    "gpiob/adc1",
    "gpiob/adc2",
    "gpiob/din0",
    "gpiob/din1",
    "gpiob/din2",
    "gpiob/din3",
    "gpiob/led1",
    "gpiob/led2",
    "gpiob/device-id",
    "gpiob/vendor-id",
    "gpiob/dout0",
    "gpiob/dout1",
    "gpiob/dout2",
    "gpiob/dout3",
    "gpiob/reset",
    "gpiob/dout-enable",
    "gpiob/hw-version",
    "has-radio",
    "hw-version",
    "imei",
    "led-a",
    "led-b",
    "led-c",
    "led-cd",
    "led-d",
    "led-sig1",
    "led-sig2",
    "led-sig3",
    "led-status",
    "mac-eth",
    "product-id",
    "reset",
    "reset-monitor",
    "reset-monitor-intervals",
    "uuid",
    "vendor-id",
]

class MTCDTGPIOExoEdgeSource(AsyncSource):
    """ Exoedge GPIO source for the Multitech Conduit."""

    def show(self, *args, **kwargs):
        showname = kwargs.get('showname')
        if showname not in SHOWNAMES:
            return "Showname not supported: {}".format(showname)
        with open(os.path.join('/sys/devices/platform/mts-io', showname), 'r') as theshow:
            return theshow.read().strip()

    def run(self):
        while not self.is_stopped():
            time.sleep(0.1)
        logging.critical("{} HAS BEEN STOPPED.".format(self.name))

# set up borg instance of async source
src = MTCDTGPIOExoEdgeSource().get_async_source()

# get access to the current module
this_module = sys.modules[__name__]

# register all desired class methods to module
setattr(this_module, 'show', src.show)

logging.critical("current module methods: {}".format(dir(sys.modules[__name__])))

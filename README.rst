Description
############

This project is for using the Multitech Conduit GPIO Accessory Card on mLinux.

Install
#########

With `pip`
"""""""""""

.. code-block::

    pip install git+https://github.com/exosite/lib_exoedge_mtcdt_gpio_python.git

From Source
""""""""""""

Clone this repo and execute the following commands:

.. code-block::

    pip install -r requirements.txt
    python setup.py install

ExoEdge Configuration
######################


Example
""""""""

.. code-block::

    edged -H mqtt://f5330e5s8cho0000.m2.exosite.io/ -s gpio-test1 -i gpio-test1.ini go


ExoSense Configuration
########################

Below is an example that reads ADC channels 0 and 1 from the Multitech Conduit GPIO Accessory Card. Each channel is sampled once per second.

.. code-block:: json

    {
      "channels": {
        "gpiob/adc0": {
          "display_name": "ADC 0",
          "description": "Analog-to-Digital Converter Channel 0.",
          "properties": {
            "max": 4095,
            "precision": null,
            "data_type": "NUMBER",
            "min": 0
          },
          "protocol_config": {
            "report_on_change": false,
            "report_rate": 1000,
            "sample_rate": 1000,
            "mode": "poll",
            "app_specific_config": {
              "function": "show",
              "parameters": {
                "showname": "gpiob/adc0"
              },
              "positionals": [],
              "module": "exoedge_mtcdt_gpio"
            }
          }
        },
        "gpiob/adc1": {
          "display_name": "ADC 1",
          "description": "Analog-to-Digital Converter Channel 1.",
          "properties": {
            "max": 4095,
            "precision": null,
            "data_type": "NUMBER",
            "min": 0
          },
          "protocol_config": {
            "report_on_change": false,
            "report_rate": 1000,
            "sample_rate": 1000,
            "mode": "poll",
            "app_specific_config": {
              "function": "show",
              "parameters": {
                "showname": "gpiob/adc1"
              },
              "positionals": [],
              "module": "exoedge_mtcdt_gpio"
            }
          }
        }
      }
    }


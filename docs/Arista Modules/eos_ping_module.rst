.. _eos_ping:


eos_ping
++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.0.0

The eos_ping module will execute a network ping from the node and return the results.  If the destination can be successfully pinged, then the module returns successfully.  If any of the sent pings are not returned the module fails.  By default, the error threshold is set to the same value as the number of pings sent

Options
-------

.. raw:: html

    <table border=1 cellpadding=4>
    <tr>
    <th class="head">parameter</th>
    <th class="head">required</th>
    <th class="head">default</th>
    <th class="head">choices</th>
    <th class="head">comments</th>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">count</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">5</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the number of packets to send from the node to the remote dst.  The default value is 5.<br>(added in 1.1.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">dst</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Specifies the destination IP address or FQDN for the network ping packet.<br>(added in 1.1.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">error_threshold</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the error threshold (in packet loss percentage) for the ping test to be considered failed.  By default the value of the error_threshold is set to 0. Valid values between 0 and 100.<br>(added in 1.1.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">source</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the source interface for the network ping packet<br>(added in 1.1.0)    </td>
    </tr>
        </table><br>


.. important:: Requires Arista EOS 4.13.7M or later with command API enabled


.. important:: Requires Python Client for eAPI 0.4.0 or later


Examples
--------

.. raw:: html

    <br/>


::

    
    - eos_ping: dst=192.168.1.254 count=10
    
    # Set the error_threshold to 50% packet loss
    - eos_ping: dst=192.168.1.254 count=10 error_threshold=50
    



.. note:: Important fixes to this module were made in pyeapi 0.4.0. Be sure to update to at least that version.
.. note:: All configuration is idempotent unless otherwise specified
.. note:: Supports eos metaparameters for using the eAPI transport
.. note:: Does not support stateful resource configuration.

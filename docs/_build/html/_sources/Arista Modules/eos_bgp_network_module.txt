.. _eos_bgp_network:


eos_bgp_network
+++++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.1.0

This eos_bgp_network module provides stateful management of the network statements for the BGP routing process for Arista EOS nodes

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
    <td style="vertical-align:middle">masklen</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The IPv4 subnet mask length in bits.  The value for the masklen must be in the valid range of 1 to 32.<br>(added in 1.1.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">prefix</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The IPv4 prefix to configure as part of the network statement.  The value must be a valid IPv4 prefix<br>(added in 1.1.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">route_map</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the BGP route-map name to apply to the network statement when configured.  Note this module does not create the route-map<br>(added in 1.1.0)    </td>
    </tr>
        </table><br>


.. important:: Requires Arista EOS 4.13.7M or later with command API enable


.. important:: Requires Python Client for eAPI 0.3.1 or later


Examples
--------

.. raw:: html

    <br/>


::

    
    - name: add network 172.16.10.0/26 with route-map test
      eos_bgp_network: prefix=172.16.10.0 masklen=26 route_map=test
    
    - name: remove network 172.16.0.0/8
      eos_bgp_network: prefix=172.16.0.0 masklen=8 state=absent



.. note:: All configuraiton is idempontent unless otherwise specified
.. note:: Supports eos metaparameters for using the eAPI transport
.. note:: Supports tateful resource configuration

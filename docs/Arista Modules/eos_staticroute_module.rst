.. _eos_staticroute:


eos_staticroute
+++++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.2.0

The eos_staticroute module manages static route configuration options on Arista EOS nodes.

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
    <td style="vertical-align:middle">distance</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">1</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Distance designated for this route<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">ip_dest</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Destination IP address<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">next_hop</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Next hop IP address or egress interface<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">next_hop_ip</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      IP address of the next router. Only valid when next_hop is an egress interface<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">route_name</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Descriptive name for the route<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">tag</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Tag assigned for the route<br>(added in 1.2.0)    </td>
    </tr>
        </table><br>


.. important:: Requires Arista EOS 4.13.7M or later with command API enabled


.. important:: Requires Python Client for eAPI 0.4.0 or later


Examples
--------

.. raw:: html

    <br/>


::

    
    - eos_staticroute: ip_dest=1.1.1.0/24 next_hop=Ethernet1
                       next_hop_ip=1.1.1.1 distance=1
                       tag=15 name=route1
    



.. note:: All configuration is idempotent unless otherwise specified
.. note:: Supports eos metaparameters for using the eAPI transport
.. note:: Supports stateful resource configuration.

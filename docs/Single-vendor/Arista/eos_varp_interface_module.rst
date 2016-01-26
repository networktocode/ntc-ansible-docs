.. _eos_varp_interface:


eos_varp_interface
++++++++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.2.0

This module will manage interface Varp configuration on EOS nodes. Typically this includes Vlan interfaces only by using the ip virtual-router address command.

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
    <td style="vertical-align:middle">name</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The Varp interface which will have the following shared_ip's configured. These are typically Vlan interfaces. The interface name must match the way it is written in the configuration. For example, use Vlan100, not vlan100 or vlan 100.<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">shared_ip</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The list of IP addresses that will be shared in the Varp configuration. The list of IPs should be a string of comma-separated addresses. Please provide a list of sorted IPs.<br>(added in 1.2.0)    </td>
    </tr>
        </table><br>


.. important:: Requires Arista EOS 4.13.7M or later with command API enabled


.. important:: Requires Python Client for eAPI 0.4.0 or later


Examples
--------

.. raw:: html

    <br/>


::

    
    - eos_varp_interface: name=Vlan1000 shared_ip='1.1.1.2,1.1.1.3,1.1.1.4'



.. note:: All configuration is idempotent unless otherwise specified
.. note:: Supports eos metaparameters for using the eAPI transport
.. note:: Does not support stateful resource configuration.

.. _eos_varp:


eos_varp
++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.2.0

This module will manage global Varp configuration on EOS nodes

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
    <td style="vertical-align:middle">mac_address</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The MAC address to assign as the virtual-router mac address. This value must be formatted like aa:bb:cc:dd:ee:ff<br>(added in 1.2.0)    </td>
    </tr>
        </table><br>


.. important:: Requires Arista EOS 4.13.7M or later with command API enabled


.. important:: Requires Python Client for eAPI 0.4.0 or later


Examples
--------

.. raw:: html

    <br/>


::

    
    - eos_varp: mac_address='00:11:22:33:44:55'



.. note:: All configuration is idempotent unless otherwise specified
.. note:: Supports eos metaparameters for using the eAPI transport
.. note:: Does not support stateful resource configuration.

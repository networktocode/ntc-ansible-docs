.. _eos_mlag_interface:


eos_mlag_interface
++++++++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.0.0

The eos_mlag_interface module manages the MLAG interfaces on Arista EOS nodes.  This module is fully stateful and all configuration of resources is idempotent unless otherwise specified.

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
    <td style="vertical-align:middle">mlag_id</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the interface mlag setting to the specified value.  The mlag setting is any valid number from 1 to 2000.  A MLAG identifier cannot be used on more than one interface.<br>(added in 1.0.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">name</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The interface name assocated with this resource.  The interface name must be the full interface identifier.  Valid interfaces match Po*<br>(added in 1.0.0)    </td>
    </tr>
        </table><br>


.. important:: Requires Arista EOS 4.13.7M or later with command API enabled


.. important:: Requires Python Client for eAPI 0.3.0 or later


Examples
--------

.. raw:: html

    <br/>


::

    
    - name: Ensure Ethernet1 is configured with mlag id 10
      eos_mlag_interface: name=Ethernet1 state=present mlag_id=10
    
    - name: Ensure Ethernet10 is not configured as mlag
      eos_mlag_interface: name=Ethernet10 state=absent
    



.. note:: All configuration is idempotent unless otherwise specified
.. note:: Supports eos metaparameters for using the eAPI transport
.. note:: Supports stateful resource configuration.

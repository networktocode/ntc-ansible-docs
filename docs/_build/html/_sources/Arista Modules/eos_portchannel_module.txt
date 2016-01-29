.. _eos_portchannel:


eos_portchannel
+++++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.0.0

The eos_portchannel module manages the interface configuration for logical Port-Channel interfaces on EOS nodes.

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
    <td style="vertical-align:middle">description</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures a one lne ASCII description for the interface.  The EOS default value for description is None<br>(added in 1.0.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">enable</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">True</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>True</li><li>False</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the administrative state for the interface.  Setting the value to true will adminstrative enable the interface and setting the value to false will administratively disable the interface.  The EOS default value for enable is true<br>(added in 1.0.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">lacp_mode</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>active</li><li>passive</li><li>disabled</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the LACP mode configured on the named interface.  The LACP mode identifies the negotiation protocol used between peers.<br>(added in 1.0.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">members</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the set of physical Ethernet interfaces that are bundled together to create the logical Port-Channel interface.  Member interface names should be a comma separated list of physical Ethernet interface names to be included in the named interface.<br>(added in 1.0.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">minimum_links</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Conifugres the minimum links value which specifies the miniumum number of physical Ethernet interfaces that must be operationally up for the entire Port-Channel interface to be considered operationally up.  Valid values for minimum links are in the range of 0 to 16.  The EOS default value for min-links is 0<br>(added in 1.0.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">name</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The unique interface identifier name.  The interface name must use the full interface name (no abbreviated names).  For example, interfaces should be specified as Ethernet1 not Et1<br>(added in 1.0.0)    </td>
    </tr>
        </table><br>


.. important:: Requires Arista EOS 4.13.7M or later with command API enabled


.. important:: Requires Python Client for eAPI 0.3.0 or later


Examples
--------

.. raw:: html

    <br/>


::

    
    - name: Ensure Port-Channel1 has members Ethernet1 and 2
      eos_portchannel: name=Port-Channel1 members=Ethernet1,Ethernet2
    
    - name: Ensure Port-Channel10 uses lacp mode active
      eos_portchannel: name=Port-Channel10 members=Ethernet1,Ethernet3
                       lacp_mode=active



.. note:: All configuration is idempotent unless otherwise specified
.. note:: Supports eos metaparameters for using the eAPI transport
.. note:: Supports stateful resource configuration.

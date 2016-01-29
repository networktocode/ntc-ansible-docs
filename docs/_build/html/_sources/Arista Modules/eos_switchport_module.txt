.. _eos_switchport:


eos_switchport
++++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.0.0

Provides active state management of switchport (layer 2) interface configuration in Arista EOS.  Logical switchports are mutually exclusive with ``eos_ipinterface``.

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
    <td style="vertical-align:middle">access_vlan</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the VLAN associated with a switchport that is configured to use 'access' mode.  This parameter only takes effect if mode is equal to 'access'.  Valid values for access vlan are in the range of 1 to 4094.  The EOS default value for access vlan is 1<br>(added in 1.0.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">mode</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>trunk</li><li>access</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Identifies the mode of operation for the interface.  Switchport interfaces can act as trunk interfaces (carrying multiple VLANs) or as access interfaces (attached to a single VLAN).  The EOS default value is 'access'<br>(added in 1.0.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">name</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The unique interface identifier name.  The interface name must use the full interface name (no abbreviated names).  For example, interfaces should be specified as Ethernet1 not Et1<br>(added in 1.0.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">trunk_allowed_vlans</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the set of VLANs that are allowed to traverse this switchport interface.  This parameter only takes effect if the mode is configured to 'trunk'.  This parameter accepts a comma delimited list of VLAN IDs to configure on the trunk port.  Each VLAN ID must be in the valid range of 1 to 4094.  The EOS default value for trunk allowed vlans is 1-4094.<br>(added in 1.0.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">trunk_groups</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the list of trunk groups on the switchport.  The parameter accepts a comma separated list of values to be provisioned on the interface.<br>(added in 1.1.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">trunk_native_vlan</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the native VLAN on a trunk interface for untagged packets entering the switchport.  This parameter only takes effect if mode is equal to 'trunk'.  Valid values for trunk native vlan are in the range of 1 to 4094.  The EOS default value for trunk native value is 1.<br>(added in 1.0.0)    </td>
    </tr>
        </table><br>


.. important:: Requires Arista EOS 4.13.7M or later with command API enabled


.. important:: Requires Python Client for eAPI 0.3.0 or later


Examples
--------

.. raw:: html

    <br/>


::

    
    - name: Ensure Ethernet1 is an access port
      eos_switchport: name=Ethernet1 mode=access access_vlan=10
    
    - name: Ensure Ethernet12 is a trunk port
      eos_switchport: name=Ethernet12 mode=trunk trunk_native_vlan=100
    
    - name: Add the set of allowed vlans to Ethernet2/1
      eos_switchport: name=Ethernet2/1 mode=trunk trunk_allowed_vlans=1,10,100
    
    - name: Add trunk group values to an interface
      eos_switchport: name=Ethernet5 trunk_groups=foo,bar,baz
    



.. note:: All configuration is idempotent unless otherwise specified
.. note:: Supports eos metaparameters for using the eAPI transport
.. note:: Supports stateful resource configuration.

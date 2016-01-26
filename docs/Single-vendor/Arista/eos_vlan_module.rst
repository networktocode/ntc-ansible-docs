.. _eos_vlan:


eos_vlan
++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.0.0

The eos_vlan module manages VLAN configurations on Arista EOS nodes.

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
    <td style="vertical-align:middle">enable</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">True</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>True</li><li>False</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the administrative state for the VLAN.  If enable is True then the VLAN is administratively enabled.  If enable is False then the VLAN is administratively disabled.<br>(added in 1.0.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">name</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      An ASCII string identifer for this VLAN.  The default value for the VLAN name is VLANxxxx where xxxx is the four digit VLAN ID.<br>(added in 1.0.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">trunk_groups</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the list of trunk groups associated with the VLAN in the node configuration.  The list of trunk groups is a comma separated list.  The default value for trunk_groups is an empty list.<br>Note: The list of comma delimited values must not include spaces.<br>(added in 1.0.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">vlanid</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The unique VLAN identifier associated with this resource.  The value for this identiifer must be in the range of 1 to 4094.<br>(added in 1.0.0)    </td>
    </tr>
        </table><br>


.. important:: Requires Arista EOS 4.13.7M or later with command API enabled


.. important:: Requires Python Client for eAPI 0.3.0 or later


Examples
--------

.. raw:: html

    <br/>


::

    
    - name: ensures vlan 100 is configured
      eos_vlan: vlanid=100 state=present
    
    - name: ensures vlan 200 is not configured
      eos_vlan: vlanid=200 state=absent
    
    - name: configures the vlan name
      eos_vlan: vlanid=1 name=TEST_VLAN_1
    
    - name: configure trunk groups for vlan 10
      eos_vlan: vlanid=10 trunk_groups=tg1,tg2,tg3
    



.. note:: All configuration is idempotent unless otherwise specified
.. note:: Supports eos metaparameters for using the eAPI transport
.. note:: Supports stateful resource configuration.

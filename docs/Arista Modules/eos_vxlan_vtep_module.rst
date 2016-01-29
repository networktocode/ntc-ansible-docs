.. _eos_vxlan_vtep:


eos_vxlan_vtep
++++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.0.0

The eos_vxlan_vtep module manages the Vxlan global VTEP flood list configure on Arista EOS nodes that are operating as VTEPs

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
      The unique interface identifier name.  The interface name must use the full interface name (no abbreviated names).  For example, interfaces should be specified as Ethernet1 not Et1<br>Note: The name parameter only accepts Vxlan1 as the identifier<br>(added in 1.0.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">vlan</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Specifies the VLAN ID to associate the VTEP with.  If the VLAN argument is not used, the the VTEP is confgured on the global flood list.<br>(added in 1.0.1)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">vtep</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Specifes the remote endpoing IP address to add to the global VTEP flood list.  Valid values for the vtep parameter are unicast IPv4 addresses<br>(added in 1.0.0)    </td>
    </tr>
        </table><br>


.. important:: Requires Arista EOS 4.13.7M or later with command API enabled


.. important:: Requires Python Client for eAPI 0.3.0 or later


Examples
--------

.. raw:: html

    <br/>


::

    
    - name: Ensures that 1.1.1.1 is in the global flood list
      eos_vxlan_vtep: name=Vxlan1 state=present vtep=1.1.1.1
    
    - name: Ensures that 2.2.2.2 is not in the global flood list
      eos_vxlan_vtep: name=Vxlan1 state=absent vtep=2.2.2.2
    



.. note:: All configuration is idempotent unless otherwise specified
.. note:: Supports eos metaparameters for using the eAPI transport
.. note:: Supports stateful resource configuration.

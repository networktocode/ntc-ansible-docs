.. _eos_stp_interface:


eos_stp_interface
+++++++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.0.0

Provides active state management of STP interface configuration on Arista EOS nodes.

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
    <td style="vertical-align:middle">bpduguard</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>True</li><li>False</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Specifies whether or not bpduguard should be enabled on the named interface.  If this value is configured true, then bpduguard is enabled on the interface.  If this value is configured false, then bpduguard is disabled on the interface.  The EOS default value for bpduguard is false<br>(added in 1.0.0)    </td>
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
    <td style="vertical-align:middle">portfast</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>True</li><li>False</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Specifies whether or not portfast should be enabled on the named interface.  If this value is configured true, then portfast is enabled on the interface.  If this value is configured false, then portfast is disabled on the interface.  The EOS default value for portfast is false<br>(added in 1.0.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">portfast_type</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>edge</li><li>network</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the portfast port type value for the named interface in EOS.  Valid port types include edge or network.<br>(added in 1.0.0)    </td>
    </tr>
        </table><br>


.. important:: Requires Arista EOS 4.13.7M or later with command API enabled


.. important:: Requires Python Client for eAPI 0.3.0 or later


Examples
--------

.. raw:: html

    <br/>


::

    
    - name: Ensure portfast is enabled on Ethernet3
      eos_stp_interface: name=Ethernet3 portfast=yes
    
    - name: Ensure bpduguard is enabled on Ethernet49
      eos_stp_interface: name=Ethernet49 bpduguard=yes
    



.. note:: All configuration is idempotent unless otherwise specified
.. note:: Supports eos metaparameters for using the eAPI transport
.. note:: Does not support stateful resource configuration.

.. _eos_config:


eos_config
++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.0.0

The eos_config module evalues the current configuration for specific commands.  If the commands are either present or absent (depending on the function argument, the eos_config module will configure the node using the command argument.

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
    <td style="vertical-align:middle">command</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Specifies the configuration command to send to the node if the expression does not evalute to true.<br>(added in 1.0.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">regexp</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Specifies the expression to evalute the current node's running configuration.  The value can be any valid regular expression. This optional argument will default to use the command argument if none is provided.<br>(added in 1.1.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">section</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Restricts the configuration evaluation to a single configuration section.  If the configuration section argument is not provided, then the global configuration is used.<br>(added in 1.0.0)    </td>
    </tr>
        </table><br>


.. important:: Requires Arista EOS 4.13.7M or later with command API enabled


.. important:: Requires Python Client for eAPI 0.3.0 or later


Examples
--------

.. raw:: html

    <br/>


::

    
    - name: idempotent operation for removing a SVI
      eos_config:
        command='no interface Vlan100'
        regexp='interface Vlan100'
        state=absent
    
    - name: non-idempotent operation for removing a SVI
      eos_config:
        command='no interface Vlan100'
    
    - name: ensure default route is present
      eos_config:
        command='ip route 0.0.0.0/0 192.168.1.254'
    
    - name: configure interface range to be shutdown if it isn't already
      eos_config:
        command='shutdown'
        regexp='(?<=[^no ] )shutdown'
        section='interface {{ item }}'
      with_items:
        - Ethernet1
        - Ethernet2
        - Ethernet3
    



.. note:: This module does not support idempotent operations.
.. note:: Supports eos metaparameters for using the eAPI transport
.. note:: This module does not support stateful configuration

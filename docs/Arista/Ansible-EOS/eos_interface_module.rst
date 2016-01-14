.. _eos_interface:


eos_interface
+++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.0.0

The eos_interface module manages the interface configuration for any valid interface on EOS nodes.

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

    
    - name: ensures the interface is configured
      eos_interface: name=Loopback0 state=present enable=yes
    
    - name: ensures the interface is not configured
      eos_interface: name=Loopback1 state=absent
    



.. note:: All configuration is idempotent unless otherwise specified
.. note:: Supports eos metaparameters for using the eAPI transport
.. note:: Supports stateful resource configuration.

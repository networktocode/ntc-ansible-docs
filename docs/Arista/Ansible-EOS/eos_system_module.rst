.. _eos_system:


eos_system
++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.0.0

The eos_system module manages global system configuration options on Arista EOS nodes.

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
    <td style="vertical-align:middle">hostname</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The ASCII string to use to configure the hostname value in the nodes current running-configuration.  The EOS default value for hostname is 'localhost'<br>(added in 1.0.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">ip_routing</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>true</li><li>false</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the state of IPv4 'ip routing' on the switch. By default EOS switches come up with 'no ip routing'. This attribute requires pyeapi version 0.4.0.<br>(added in 1.2.0)    </td>
    </tr>
        </table><br>


.. important:: Requires Arista EOS 4.13.7M or later with command API enabled


.. important:: Requires Python Client for eAPI 0.3.0 or later


Examples
--------

.. raw:: html

    <br/>


::

    
    - name: configures the hostname to spine01
      eos_system: hostname=spine01
    



.. note:: All configuration is idempotent unless otherwise specified
.. note:: Supports eos metaparameters for using the eAPI transport
.. note:: Supports stateful resource configuration.

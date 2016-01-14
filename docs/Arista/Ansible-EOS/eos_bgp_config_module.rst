.. _eos_bgp_config:


eos_bgp_config
++++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.1.0

The eos_bgp_config module provides resource management of the global BGP routing process for Arista EOS nodes

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
    <td style="vertical-align:middle">bgp_as</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The BGP autonomous system number to be configured for the local BGP routing instance.  The value must be in the valid BGP AS range of 1 to 65535.<br>(added in 1.1.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">enable</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">True</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>True</li><li>False</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the administrative state for the global BGP routing process. If enable is True then the BGP routing process is administartively enabled and if enable is False then the BGP routing process is administratively disabled.<br>(added in 1.1.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">maximum_ecmp_paths</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the maximum number of ecmp paths for each route. The EOS default for this attribute is the maximum value, which varies by hardware platform. Check your Arista documentation for more information. This value should be greater than or equal to maximum_paths.<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">maximum_paths</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the maximum number of parallel routes. The EOS default for this attribute is 1. This value should be less than or equal to maximum_ecmp_paths.<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">router_id</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the BGP routing process router-id value.  The router id must be in the form of A.B.C.D<br>(added in 1.1.0)    </td>
    </tr>
        </table><br>


.. important:: Requires Arista EOS 4.13.7M or later with command API enable


.. important:: Requires Python Client for eAPI 0.4.0 or later


Examples
--------

.. raw:: html

    <br/>


::

    
    - name: enable BGP routing with AS 65535
      eos_bgp_config: bgp_as=65535 state=present enable=yes
    
    - name: disable the BGP routing process
      eos_bgp_config: bgp_as=65535 enable=no
    
    - name: configure the BGP router-id
      eos_bgp_config: bgp_as=65535 router_id=1.1.1.1
    
    - name: configure the BGP with just max paths
      eos_bgp_config: bgp_as=65535 router_id=1.1.1.1 maximum_paths=20
    
    - name: configure the BGP with maximum_paths and maximum_ecmp_paths
      eos_bgp_config: bgp_as=65535 router_id=1.1.1.1 maximum_paths=20
      maximum_ecmp_paths=20



.. note:: All configuraiton is idempontent unless otherwise specified
.. note:: Supports eos metaparameters for using the eAPI transport
.. note:: Supports tateful resource configuration

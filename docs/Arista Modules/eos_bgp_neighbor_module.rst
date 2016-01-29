.. _eos_bgp_neighbor:


eos_bgp_neighbor
++++++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.1.0

This eos_bgp_neighbor module provides stateful management of the neighbor statements for the BGP routing process for Arista EOS nodes

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
      Configures the BGP neighbors description value.  The value specifies an arbitrary description to add to the neighbor statement in the nodes running-configuration.<br>(added in 1.1.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">enable</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">True</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>True</li><li>False</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the administrative state for the BGP neighbor process. If enable is True then the BGP neighbor process is administartively enabled and if enable is False then the BGP neighbor process is administratively disabled.<br>(added in 1.1.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">name</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The name of the BGP neighbor to manage.  This value can be either an IPv4 address or string (in the case of managing a peer group)<br>(added in 1.1.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">next_hop_self</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the BGP neighbors next-hop-self value.  If enabled then the BGP next-hop-self value is enabled.  If disabled, then the BGP next-hop-self community value is disabled.<br>(added in 1.1.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">peer_group</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The name of the peer-group value to associate with the neighbor.  This argument is only valid if the neighbor is an IPv4 address<br>(added in 1.1.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">remote_as</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the BGP neighbors remote-as value.  Valid AS values are in the range of 1 to 65535.<br>(added in 1.1.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">route_map_in</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the BGP neigbhors route-map in value.  The value specifies the name of the route-map.<br>(added in 1.1.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">route_map_out</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the BGP neigbhors route-map out value.  The value specifies the name of the route-map.<br>(added in 1.1.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">send_community</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the BGP neighbors send-community value.  If enabled then the BGP send-community value  is enable.  If disabled, then the BGP send-community value is disabled.<br>(added in 1.1.0)    </td>
    </tr>
        </table><br>


.. important:: Requires Arista EOS 4.13.7M or later with command API enable


.. important:: Requires Python Client for eAPI 0.3.1 or later


Examples
--------

.. raw:: html

    <br/>


::

    
    - name: add neighbor 172.16.10.1 to BGP
      eos_bgp_neighbor: name=172.16.10.1 enable=yes remote_as=65000
    
    - name: remove neighbor 172.16.10.1 to BGP
      eos_bgp_neighbor name=172.16.10.1 enable=yes remote_as=65000 state=absent



.. note:: All configuraiton is idempontent unless otherwise specified
.. note:: Supports eos metaparameters for using the eAPI transport
.. note:: Supports tateful resource configuration

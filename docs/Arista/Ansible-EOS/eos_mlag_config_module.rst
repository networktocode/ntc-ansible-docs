.. _eos_mlag_config:


eos_mlag_config
+++++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.0.0

The eos_mlag_interface module manages the MLAG interfaces on Arista EOS nodes.  This module is fully stateful and all configuration of resources is idempotent unless otherwise specified.

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
    <td style="vertical-align:middle">domain_id</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the global MLAG domain-id value on the EOS node.  The domain-id specifies the name the for MLAG domain.  Valid values for domain-id is any ASCII string.<br>(added in 1.0.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">local_interface</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the VLAN interface (SVI) for use as the MLAG endpoint for control traffic.  Valid values for local-interface is any VLAN SVI identifier.<br>(added in 1.0.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">peer_address</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the global MLAG peer-address of the MLAG peer.  This peer address must be reachable by the configured local-interface.  Valid values are any IPv4 unicast IP address.<br>(added in 1.0.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">peer_link</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the physical link that connects the local MLAG to its remote peer node.  The physical link value can be any valid Ethernet or Port-Channel interface<br>(added in 1.0.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">shutdown</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>True</li><li>False</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the global MLAG administratively state.  If the value of shutdown is true, then MLAG is administratively disabled.  If the value of shutdown is false, then MALG is administratively enabled.  The EOS default value for shutdown is false.<br>(added in 1.0.0)    </td>
    </tr>
        </table><br>


.. important:: Requires Arista EOS 4.13.7M or later with command API enabled


.. important:: Requires Python Client for eAPI 0.3.0 or later


Examples
--------

.. raw:: html

    <br/>


::

    
    - name: Ensure the MLAG domain-id is mlagPeer
      eos_mlag_config: domain_id=mlagPeer
    
    - name: Configure the peer address and local interface
      eos_mlag_config: peer_address=2.2.2.2 local_interface=Vlan4094
    



.. note:: All configuration is idempotent unless otherwise specified
.. note:: Supports eos metaparameters for using the eAPI transport
.. note:: Does not support stateful resource configuration.

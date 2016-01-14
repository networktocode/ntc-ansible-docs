.. _eos_vrrp:


eos_vrrp
++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.2.0

This module will manage VRRP configurations on EOS nodes

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
    <td style="vertical-align:middle">delay_reload</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Delay between switch reload and VRRP initialization<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">description</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Text description of the virtual router<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">enable</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">True</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>True</li><li>False</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The state of the VRRP<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">interface</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The interface on which the VRRP is configured<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">ip_version</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">2</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>2</li><li>3</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      VRRP version in place on the virtual router<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">mac_addr_adv_interval</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">30</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Interval between advertisement messages to virtual router group<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">preempt</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">True</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>True</li><li>False</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Preempt mode setting for the virtual router<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">preempt_delay_min</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Interval between a preempt event and takeover<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">preempt_delay_reload</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Interval between a preempt event and takeover after reload<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">primary_ip</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">0.0.0.0</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The ip address of the virtual router<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">priority</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">100</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The priority setting for the virtual router<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">secondary_ip</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Array of secondary ip addresses assigned to the VRRP<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">timers_advertise</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">1</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Interval between advertisement messages to virtual router group<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">track</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Array of track definitions to be assigned to the vrrp<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">vrid</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The unique identifying ID of the VRRP on its interface<br>(added in 1.2.0)    </td>
    </tr>
        </table><br>


.. important:: Requires Arista EOS 4.13.7M or later with command API enabled


.. important:: Requires Python Client for eAPI 0.4.0 or later


Examples
--------

.. raw:: html

    <br/>


::

    
    # Configure the set of tracked objects for the VRRP
    # Create a list of dictionaries, where name is the object to be
    # tracked, action is shutdown or decrement, and amount is the
    # decrement amount. Amount is not specified when action is shutdown.
    
    vars:
      tracks:
          - name: Ethernet1
            action: shutdown
          - name: Ethernet2
            action: decrement
            amount: 5
    
    # Setup the VRRP
    
      - eos_vrrp:
          interface=Vlan70
          vrid=10
          enable=True
          primary_ip=10.10.10.1
          priority=50
          description='vrrp 10 on Vlan70'
          ip_version=2
          secondary_ip=['10.10.10.70','10.10.10.80']
          timers_advertise=15
          preempt=True
          preempt_delay_min=30
          preempt_delay_reload=30
          delay_reload=30
          track="{{ tracks }}"
    



.. note:: All configuration is idempotent unless otherwise specified
.. note:: Supports eos metaparameters for using the eAPI transport
.. note:: Supports stateful resource configuration.

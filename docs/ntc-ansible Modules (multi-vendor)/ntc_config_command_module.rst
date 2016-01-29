.. _ntc_config_command:


ntc_config_command
++++++++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------


This module write config data to devices that don't have an API. The use case would be writing configuration based on output gleaned from ntc_show_command output.

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
    <td style="vertical-align:middle">commands</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Command to execute on target device<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">commands_file</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Command to execute on target device<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">connection</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">ssh</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>ssh</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      connect to device using netmiko or read from offline file for testing<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">host</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      IP Address or hostname (resolvable by Ansible control host)<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">password</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Password used to login to the target device<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">platform</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle">ssh</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Platform FROM the index file<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">port</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">22</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      SSH port to use to connect to the target device<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">secret</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Password used to enter a privileged mode on the target device<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">username</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Username used to login to the target device<br>    </td>
    </tr>
        </table><br>


.. important:: Requires netmiko


Examples
--------

.. raw:: html

    <br/>


::

    
    # write vlan data
    - ntc_config_command:
        connection: ssh
        platform: cisco_nxos
        commands:
          - vlan 10
          - name vlan_10
          - end
        host: "{{ inventory_hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        secret: "{{ secret }}"
    
    # write config from file
    - ntc_config_command:
        connection: ssh
        platform: cisco_nxos
        commands_file: "dynamically_created_config.txt"
        host: "{{ inventory_hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        secret: "{{ secret }}"




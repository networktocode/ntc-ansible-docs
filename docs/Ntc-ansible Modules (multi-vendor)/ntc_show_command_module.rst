.. _ntc_show_command:


ntc_show_command
++++++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------


This module offers structured data for CLI enabled devices by using the TextFSM library for templating and netmiko for SSH connectivity

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
      Command to execute on target device<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">connection</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">ssh</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>ssh</li><li>offline</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      connect to device using netmiko or read from offline file for testing<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">delay</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">1</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Wait for command output from target device<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">file</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      If using connection=offline, this is the file (with path) of a file that contains raw text output, i.e. 'show command' and then the contents of the file will be rendered with the the TextFSM template<br>    </td>
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
    <td style="vertical-align:middle">index_file</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">index</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      name of index file.  file location must be relative to the template_dir<br>    </td>
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
    <td style="vertical-align:middle">template_dir</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">ntc_templates</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      path where TextFSM templates are stored. Default path is ntc with ntc in the same working dir as the playbook being run<br>    </td>
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


.. important:: Requires textfsm


.. important:: Requires terminal


Examples
--------

.. raw:: html

    <br/>


::

    
    # get vlan data
    - ntc_show_command:
        connection=ssh
        platform=cisco_nxos
        command='show vlan'
        host={{ inventory_hostname }}
        username={{ username }}
        password={{ password }}
    
    # get snmp community
    - ntc_show_command:
        connection=ssh
        platform=cisco_nxos
        command='show snmp community'
        host={{ inventory_hostname }}
        username={{ username }}
        password={{ password }}
        secret:{{ secret }}
    




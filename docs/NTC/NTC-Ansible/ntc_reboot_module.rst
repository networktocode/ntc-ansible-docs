.. _ntc_reboot:


ntc_reboot
++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.9.2

Reboot a network device, optionally on a timer.
Supported platforms include Cisco Nexus switches with NX-API, Cisco IOS switches or routers, Arista switches with eAPI.

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
    <td style="vertical-align:middle">confirm</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Safeguard boolean. Set to true if you're sure you want to reboot.<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">host</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Hostame or IP address of switch.<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">ntc_conf_file</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The path to a local NTC configuration file. If omitted, and ntc_host is specified, the system will look for a file given by the path in the environment variable PYNTC_CONF, and then in the users home directory for a file called .ntc.conf.<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">ntc_host</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The name of a host as specified in an NTC configuration file.<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">password</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Password used to login to the target device<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">platform</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>cisco_nxos_nxapi</li><li>arista_eos_eapi</li><li>cisco_ios</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Switch platform<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">port</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      TCP/UDP port to connect to target device. If omitted standard port numbers will be used. 80 for HTTP; 443 for HTTPS; 22 for SSH.<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">secret</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Enable secret for devices connecting over SSH.<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">timer</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Time in minutes after which the device will be rebooted.<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">transport</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">https</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>http</li><li>https</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Transport protocol for API-based devices.<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">username</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Username used to login to the target device<br>    </td>
    </tr>
        </table><br>


.. important:: Requires pyntc


Examples
--------

.. raw:: html

    <br/>


::

    - ntc_reboot:
        platform: cisco_nxos_nxapi
        confirm: true
        host: "{{ inventory_hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        transport: http
    
    - ntc_reboot:
        ntc_host: n9k1
        ntc_conf_file: .ntc.conf
        confirm: true
    
    - ntc_file_copy:
        platform: arista_eos_eapi
        confirm: true
        host: "{{ inventory_hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
    
    - ntc_file_copy:
        platform: cisco_ios
        confirm: true
        timer: 5
        host: "{{ inventory_hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        secret: "{{ secret }}"


Return Values
-------------

Common return values are documented here :doc:`common_return_values`, the following are the fields unique to this module:

.. raw:: html

    <table border=1 cellpadding=4>
    <tr>
    <th class="head">name</th>
    <th class="head">despcription</th>
    <th class="head">returned</th>
    <th class="head">type</th>
    <th class="head">sample</th>
    </tr>

        <tr>
        <td> rebooted </td>
        <td> Whether the device was instructed to reboot. </td>
        <td align=center> success </td>
        <td align=center> boolean </td>
        <td align=center> True </td>
    </tr>
        
    </table>
    </br></br>


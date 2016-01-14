.. _ntc_get_facts:


ntc_get_facts
+++++++++++++

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
    <td style="vertical-align:middle">host</td>
    <td style="vertical-align:middle">no</td>
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
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Password used to login to the target device<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">platform</td>
    <td style="vertical-align:middle">no</td>
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
    <td style="vertical-align:middle">transport</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">https</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>http</li><li>https</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Transport protocol for API-based devices.<br>    </td>
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


.. important:: Requires pyntc


Examples
--------

.. raw:: html

    <br/>


::

    - ntc_get_facts:
        platform: cisco_nxos_nxapi
        host: "{{ inventory_hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        transport: http
    
    - ntc_get_facts:
        ntc_host: n9k1
        ntc_conf_file: .ntc.conf
    
    - ntc_get_facts:
        ntc_host: eos_leaf
    
    - ntc_get_facts:
        platform: arista_eos_eapi
        host: "{{ inventory_hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
    
    - ntc_get_facts:
        platform: cisco_ios
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
        <td> uptime </td>
        <td> The device uptime represented as an integer number of strings. </td>
        <td align=center> success </td>
        <td align=center> int </td>
        <td align=center> 1313 </td>
    </tr>
            <tr>
        <td> vendor </td>
        <td> Vendor of network device. </td>
        <td align=center> success </td>
        <td align=center> string </td>
        <td align=center> cisco </td>
    </tr>
            <tr>
        <td> uptime_string </td>
        <td> The device uptime represented as a string format DD:HH:MM:SS. </td>
        <td align=center> success </td>
        <td align=center> string </td>
        <td align=center> 00:00:21:53 </td>
    </tr>
            <tr>
        <td> interfaces </td>
        <td> List of interfaces. </td>
        <td align=center> success </td>
        <td align=center> list </td>
        <td align=center> ['mgmt0', 'Ethernet1/1', 'Ethernet1/2', 'Ethernet1/3', 'Ethernet1/4', 'Ethernet1/5', 'Ethernet1/6'] </td>
    </tr>
            <tr>
        <td> hostname </td>
        <td> Hostname of network device. </td>
        <td align=center> success </td>
        <td align=center> string </td>
        <td align=center> N9K1 </td>
    </tr>
            <tr>
        <td> fqdn </td>
        <td> Fully-qualified domain name. </td>
        <td align=center> success </td>
        <td align=center> string </td>
        <td align=center> N9K1.ntc.com </td>
    </tr>
            <tr>
        <td> os_version </td>
        <td> Operating System version on network device. </td>
        <td align=center> success </td>
        <td align=center> string </td>
        <td align=center> 7.0(3)I2(1) </td>
    </tr>
            <tr>
        <td> serial_number </td>
        <td> Serial number on network device. </td>
        <td align=center> success </td>
        <td align=center> string </td>
        <td align=center> SAL1819S6LU </td>
    </tr>
            <tr>
        <td> model </td>
        <td> Hardware model of network device. </td>
        <td align=center> success </td>
        <td align=center> string </td>
        <td align=center> Nexus9000 C9396PX Chassis </td>
    </tr>
            <tr>
        <td> vlans </td>
        <td> List of VLAN IDs. </td>
        <td align=center> success </td>
        <td align=center> List </td>
        <td align=center> ['1', '2', '3', '4'] </td>
    </tr>
        
    </table>
    </br></br>

.. note:: Facts to be returned include - uptime (string), uptime (seconds), model, vendor, os_version, serial_number, hostname, fqdn, vlans, interfaces.
.. note:: Facts are automatically added to Ansible facts environment. No need to register them.

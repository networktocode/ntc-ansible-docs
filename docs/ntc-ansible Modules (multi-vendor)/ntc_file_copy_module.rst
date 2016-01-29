.. _ntc_file_copy:


ntc_file_copy
+++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.9.2

Copy a file to the flash (or bootflash) remote network device on supported platforms over SCP.
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
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Hostame or IP address of switch.<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">local_file</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Path to local file. Local directory must exist.<br>    </td>
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
    <td style="vertical-align:middle">remote_file</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Remote file path to be copied to flash. Remote directories must exist. If omitted, the name of the local file will be used.<br>    </td>
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
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>http</li><li>https</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Transport protocol for API-based devices. Not used for actual file transfer.<br>    </td>
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

    - ntc_file_copy:
        platform: cisco_nxos_nxapi
        local_file: /path/to/file
        host: "{{ inventory_hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        transport: http
    - ntc_file_copy:
        ntc_host: n9k1
        ntc_conf_file: .ntc.conf
        local_file: /path/to/file
    - ntc_file_copy:
        ntc_host: eos_leaf
        local_file: /path/to/file
    - ntc_file_copy:
        platform: arista_eos_eapi
        local_file: /path/to/file
        remote_file: /path/to/remote_file
        host: "{{ inventory_hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
    - ntc_file_copy:
        platform: cisco_ios
        local_file: "{{ local_file_1 }}"
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
        <td> local_file </td>
        <td> The path of the local file. </td>
        <td align=center> success </td>
        <td align=center> string </td>
        <td align=center> /path/to/local/file </td>
    </tr>
            <tr>
        <td> remote_file </td>
        <td> The path of the remote file. </td>
        <td align=center> success </td>
        <td align=center> string </td>
        <td align=center> /path/to/remote/file </td>
    </tr>
            <tr>
        <td> transfer_status </td>
        <td> Whether a file was transfered. "No Transfer" or "Sent". </td>
        <td align=center> success </td>
        <td align=center> string </td>
        <td align=center> Sent </td>
    </tr>
        
    </table>
    </br></br>

.. note:: On NXOS, the feature must be enabled with feature scp-server.
.. note:: On IOS and Arista EOS, the user must be at privelege 15.
.. note:: If the file is already present (md5 sums match), no transfer will take place.
.. note:: Check mode will tell you if the file would be copied.
.. note:: The same user credentials are used on the API/SSH channel and the SCP file transfer channel.

.. _junos_zeroize:


junos_zeroize
+++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.0.0

Execute the Junos OS **request system zeroize** command to remove all configuration information on the Routing Engines and reset all key values on a device running Junos OS. The command removes all data files, including customized configuration and log files, by unlinking the files from their directories. The command also removes all user-created files from the system including all plain-text passwords, secrets, and private keys for SSH, local encryption, local authentication, IPsec, RADIUS, TACACS+, and SNMP.
This command reboots the device and sets it to the factory default configuration. After the reboot, you must log in through the console as root in order to access the device.

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
    <td style="vertical-align:middle">console</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">None</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      SERIAL or TERMINAL-SERVER port setting, per use with the <b>netconify</b> utility<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">host</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Set to {{ inventory_hostname }}<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">logfile</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">None</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Path on the local server where the progress status is logged for debugging purposes<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">passwd</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">assumes ssh-key active</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Login password<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">port</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">830</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      TCP port number to use when connecting to the device<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">user</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">$USER</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Login username<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">zeroize</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle">None</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Safety mechanism. You <b>MUST</b> set this to 'zeroize'.<br>    </td>
    </tr>
        </table><br>


.. important:: Requires junos-eznc >= 1.2.2


.. important:: Requires junos-netconify >= 1.0.1, when using the *console* option


Examples
--------

.. raw:: html

    <br/>


::

    - junos_zeroize:
        host={{ inventory_hostname }}
        zeroize="zeroize"



.. note:: You **MUST** either use the *host* option or the *console* option to designate how the device is accessed.

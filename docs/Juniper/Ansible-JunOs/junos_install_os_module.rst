.. _junos_install_os:


junos_install_os
++++++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.0.0

Install a Junos OS image on one or more Routing Engines. This module supports installations on single Routing Engine devices, MX Series routers with dual Routing Engines, and EX Series switches in a non-mixed Virtual Chassis. This action is equivalent to performing the Junos OS **request system software add** operational command.
If the existing Junos OS version matches the desired version, no action is performed, and the "changed" attribute reports False. If the existing version does not match, then the module performs the following actions
(1) Computes the MD5 checksum of the package located on the server. (2) Copies the Junos OS software package to the device running Junos OS. (3) Computes the MD5 checksum on the device running Junos OS and compares the two. (4) Installs the Junos OS software package. (5) Reboots the device (default).
Running the module in check mode reports whether the current Junos OS version matches the desired version.

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
    <td style="vertical-align:middle">no_copy</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>true</li><li>false</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Installer need to be copied or not on the device.<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">package</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Absolute path on the local server to the Junos OS software package<br>    </td>
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
    <td style="vertical-align:middle">reboot</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">True</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>yes</li><li>no</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      If set to <b>yes</b>, the device reboots after the installation completes.<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">reboot_pause</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">10</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Amount of time in seconds to wait after the reboot is issued<br>    </td>
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
    <td style="vertical-align:middle">version</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Junos OS version string as it would be reported by the <b>show version</b> command<br>    </td>
    </tr>
        </table><br>


.. important:: Requires py-junos-eznc >= 1.2.2


Examples
--------

.. raw:: html

    <br/>


::

    - junos_install_os:
        host={{ inventory_hostname }}
        version=12.1X46-D10.2
        package=/usr/local/junos/images/junos-vsrx-12.1X46-D10.2-domestic.tgz
        logfile=/usr/local/junos/log/software.log




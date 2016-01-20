.. _ntc_install_os:


ntc_install_os
++++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.9.2

Set boot options like boot image and kickstart image.
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
    <td style="vertical-align:middle">kickstart_image_file</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Name of the kickstart image file on flash.<br>    </td>
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
    <td style="vertical-align:middle">system_image_file</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Name of the system (or combined) image file on flash.<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">transport</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
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

    - ntc_install_os:
        ntc_host: n9k1
        system_image_file: n9000-dk9.6.1.2.I3.1.bin
    
    - ntc_install_os:
        ntc_host: n3k1
        system_image_file: n3000-uk9.6.0.2.U6.5.bin
        kickstart_image_file: n3000-uk9-kickstart.6.0.2.U6.5.bin
    
    - ntc_install_os:
        ntc_host: c2801
        system_image_file: c2800nm-adventerprisek9_ivs_li-mz.151-3.T4.bin


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
        <td> install_state </td>
        <td>  </td>
        <td align=center> always </td>
        <td align=center> dictionary </td>
        <td align=center> {'sys': 'n5000-uk9.7.2.1.N1.1.bin', 'status': 'This is the log of last installation.\nContinuing with installation process, please wait.\nThe login will be disabled until the installation is completed.\nPerforming supervisor state verification.\nSUCCESS\nSupervisor non-disruptive upgrade successful.\nInstall has been successful. ', 'kick': 'n5000-uk9-kickstart.7.2.1.N1.1.bin'} </td>
    </tr>
        <tr><td>contains: </td>
    <td colspan=4>
        <table border=1 cellpadding=2>
        <tr>
        <th class="head">name</th>
        <th class="head">despcription</th>
        <th class="head">returned</th>
        <th class="head">type</th>
        <th class="head">sample</th>
        </tr>

        
        </table>
    </td></tr>

        
    </table>
    </br></br>

.. note:: Do not include full file paths, just the name of the file(s) stored on the top level flash directory.
.. note:: You must know if your platform supports taking a kickstart image as a parameter. If supplied but not supported, errors may occur.
.. note:: It may be useful to use this module in conjuction with ntc_file_copy and ntc_reboot.
.. note:: With NXOS devices, this module attempts to install the software immediately, wich may trigger a reboot.
.. note:: With NXOS devices, install process may take up to 10 minutes, especially if the device reboots.
.. note:: Tested on Nexus 3000, 5000, 9000.
.. note:: In check mode, the module tells you if the current boot images are set to the desired images.

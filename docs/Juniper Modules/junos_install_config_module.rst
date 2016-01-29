.. _junos_install_config:


junos_install_config
++++++++++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.0.0

Load a complete Junos OS configuration (overwrite) or merge a configuration snippet onto a device running Junos OS and commit it. The default behavior is to perform a **load merge** operation (overwrite='no'). This module performs an atomic lock/edit/unlock. If the process fails at any step, then all configuration changes are discarded. You can load the configuration using either NETCONF or the CONSOLE port. Specify the *console* option to use the CONSOLE port.
You provide the configuration data in a file. Supported formats when using NETCONF include ASCII text, Junos XML elements, and Junos OS **set** commands. Configurations performed through the console must only use ASCII text formatting.

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
    <td style="vertical-align:middle">comment</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">None</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Provide a comment to the commit of the configuration<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">confirm</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">None</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Provide a confirm in minutes to the commit of the configuration<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">console</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">None</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Port configuration, per the <b>netconify</b> utility<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">diffs_file</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">None</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Path to the file where any diffs will be written<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">file</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Path to the file containing the Junos OS configuration data. If the file has a <code>*.conf</code> extension, the content is treated as text format. If the file has a <code>*.xml</code> extension, the content is treated as XML format. If the file has a <code>*.set</code> extension, the content is treated as Junos OS <b>set</b> commands.<br>    </td>
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
    <td style="vertical-align:middle">overwrite</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>true</li><li>false</li><li>yes</li><li>no</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Specify whether the configuration <em>file</em> completely replaces the existing configuration.<br>    </td>
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
    <td style="vertical-align:middle">replace</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>true</li><li>false</li><li>yes</li><li>no</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Specify whether the configuration <em>file</em> uses "replace:" statements. (NETCONF only) <b>NOT</b> compatible with <b>set</b> format<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">savedir</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">None</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Path to the local server directory where device facts and inventory files will be stored. This option is used only with the <em>console</em> option. Refer to the <b>netconify</b> utility for details.<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">timeout</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">0</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Extend the NETCONF RPC timeout beyond the default value of 30 seconds. Set this value to accommodate configuration changes (commits) that might take longer than the default timeout interval.<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">user</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">$USER</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Login username<br>    </td>
    </tr>
        </table><br>


.. important:: Requires junos-eznc >= 1.2.2


.. important:: Requires junos-netconify >= 1.0.1, when using the *console* option


Examples
--------

.. raw:: html

    <br/>


::

    # load merge a change to the Junos OS configuration using NETCONF
    
    - junos_install_config:
        host={{ inventory_hostname }}
        file=banner.conf
    
    # load overwrite a new Junos OS configuration using the CONSOLE port
    
    - junos_install_config:
        host={{ inventory_hostname }}
        console="--telnet={{TERMSERV}},{{TERMSERV_PORT}}"
        file=default_new_switch.conf
        overwrite=yes
    
    # load merge a change to the Junos OS configuration using NETCONF and supplying a commit log message
    - junos_install_config:
        host={{ inventory_hostname }}
        file=banner.conf
        comment="configured by ansible"
    
    # load replace a change to the Junos OS configuration using NETCONF
    - junos_install_config:
        host={{ inventory_hostname }}
        file=snmp.conf
        replace=yes




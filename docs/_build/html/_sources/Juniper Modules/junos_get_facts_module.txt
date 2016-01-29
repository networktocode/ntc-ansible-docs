.. _junos_get_facts:


junos_get_facts
+++++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.0.0

Retrieve facts for a device running Junos OS, which includes information such as the serial number, product model, and Junos OS version. The module supports using both NETCONF and CONSOLE-based retrieval and returns the information as a JSON dictionary. The information is similar to facts gathered by other IT frameworks.

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
      CONSOLE port, per the <b>netconify</b> utility<br>    </td>
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
      Path on the local server where the progress status is logged for debugging purposes. This option is used only with the <em>console</em> option.<br>    </td>
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
    <td style="vertical-align:middle">savedir</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">$CWD</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Path to the local server directory where device fact files will be stored. Resulting file will be <em>savedir/hostname-facts.json</em><br>    </td>
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

    # retrieve facts using NETCONF, assumes ssh-keys
    
    - junos_get_facts: host={{ inventory_hostname }}
      register: junos
    
    # retrieve facts using CONSOLE, assumes Amnesiac system
    # root login, no password
    
    - junos_get_facts:
        host={{ inventory_hostname }}
        user=root
        console="--telnet={{TERMSERV}},{{TERMSERVPORT}}"
        savedir=/usr/local/junos/inventory
      register: junos
    
    # access the facts
    
    - name: version
      debug: msg="{{ junos.facts.version }}"




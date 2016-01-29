.. _snmp_device_version:


snmp_device_version
+++++++++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------


Returns vendor, os and version of an SNMP device.

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
    <td style="vertical-align:middle">authkey</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Authentication key, required if version is 3<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">community</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The SNMP community string, required if version is 2c<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">host</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Typically set to {{ inventory_hostname }}<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">integrity</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>md5</li><li>sha</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Hashing algoritm, required if version is 3<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">level</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>authPriv</li><li>authNoPriv</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Authentication level, required if version is 3<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">port</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">161</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      SNMP port number<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">privacy</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>des</li><li>3des</li><li>aes</li><li>aes192</li><li>aes256</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Encryption algoritm, required if level is authPriv<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">privkey</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Encryption key, required if version is authPriv<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">username</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Username for SNMPv3, required if version is 3<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">version</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>2c</li><li>3</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      SNMP Version to use, 2c or 3<br>    </td>
    </tr>
        </table><br>


.. important:: Requires nelsnmp


Examples
--------

.. raw:: html

    <br/>


::

    # Get device info with SNMPv2
    - snmp_device_version: host={{ inventory_hostname }} version=2c community=public
    
    # Get device info with SNMPv3
    - cisco_snmp_save_config:
        host={{ inventory_hostname }}
        version=3
        level=authPriv
        integrity=sha
        privacy=aes
        username=snmp-user
        authkey=abc12345
        privkey=def6789




.. _ntc_rollback:


ntc_rollback
++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------


This module offers the ability to set a configuration checkpoint file or rollback to a configuration checkpoint file on supported Cisco or Arista switches.
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
    <td style="vertical-align:middle">checkpoint_file</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Name of checkpoint file to create. Mutually exclusive with rollback_to.<br>    </td>
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
      Password used to login to the target device.<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">platform</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>cisco_nxos_nxapi</li><li>cisco_ios</li><li>arista_eos_eapi</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Vendor and platform identifier.<br>    </td>
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
    <td style="vertical-align:middle">rollback_to</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Name of checkpoint file to rollback to. Mutually exclusive with checkpoint_file.<br>    </td>
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
      Transport protocol for API. Only needed for NX-API and eAPI. If omitted, platform-specific default will be used.<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">username</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Username used to login to the target device.<br>    </td>
    </tr>
        </table><br>


.. important:: Requires pyntc


Examples
--------

.. raw:: html

    <br/>


::

    - ntc_rollback:
        ntc_host: eos1
        checkpoint_file: backup.cfg
    
    - ntc_rollback:
        ntc_host: eos1
        rollback_to: backup.cfg


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
        <td> status </td>
        <td> Which operation took place and whether it was successful. </td>
        <td align=center> success </td>
        <td align=center> string </td>
        <td align=center> rollback executed </td>
    </tr>
            <tr>
        <td> filename </td>
        <td> The filename of the checkpoint/rollback file. </td>
        <td align=center> success </td>
        <td align=center> string </td>
        <td align=center> backup.cfg </td>
    </tr>
        
    </table>
    </br></br>

.. note:: This module is not idempotent.

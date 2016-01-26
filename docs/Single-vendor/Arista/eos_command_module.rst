.. _eos_command:


eos_command
+++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.0.0

The eos_command module provides a module for sending arbitray commands to the EOS node and returns the ouput.  Only priviledged mode (enable) commands can be sent.

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
    <td style="vertical-align:middle">commands</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Specifies the list of commands to send to the node and execute in the configured mode.  Mutliple commands can be sent to the node as a comma delimited set of values.<br>(added in 1.0.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">encoding</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">json</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>json</li><li>text</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Specifies the requested encoding of the command output.<br>(added in 1.2.0)    </td>
    </tr>
        </table><br>


.. important:: Requires Arista EOS 4.13.7M or later with command API enabled


.. important:: Requires Python Client for eAPI 0.3.0 or later


Examples
--------

.. raw:: html

    <br/>


::

    
    - name: execute show version and show hostname
      eos_command: commands='show version, show hostname'
    
    



.. note:: This module does not support idempotent operations.
.. note:: Supports eos metaparameters for using the eAPI transport
.. note:: This module does not support stateful configuration

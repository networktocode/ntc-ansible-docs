.. _eos_acl_entry:


eos_acl_entry
+++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.1.0

This module will manage standard ACL entries on EOS nodes

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
    <td style="vertical-align:middle">acltype</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The type of ACL to manage.  Currently the only supported value for acltype is 'standard'<br>(added in 1.1.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">action</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      (added in 1.1.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">log</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Enables or disables the log keyword<br>(added in 1.1.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">name</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The name of the ACL to manage.  This name must correspond to the ACL name in the running-configuration of the node<br>(added in 1.1.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">seqno</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The sequence number of the rule that this entry corresponds to.<br>(added in 1.1.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">srcaddr</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The source address corresponding to this rule<br>(added in 1.1.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">srcprefixlen</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The source address prefix mask length.  Valid valids are in the range of 1 to 32<br>(added in 1.1.0)    </td>
    </tr>
        </table><br>


.. important:: Requires Arista EOS 4.13.7M or later with command API enabled


.. important:: Requires Python Client for eAPI 0.3.2 or later


Examples
--------

.. raw:: html

    <br/>


::

    
    - eos_acl_entry: seqno=10 name=foo action=permit srcaddr=0.0.0.0
      srcprefixlen=32
    
    - eos_acl_entry: seqno=20 name=foo action=deny srcaddr=172.16.10.0
      srcprefixlen=16
    



.. note:: All configuration is idempotent unless otherwise specified
.. note:: Supports eos metaparameters for using the eAPI transport
.. note:: Supports stateful resource configuration.

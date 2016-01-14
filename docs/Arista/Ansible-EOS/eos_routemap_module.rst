.. _eos_routemap:


eos_routemap
++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.2.0

This module will manage routemap entries on EOS nodes

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
    <td style="vertical-align:middle">action</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle">permit</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>permit</li><li>deny</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The action associated with the routemap name.<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">continue</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The statement defines the next routemap clause to evaluate.<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">description</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The description for this routemap entry.<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">match</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The list of match statements that define the routemap entry. The match statements should be a comma separated list of match statements without the word match at the beginning of the string. See the example below for more information.<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">name</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The name of the routemap to manage.<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">seqno</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The sequence number of the rule that this entry corresponds to.<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">set</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The list of set statements that define the routemap entry. The set statements should be a comma separated list of set statements without the word set at the beginning of the string. See the example below for more information.<br>(added in 1.2.0)    </td>
    </tr>
        </table><br>


.. important:: Requires Arista EOS 4.13.7M or later with command API enabled


.. important:: Requires Python Client for eAPI 0.4.0 or later


Examples
--------

.. raw:: html

    <br/>


::

    
    - eos_routemap: name=rm1 action=permit seqno=10
                    description='this is a great routemap'
                    match='as 50,interface Ethernet2'
                    set='tag 100,weight 1000'
                    continue=20



.. note:: All configuration is idempotent unless otherwise specified
.. note:: Supports eos metaparameters for using the eAPI transport
.. note:: Supports stateful resource configuration.

.. _eos_facts:


eos_facts
+++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.0.0

The eos_facts module collects facts from the EOS for use in Ansible playbooks.  It can be used independently as well to discover what facts are availble from the node.  This facts module does not cache any facts.  If no configuration options are specified, then all facts are returned.

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
    <td style="vertical-align:middle">exclude</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Specifies the list of facts to exclude when the fact module runs.  The exclude list is comma delimited and, when configured, will not return the facts named in the exclude list.  All other facts will be returned.<br>(added in 1.0.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">include</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Specifies the list of facts to include when the fact module runs.  The include list is comma delimited and, when included, will only return the facts named in the include list.  All other facts will not be returned.<br>(added in 1.0.0)    </td>
    </tr>
        </table><br>


.. important:: Requires Arista EOS 4.13.7M or later with command API enabled


.. important:: Requires Python Client for eAPI 0.3.0 or later


Examples
--------

.. raw:: html

    <br/>


::

    
    - name: collect all facts from node
      eos_facts:
    
    - name: include only a filtered set of facts returned
      eos_facts: include=interfaces
    
    - name: exclude a specific set of facts
      eos_facts: exclude=vlans
    



.. note:: Supports eos metaparameters for using the eAPI transport
.. note:: The include and exclude options are mutually exclusive

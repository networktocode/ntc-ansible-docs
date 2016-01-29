.. _eos_purge:


eos_purge
+++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.0.0

The eos_purge module will scan the current nodes running-configuration and purge resources of a specified type if the resource is not explicitly configured in the playbook.  This module will allow a playbook task to dynamically determine which resources should be removed from the nodes running-configuration based on the playbook.
Note Purge is not supported for all EOS modules

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
    <td style="vertical-align:middle">resource</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The name of the resource module to purge from the configuration.  If the provided resource name does not support purge, the module will simply exit with an error message.<br>(added in 1.0.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">results</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The results argument is used to store the output from a previous module run.   Using the output from the module run allows the purge function to filter which resources should be removed.  See the Examples for more<br>(added in 1.0.0)    </td>
    </tr>
        </table><br>


.. important:: Requires Arista EOS 4.13.7M or later with command API enabled


.. important:: Requires Python Client for eAPI 0.3.0 or later


Examples
--------

.. raw:: html

    <br/>


::

    
    # configure the set of vlans for the node
    
    - name: configure vlans
      eos_vlan: vlanid={{ item }}
      with_items: ['1', '10', '11', '12', '13', '14', '15']
      register: required_vlans
    
    
    # note the value for results is the registered vlan variable.  Also of
    # importance is the to_nice_json filter which is required
    
    - name: purge vlans not on the list
      eos_purge: resource=eos_vlan results='{{ required_vlans|to_nice_json }}'
    



.. note:: All configuration is idempotent unless otherwise specified
.. note:: Supports eos metaparameters for using the eAPI transport
.. note:: Does not support stateful resource configuration.

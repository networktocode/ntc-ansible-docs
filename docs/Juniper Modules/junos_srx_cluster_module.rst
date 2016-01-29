.. _junos_srx_cluster:


junos_srx_cluster
+++++++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.2.0

Create an srx chassis cluster and reboot the device. The device must be capable of forming an srx cluster and have the correct cables installed.

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
    <td style="vertical-align:middle">cluster_enable</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>true</li><li>false</li><li>yes</li><li>no</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      yes/true - set device to cluster mode (specify cluster_id and node)<br>no/false - set device to stand alone mode (disable cluster mode)<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">cluster_id</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">None</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      set to the cluster id , required for cluster_enable=YES<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">console</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">None</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      SERIAL or TERMINAL-SERVER port setting, per use with the <b>netconify</b> utility<br>    </td>
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
    <td style="vertical-align:middle">node</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">None</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      set to the node required (0 or 1)<br>    </td>
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
    <td style="vertical-align:middle">user</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">$USER</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Login username<br>    </td>
    </tr>
        </table><br>


.. important:: Requires junos-eznc >= 1.2.2


Examples
--------

.. raw:: html

    <br/>


::

    -junos_srx_cluster:
      host={{ inventory_hostname }}
      console="--port={{ serial }}"
      user=rick
      passwd=password123
      cluster_enable=true
      logfile=cluster.log
      cluster_id={{ cluster_id }}
      node={{ node_id }}
    
    -junos_srx_cluster:
      host={{ inventory_hostname }}
      user=rick
      passwd=password123
      cluster_enable=false
      logfile=cluster.log




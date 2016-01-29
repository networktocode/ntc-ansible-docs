.. _napalm_install_config:


napalm_install_config
+++++++++++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.0.0

This library will take the configuration from a file and load it into a device running any OS supported by napalm. The old configuration will be replaced by the new one.

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
    <td style="vertical-align:middle">commit_changes</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      If set to True the configuration will be actually replaced. If the set to False, we will not apply the changes, just check the differences.<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">config_file</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Where to load the configuration from.<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">dev_os</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      OS running the device<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">diff_file</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>True</li><li>True</li><li>1</li><li>True</li><li>False</li><li>False</li><li>0</li><li>False</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      A file where to store the "diff" between the running configuration and the new configuration. If it's not set the diff between configurations is not saved.<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">get_diffs</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>True</li><li>True</li><li>1</li><li>True</li><li>False</li><li>False</li><li>0</li><li>False</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Set to false to not have any diffs generated and always apply config.  Useful if platform does not support commands being used to generated diffs.  Note- By default diffs are generated even if the diff_file param is not set.<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">hostname</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      IP or FQDN of the device you want to connect to<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">password</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Password<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">replace_config</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>True</li><li>True</li><li>1</li><li>True</li><li>False</li><li>False</li><li>0</li><li>False</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      If set to True the entire configuration on the device will be replaced during the commit. If set to False, we will merge the new config with the existing one. Default- false.<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">timeout</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">60</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Timeout for connections and requests to device<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">username</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Username<br>    </td>
    </tr>
        </table><br>


.. important:: Requires napalm


Examples
--------

.. raw:: html

    <br/>


::

    
    - assemble:
        src=../compiled/{{ inventory_hostname }}/
        dest=../compiled/{{ inventory_hostname }}/running.conf
    
    - napalm_install_config:
        hostname={{ inventory_hostname }}
        username=dbarroso
        dev_os={{os}}
        password=p4ssw0rd
        config_file=../compiled/{{ inventory_hostname }}/running.conf
        commit_changes={{ commit_changes }}
        replace_config={{ replace_config }}
        diff_file=../compiled/{{ inventory_hostname }}/diff




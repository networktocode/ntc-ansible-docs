.. _junos_get_config:


junos_get_config
++++++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.2.0

Retrieve the configuration of a device running Junos and save it to a file. **Note** unicode chars will be converted to '??' as also done in PyEZ

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
    <td style="vertical-align:middle">dest</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle">None</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Path to the local server directory where configuration will be saved.<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">filter</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">None</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Defines heircachy of configuration to retrieve.  If omitted entire configuration is retrieved.  Format is slash notation ex <em>groups/routeinst/routing-instances/ISP-1</em><br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">format</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">text</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>text</li><li>xml</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      text - configuration saved as text (curly-brace) format<br>xml - configuration saved as XML<br>    </td>
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
    <td style="vertical-align:middle">options</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle">None</td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Additional options to pass to get_config. Refer to <b>jnpr.junos.rpcmeta.get_config</b> for details.<br>    </td>
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

    - junos_get_config:
       host: "{{ inventory_hostname }}"
       logfile: get_config.log
       dest: "{{ inventory_hostname }}.xml"
       format: xml
       filter: "interfaces"
       options: {inherit: inherit, groups: groups}




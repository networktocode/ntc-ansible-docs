.. _compare_dict:


compare_dict
++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------


This module verifies that the result received from TextFSM for a particular template matches the expected output from a test scenario. It does so by comparing two lists of dictionaries going through elements of one and checking if the element 'is in' the second list.

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
    <td style="vertical-align:middle">result</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      a list of dictionaries received from ntc_show_command module<br>    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">sample</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      a parsed sample from a test scenario<br>    </td>
    </tr>
        </table><br>


.. important:: Requires none


Examples
--------

.. raw:: html

    <br/>


::

    
    # verify that parsed result is the same as expected
    - compare_dict:
        result: "{{ item.item.response }}"
        sample: "{{ item.ansible_facts.parsed_sample }}"
    




.. _get_test_info:


get_test_info
+++++++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------


Offers ability to dynamically create a list of dictionaries with info required to test all templates.  This will loop through the tests dir and build each dictionary to have command, platform, rawfile, parsedfile, and path for each.

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
    <td style="vertical-align:middle">path</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      location where tests are located<br>    </td>
    </tr>
        </table><br>


Examples
--------

.. raw:: html

    <br/>


::

    - get_test_info:
    




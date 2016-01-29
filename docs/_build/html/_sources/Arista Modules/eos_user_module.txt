.. _eos_user:


eos_user
++++++++

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Added in version 1.2.0

The eos_user module helps manage CLI users on your Arista nodes. You can create, delete and modify users along with their passwords.

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
    <td style="vertical-align:middle">encryption</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>md5</li><li>sha512</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Defines the encryption format of the password provided in the corresponding secret key. Note that cleartext passwords are allowed via manual CLI user creation but are not supported in this module due to security concerns and idempotency.<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">name</td>
    <td style="vertical-align:middle">yes</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The unique username. The username must adhere to certain format guidelines. Valid usernames begin with A-Z, a-z, or 0-9 and may also contain any of these characters: @#$%^&amp;*-_= +;&lt;&gt;,.~|<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">nopassword</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"><li>True</li><li>False</li></ul></td>
        <td style="vertical-align:middle;text-align:left">
      The nopassword key is used to create a user with no password assigned. This attribute is mutually exclusive with secret and encryption.<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">privilege</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the privilege level for the user. Permitted values are integers between 0 and 15. The EOS default privilege is 1.<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">role</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures the role assigned to the user. The EOS default for this attribute is managed with aaa authorization policy local default-role; this is typically the network-operator role.<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">secret</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      This key is used in conjunction with encryption. The value should be a hashed password that was previously generated.<br>(added in 1.2.0)    </td>
    </tr>
            <tr style="text-align:center">
    <td style="vertical-align:middle">sshkey</td>
    <td style="vertical-align:middle">no</td>
    <td style="vertical-align:middle"></td>
        <td style="vertical-align:middle;text-align:left"><ul style="margin:0;"></ul></td>
        <td style="vertical-align:middle;text-align:left">
      Configures an sshkey for the CLI user. This sshkey will end up in /home/USER/.ssh/authorized_keys.  Typically this is the public key from the client SSH node.<br>(added in 1.2.0)    </td>
    </tr>
        </table><br>


.. important:: Requires Arista EOS 4.13.7M or later with command API enabled


.. important:: Requires Python Client for eAPI 0.4.0 or later


.. important:: Requires Cleartext passwords are not accepted in playbooks


Examples
--------

.. raw:: html

    <br/>


::

    
    - name: Create simple user with no assigned password
      eos_user: name=simpletom nopassword=true
    
    - name: Create user with MD5 password
      eos_user: name=securetom encryption=md5
                secret=$1$J0auuPhz$Pkr5NnHssW.Jqlk17Ylpk0
    
    - name: Create user with SHA512 password (passwd truncated in eg)
      eos_user: name=securetom encryption=sha512
                secret=$6$somesalt$rkDq7Az4Efjo
    
    - name: Remove user
      eos_user: name=securetom state=absent
    
    - name: Create user with privilege level 10
      eos_user: name=securetom encryption=sha512
                secret=$6$somesalt$rkDq7Az4Efjo
                privilege=10
    
    - name: Create user with role network-admin
      eos_user: name=securetom encryption=sha512
                secret=$6$somesalt$rkDq7Az4Efjo
                privilege=10 role=network-admin
    
    - name: Add an SSH key with a user no password
      eos_user: name=sshkeytom nopassword=true
                sshkey='ssh-rsa somesshkey'
    
    - name: Remove SSH key with a user no password
      eos_user: name=sshkeytom nopassword=true
                sshkey=''



.. note:: All configuration is idempotent unless otherwise specified
.. note:: Supports eos metaparameters for using the eAPI transport
.. note:: Supports stateful resource configuration.

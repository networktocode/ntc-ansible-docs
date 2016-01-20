#!/usr/bin/env python

DOCUMENTATION = """
---

module: docgen
short_description: Generate .rst documents from ansible modules
description:
    - Generate .rst documents from ansible modules
options:
    module_dir:
        description:
            - Path to module library
        required: true
        default: null
        choices: []
        aliases: []
    output_dir:
        description:
            - Output directory for .rst files
        required: true
        default: null
        choices: []
        aliases: []
    make_index:
        description:
            - Whether to make the index.rst file.
        required: false
        default: null
        choices: []
        aliases: []
    modules_title:
        description:
            - The title for the collection of modules.
        required: false
        default: null
        choices: []
        aliases: []
"""

EXAMPLES = """

# make some docs
- docgen: module_dir=/my/repo/library output_dir=/my/repo/docs

"""

import os
import sys
import module_formatter

INDEX_STR ="""##########################
    Title goes here
##########################

Body text goes here.

.. toctree::
   :maxdepth: 2

   modules_by_category

"""

def main():
    module = AnsibleModule(
        argument_spec=dict(
            module_dir=dict(required=True),
            output_dir=dict(required=True),
            make_index=dict(choices=BOOLEANS,
                            default='true'),
            modules_title=dict()
        ),
        supports_check_mode=False
    )

    changed = False

    module_dir = module.params['module_dir']
    output_dir = module.params['output_dir']
    make_index = module.params['make_index']
    modules_title = module.params['modules_title']

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    if make_index:
        with open(os.path.join(output_dir, 'index.rst'), "wb+") as f:
            f.write(INDEX_STR)

    sys.argv = ['module_formatter',
                '-t', 'rst',
                '--module-dir', os.path.abspath(module_dir),
                '-o', os.path.abspath(output_dir)
                ]
    #sys.stdout = out
    #sys.stderr = out
    if modules_title:
        module_formatter.run(by_category=False, modules_title=modules_title)
    else:
        module_formatter.run(by_category=False)

    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

    changed = True

    results = {}
    results['changed'] = changed
    module.exit_json(**results)
from ansible.module_utils.basic import *
main()

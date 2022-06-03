#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: module for copy content in path
version_added: "1.0.0"

options:
    name:
        description: This is the message to send to the test module.
        required: true
        type: str
    path:
        description:
        path for create file
        required: true
        type: path
        
    content:
        description:
        content for file
        required: true
        type: str


author:
    - Igor
'''

EXAMPLES = r'''
- name: Test with a message
  my_namespace.my_collection.my_own_module:
    name: my_name
- path: path
  my_namespace.my_collection.my_own_module:
    path: '/opt/test'
- content: content
  my_namespace.my_collection.my_own_module:
    content: 'test123test'

'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.

changed:
    description: Return state

'''

from ansible.module_utils.basic import AnsibleModule
import os


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        name=dict(type='str', required=False),
        path=dict(type='path', required=True),
        content=dict(type='str', required=True)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    result = dict(
        changed=False
    )

    path = module.params['path']
    content = module.params['content']
    file_path = "~/test/my_file.txt"

    if os.path.exists(path):
        result['changed'] = False
    else:
        os.makedirs(path)
        result['changed'] = True

    os.chdir(path)
    if os.path.exists(file_path):
        result['changed'] = False
    else:
        my_file = open("my_file.txt", "w+")
        my_file.write(content)
        my_file.close()
        result['changed'] = True

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
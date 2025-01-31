#!/usr/bin/python
# (c) 2018 Rubrik, Inc
# GNU General Public License v3.0+ (see COPYING or
# https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function
__metaclass__ = type

from module_utils.rubrik_cdm import credentials, load_provider_variables, rubrik_argument_spec
from ansible.module_utils.basic import AnsibleModule

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
module: rubrik_sql_live_unmount
short_description: Delete a Microsoft SQL Live Mount from the Rubrik cluster.
description:
    - Delete a Microsoft SQL Live Mount from the Rubrik cluster.
version_added: '2.8'
author: Rubrik Build Team (@drew-russell) <build@rubrik.com>
options:
  mounted_db_name:
    description:
      - The name of the Live Mounted database to be unmounted.
    required: True
    type: str
  sql_instance:
    description:
      - The name of the MSSQL instance managing the Live Mounted database to be unmounted.
    required: True
    type: str
    default: None
  sql_host:
    description:
      - The name of the MSSQL host running the Live Mounted database to be unmounted.
    required: True
    type: str
    default: None
  force:
    description:
      - Remove all data within the Rubrik cluster related to the Live Mount, even if the SQL Server database cannot be contacted.
    required: False
    type: bool
    default: False
  timeout:
    description:
      - The number of seconds to wait to establish a connection the Rubrik cluster before returning a timeout error.
    required: False
    type: int
    default: 30

extends_documentation_fragment:
    - rubrik_cdm
requirements: [rubrik_cdm]
'''


EXAMPLES = '''
- rubrik_sql_live_mount:
    mounted_db_name: 'AdventureWorks2016'
    sql_instance: 'MSSQLSERVER'
    sql_host: 'sql.rubrikdemo.com'
    force: True
'''


RETURN = '''
version:
    description: The full response of `DELETE /mssql/db/mount/{id}?force={bool}`.
    returned: success
    type: dict
'''


try:
    import rubrik_cdm
    HAS_RUBRIK_SDK = True
except ImportError:
    HAS_RUBRIK_SDK = False


def main():
    """ Main entry point for Ansible module execution.
    """

    results = {}

    argument_spec = dict(
        mounted_db_name=dict(required=True, type='str'),
        sql_instance=dict(required=True, type='str', default=None),
        sql_host=dict(required=True, type='str', default=None),
        force=dict(required=False, type='bool', default=False),
        timeout=dict(required=False, type='int', default=30),

    )

    argument_spec.update(rubrik_argument_spec)

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=False)

    ansible = module.params

    load_provider_variables(module)

    if not HAS_RUBRIK_SDK:
        module.fail_json(msg='The Rubrik Python SDK is required for this module (pip install rubrik_cdm).')

    node_ip, username, password, api_token = credentials(module)

    try:
        rubrik = rubrik_cdm.Connect(node_ip, username, password, api_token)
    except Exception as error:
        module.fail_json(msg=str(error))

    try:
        api_request = rubrik.sql_live_unmount(
            ansible["mounted_db_name"],
            ansible["sql_instance"],
            ansible["sql_host"],
            ansible["force"],
            ansible["timeout"])
    except Exception as error:
        module.fail_json(msg=str(error))

    results["response"] = api_request

    module.exit_json(**results)


if __name__ == '__main__':
    main()

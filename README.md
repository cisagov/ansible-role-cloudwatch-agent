# ansible-role-cloudwatch-agent #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-cloudwatch-agent/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-cloudwatch-agent/actions)
[![CodeQL](https://github.com/cisagov/ansible-role-cloudwatch-agent/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-cloudwatch-agent/actions/workflows/codeql-analysis.yml)

This is an Ansible role that installs and enables the [Amazon
CloudWatch
Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)
systemd service.

Note that for an EC2 instance to successfully run the CloudWatch
Agent, it must be started with an instance role that includes the
"CloudWatchAgentServerPolicy" policy.  See
[here](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-iam-roles-for-cloudwatch-agent.html)
for more details.

See
[here](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.html)
for details on configuring the Amazon CloudWatch Agent.

Note that this Ansible role makes use of the [`json_patch` Ansible
module](https://github.com/ParticleDecay/ansible-jsonpatch), which is
proposed for inclusion into the main Ansible project.  (For more
information about what JSON Patch is, see
[here](http://jsonpatch.com/).)  A copy of the relevant piece of
Python code from that repository is included in the `library`
directory, so there is no extra action required by the user.

## Requirements ##

None.

## Role Variables ##

None.

<!--
| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| optional_variable | Describe its purpose. | `default_value` | No |
| required_variable | Describe its purpose. | n/a | Yes |
-->

## Dependencies ##

None.

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: ec2
  become: yes
  become_method: sudo
  tasks:
    - name: Install AWS CloudWatch agent
      ansible.builtin.include_role:
        name: cloudwatch-agent
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

First Last - <jeremy.frasier@trio.dhs.gov>

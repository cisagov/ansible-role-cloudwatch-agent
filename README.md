# ansible-role-cloudwatch-agent #

[![Build Status](https://travis-ci.com/cisagov/ansible-role-cloudwatch-agent.svg?branch=develop)](https://travis-ci.com/cisagov/ansible-role-cloudwatch-agent)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/cisagov/ansible-role-cloudwatch-agent.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-cloudwatch-agent/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/cisagov/ansible-role-cloudwatch-agent.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-cloudwatch-agent/context:python)

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

## Requirements ##

None.

## Role Variables ##

None.

## Dependencies ##

None.

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: ec2
  become: yes
  become_method: sudo
  roles:
    - cloudwatch-agent
```

## Contributing ##

We welcome contributions!  Please see [here](CONTRIBUTING.md) for
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

First Last - <first.last@trio.dhs.gov>

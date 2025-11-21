#!/usr/bin/env bash

# Usage:
#   upgrade-cloudwatch-agent.sh <rpm_url>
#
# Attempt to upgrade the Amazon CloudWatch Agent.  If the package
# pointed to is not an update then nothing is changed.
#
# The RPM URL must point to an RPM package (*.rpm file).

set -o nounset
set -o errexit
set -o pipefail

function usage {
  cat << HELP
Usage:
  ${0##*/} [rpm_url]

Attempt to upgrade the Amazon CloudWatch Agent.  If the package
pointed to is not an update then nothing is changed.

The RPM URL must point to an RPM package (*.rpm file).
HELP
  exit 1
}

if [ $# -ne 1 ]; then
  usage
else
  url=${1}

  # All RedHat platforms should have a dnf executable that is
  # symlinked to the latest version of dnf, e.g., dnf5.
  dnf install --assumeyes "$url"
fi

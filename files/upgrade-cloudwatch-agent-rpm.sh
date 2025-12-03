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
  ${0##*/} <rpm_url>

Attempt to upgrade the Amazon CloudWatch Agent.  If the package
pointed to is not an update then nothing is changed.

The RPM URL must point to an RPM package (*.rpm file) and must be a
secure (HTTPS) URL.
HELP
  exit 1
}

if [ $# -ne 1 ]; then
  usage
else
  url=${1}

  # Ensure that the URL is secure (HTTPS)
  if [[ "$url" != https://* ]]; then
    echo "Error: Only HTTPS URLs are allowed for security reasons"
    exit 2
  fi

  # All RedHat platforms should have a dnf executable that is
  # symlinked to the latest version of dnf, e.g., dnf5.
  if ! output=$(dnf install --assumeyes --nogpgcheck "$url" 2>&1); then
    echo "ERROR: Failed to install RPM from URL: $url" >&2
    echo "dnf output:" >&2
    echo "$output" >&2
    exit 2
  fi
fi

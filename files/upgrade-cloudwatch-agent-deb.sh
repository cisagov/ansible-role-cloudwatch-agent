#!/usr/bin/bash

# Usage:
#   upgrade-cloudwatch-agent.sh <deb_url>
#
# Attempt to upgrade the Amazon CloudWatch Agent.  If the package
# pointed to is not an update then nothing is changed.
#
# The DEB URL must point to a DEB package (*.deb file).

set -o nounset
set -o errexit
set -o pipefail

function usage {
  cat << HELP
Usage:
  ${0##*/} [deb_url]

Attempt to upgrade the Amazon CloudWatch Agent.  If the package
pointed to is not an update then nothing is changed.

The DEB URL must point to a DEB package (*.deb file).
HELP
  exit 1
}

if [ $# -ne 1 ]; then
  usage
else
  url=${1}
  pkg_file=/tmp/amazon-cloudwatch-agent.deb

  wget --output-document "$pkg_file" "$url"
  apt install --assume-yes "$pkg_file"
  rm "$pkg_file"
fi

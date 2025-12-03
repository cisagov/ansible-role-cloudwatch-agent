#!/usr/bin/env bash

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

PKG_FILE=$(mktemp).deb

function usage {
  cat << HELP
Usage:
  ${0##*/} <deb_url>

Attempt to upgrade the Amazon CloudWatch Agent.  If the package
pointed to is not an update then nothing is changed.

The DEB URL must point to a DEB package (*.deb file) and must be a
secure (HTTPS) URL.
HELP
  exit 1
}

# Delete temporary files
function cleanup {
  rm --force "$PKG_FILE"
}

trap cleanup EXIT

if [ $# -ne 1 ]; then
  usage
else
  url=${1}

  # Ensure that the URL is secure (HTTPS)
  if [[ "$url" != https://* ]]; then
    echo "Error: Only HTTPS URLs are allowed for security reasons"
    exit 2
  fi

  wget_output=$(wget --https-only --output-document "$PKG_FILE" "$url" 2>&1)
  wget_exit_code=$?
  if [ $wget_exit_code -ne 0 ]; then
    echo "ERROR: Failed to download package from $url"
    echo "wget output:"
    echo "$wget_output"
    exit $wget_exit_code
  fi
  apt install --assume-yes "$PKG_FILE"
fi

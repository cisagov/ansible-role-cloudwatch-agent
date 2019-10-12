"""Module containing the tests for the default scenario."""

import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("pkg", ["amazon-cloudwatch-agent"])
def test_packages(host, pkg):
    """Test that the expected packages were installed."""
    assert host.package(pkg).is_installed


@pytest.mark.parametrize(
    "f", ["/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json"]
)
def test_files(host, f):
    """Test that the expected files were installed."""
    assert host.file(f).exists
    assert host.file(f).is_file
    assert host.file(f).user == "root"
    assert host.file(f).group == "root"
    assert host.file(f).mode == 0o600


@pytest.mark.parametrize("service", ["amazon-cloudwatch-agent"])
def test_services(host, service):
    """Test that the expected services were enabled."""
    assert host.service(service).is_enabled

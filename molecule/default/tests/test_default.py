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


@pytest.mark.parametrize("service", ["amazon-cloudwatch-agent"])
def test_services(host, service):
    """Test that the expected services were enabled."""
    assert host.service(service).is_enabled

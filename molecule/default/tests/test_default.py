"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("pkg", ["amazon-cloudwatch-agent", "rsyslog"])
def test_packages(host, pkg):
    """Test that the expected packages were installed."""
    assert host.package(pkg).is_installed


@pytest.mark.parametrize(
    "f",
    [
        "/etc/systemd/system/amazon-cloudwatch-agent.service.d/override.conf",
        "/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json",
    ],
)
def test_files(host, f):
    """Test that the expected files were installed."""
    assert host.file(f).exists
    assert host.file(f).is_file
    assert host.file(f).user == "root"
    assert host.file(f).group == "root"


@pytest.mark.parametrize("service", ["amazon-cloudwatch-agent", "rsyslog"])
def test_services(host, service):
    """Test that the expected services were enabled."""
    assert host.service(service).is_enabled


def test_systemd_journald_config(host):
    """Test that the journald config was altered as expected."""
    f = host.file("/etc/systemd/journald.conf")
    assert f.exists
    assert f.is_file
    assert f.contains(r"^ForwardToSyslog=yes")
    assert not f.contains(r"^ForwardToSyslog=no")
    assert f.contains(r"^MaxLevelSyslog=debug")

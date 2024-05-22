"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import configparser
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
    """Test that systemd-journald is configured as expected."""
    cmd = host.run("systemd-analyze cat-config systemd/journald.conf")
    assert cmd.rc == 0
    config = configparser.ConfigParser(strict=False)
    config.read_string(cmd.stdout)
    assert config["Journal"]["ForwardToSyslog"]
    assert config["Journal"]["MaxLevelSyslog"] == "debug"

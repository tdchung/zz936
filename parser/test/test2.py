"""Automation of L_RTOS_KTCPTLS_*."""
import os
import re
import pytest
import pexpect
from pytest_letp.lib import swilog
from pytest_letp.lib import sim_lib
from tcpudp import (
    session_config,
    get_configuration,
    get_config_addr,
    clean_tcp_config,
    send_and_receive_tcp_data,
    check_network_available,
)
from cert import (
    get_default_cipher_suite,
    provision_root_CA_to_target,
    provision_client_cert_to_target,
    provision_client_key_to_target,
    configure_cipher_suite,
    get_NIST_value,
)
import tcps_lib
END_PATTERN = "--EOF--Pattern--"
DATA = "1234567890"
IPV4_TCPS_SITE = ""
# Determine the resources folder (legato apps)
MODULE_PATH = os.path.abspath(os.path.dirname(__file__))
TEST_RESOURCES_PATH = os.path.join(MODULE_PATH, "resources")
SYSTEM_CA_STORE_PATH = "/etc/ssl"
IPV4_ROOT_CA_PATH = os.path.join(SYSTEM_CA_STORE_PATH, "certs/")
IPV4_CLIENT_CERT_PATH = os.path.join(TEST_RESOURCES_PATH, "flake.legato.io.cert.pem")
IPV4_CLIENT_KEY_PATH = os.path.join(TEST_RESOURCES_PATH, "flake.legato.io.key.pem")
IPV4_SERVER_CERT_PATH = os.path.join(TEST_RESOURCES_PATH, "localCert1.pem")
IPV4_SERVER_KEY_PATH = os.path.join(TEST_RESOURCES_PATH, "localKey1.pem")
CONFIG_PATH = os.path.expandvars("$LETP_TESTS/config/host.xml")
WS46_CONFIG_PATH = os.path.expandvars("$LETP_TESTS/config/data_control.xml")
default_cipher_suite = ""
# ====================================================================================
# Local fixtures
# ====================================================================================
@pytest.fixture(autouse=True)
def prepare_target_and_clean_up_test(target, prep_target):
    """Set up target init and clean up test config."""
    global IPV4_TCPS_SITE
    global default_cipher_suite
    IPV4_TCPS_SITE = get_configuration(
        CONFIG_PATH, "host/test_server/tcp_internal_1/url"
    )
    swilog.step("TCPS server domain name %s" % IPV4_TCPS_SITE)
    default_cipher_suite = get_default_cipher_suite(target, 0)
    target.run_at_cmd("AT+CEREG=0", 10, "OK")
    target.run_at_cmd("AT+CMEE=1", 10, "OK")
    target.run_at_cmd("ATI", 10, "OK")
    target.run_at_cmd("AT&K3", 10, "OK")
    target.run_at_cmd('AT+KPATTERN="%s"' % END_PATTERN, 10, "OK")
    tcps_lib.check_and_del_certs_key(target)
    yield
    clean_up_config_test(target, prep_target)
# ====================================================================================
# Functions
# ====================================================================================
def clean_up_config_test(target, prep_target):
    """Clean up configuration after testing."""
    if default_cipher_suite is not None:
        target.run_at_cmd("AT+KSSLCRYPTO=" + default_cipher_suite, 1, ["OK"])
    try:
        clean_tcp_config(target)
    except:
        swilog.info("Cleanup test")
    tcps_lib.check_and_del_certs_key(target)
    check_module_env(target, prep_target)
def check_default_network_config(target):
    """Check and set default network config."""
    need_restart = False
    SimInfo = sim_lib.get_sim_info(target)
    apn_def = SimInfo.APN
    band = SimInfo.Band
    ws46 = get_configuration(WS46_CONFIG_PATH, "hl78xx/WS46")
    cmd_line = ["AT+KCARRIERCFG?", "AT+WS46?", "AT+KBNDCFG?", "AT+CGDCONT?"]
    rsp_exp = [
        r"\+KCARRIERCFG: 0",
        r"\+WS46: 28",
        r"\+KBNDCFG: 0,{}".format(band),
        r'\+CGDCONT: 1,"IP","{}"'.format(apn_def),
    ]
    cmd_exp = [
        "AT+KCARRIERCFG=0",
        "AT+WS46={}".format(ws46),
        "AT+KBNDCFG=0,{}".format(band),
        'AT+CGDCONT=1,"IP","{}"'.format(apn_def),
    ]
    loop = len(cmd_line)
    for i in range(loop):
        rsp = target.run_at_cmd(cmd_line[i], check=False)
        check_val = False
        if i == 2:
            band_set = re.search(r"\+KBNDCFG: 0,(?P<band>\d{20})", rsp).group("band")
            if int(band_set) != int(band):
                check_val = True
        elif not re.search(rsp_exp[i], rsp):
            check_val = True
        if check_val:
            rsp = target.run_at_cmd(cmd_exp[i], check=False)
            if re.search("OK", rsp):
                need_restart = True
            else:
                swilog.error(
                    "Modules cannot be configured by default for {}".format(cmd_exp[i])
                )
    # Reboot module for changes to take effect
    if need_restart:
        target.reboot()
def check_module_env(target, prep_target):
    """Verify information about module status and network status."""
    try:
        # Check Module state
        swilog.step("Check module status")
        cmd_line = [
            "AT",
            "ATE0",
            "AT+CGSN",
            "ATI3",
            "AT+CGMR",
            "AT+IPR?",
            'AT!UNLOCK="A710"',
        ]
        for cmd in cmd_line:
            rsp = target.run_at_cmd(cmd, check=False)
            if not re.search("OK", rsp):
                swilog.error("The module cannot run {} command".format(cmd))
        # Check Cell Network state
        swilog.step("Check the module network configuration")
        check_default_network_config(target)
        # Check network coverage
        swilog.step("Check SIM and network are available")
        check_network_available(target, prep_target)
    except (AssertionError, TypeError) as err:
        swilog.error("***** Test environment check fails !!!*****")
        swilog.error(err)
def provision_certificates_to_target(
    target, auth, nist, root_ca_path, client_cert_path, client_key_path
):
    """Provide certificates to target."""
    swilog.info("Set cipher suite: %s with auth: %d" % (nist, auth))
    if not root_ca_path:
        swilog.info("No root CA")
    else:
        provision_root_CA_to_target(target, root_ca_path)
    if not client_cert_path:
        swilog.info("No client certificate")
    else:
        provision_client_cert_to_target(target, client_cert_path)
    if not client_key_path:
        swilog.info("No client key")
    else:
        provision_client_key_to_target(target, client_key_path)
def config_session_connection(target, prep_target, sid=1):
    """Session configuration."""
    session_config(target, prep_target=prep_target)
    target.run_at_cmd("AT+KCNXPROFILE=%d" % sid, 10, "OK")
def config_cipher_suite_and_tcps_action(
    target, auth, nist_value, profile_id=0, config_cipher=1, valid=1
):
    """Verify TCPS operations by using specified cipher suite."""
    if config_cipher:
        configure_cipher_suite(target, profile_id, nist_value, auth)
    tcps_cfg_at_cmd = tcps_lib.prepare_TCP_cfg_at_cmd(
        1, 3, IPV4_TCPS_SITE, "", "", 0, 0, 0, profile_id, auth
    )
    try:
        tcps_lib.start_TCP_cfg(target, tcps_cfg_at_cmd, valid)
    except:
        if valid == 1:
            pytest.xfail(reason="ATSWI-170")
    if valid:
        send_and_receive_tcp_data(target, 1, DATA, 0)
def L_RTOS_KTCPTLS_0001(target, prep_target):
    """TCP over TLS: Server authentication.
    No certificates loaded. Should not connect to server.
    """
    auth = 1
    nist = "All cipher suites"
    nist_value = get_NIST_value(mkey_algo=8, auth_algo=3, enc_algo=25392, mac_algo=12)
    root_ca_path = ""
    client_cert_path = ""
    client_key_path = ""
    # Provide certificates to target
    provision_certificates_to_target(
        target, auth, nist, root_ca_path, client_cert_path, client_key_path
    )
    # Session configuration
    config_session_connection(target, prep_target)
    # Verify TCPS operations by using specified cipher suite
    config_cipher_suite_and_tcps_action(
        target, auth, nist_value, config_cipher=0, valid=0
    )
    # Clean up configuration after testing
    clean_up_config_test(target, prep_target)
@pytest.mark.xfail(reason="ATSWI-170")
def L_RTOS_KTCPTLS_0002(target, prep_target):
    """TCP over TLS: Server authentication.
    Server Root CA loaded. Connects to server.
    """
    auth = 1
    nist = "All cipher suites"
    nist_value = get_NIST_value(mkey_algo=8, auth_algo=3, enc_algo=25392, mac_algo=12)
    root_ca_path = IPV4_ROOT_CA_PATH
    client_cert_path = ""
    client_key_path = ""
    # Provide certificates to target
    provision_certificates_to_target(
        target, auth, nist, root_ca_path, client_cert_path, client_key_path
    )
    # Session configuration
    config_session_connection(target, prep_target)
    # Verify TCPS operations by using specified cipher suite
    config_cipher_suite_and_tcps_action(target, auth, nist_value, config_cipher=0)
    # Clean up configuration after testing
    clean_up_config_test(target, prep_target)
@pytest.mark.xfail(reason="ATSWI-170")
def L_RTOS_KTCPTLS_0003(target, prep_target):
    """TCP over TLS: Server authentication.
    Server Root CA, Client key, Client root CA loaded. Connects to
    server.
    """
    auth = 1
    nist = "All cipher suites"
    nist_value = get_NIST_value(mkey_algo=8, auth_algo=3, enc_algo=25392, mac_algo=12)
    root_ca_path = IPV4_ROOT_CA_PATH
    client_cert_path = IPV4_CLIENT_CERT_PATH
    client_key_path = IPV4_CLIENT_KEY_PATH
    # Provide certificates to target
    provision_certificates_to_target(
        target, auth, nist, root_ca_path, client_cert_path, client_key_path
    )
    # Session configuration
    config_session_connection(target, prep_target)
    # Verify TCPS operations by using specified cipher suite
    config_cipher_suite_and_tcps_action(target, auth, nist_value, config_cipher=0)
    # Clean up configuration after testing
    clean_up_config_test(target, prep_target)
def L_RTOS_KTCPTLS_0004(target, prep_target):
    """TCP over TLS: Mutual authentication.
    No certificates loaded. Should not connect to server.
    """
    auth = 3
    nist = "Cipher suites"
    nist_value = get_NIST_value(mkey_algo=8, auth_algo=2, enc_algo=8192, mac_algo=4)
    root_ca_path = ""
    client_cert_path = ""
    client_key_path = ""
    # Provide certificates to target
    provision_certificates_to_target(
        target, auth, nist, root_ca_path, client_cert_path, client_key_path
    )
    # Session configuration
    config_session_connection(target, prep_target)
    # Verify TCPS operations by using specified cipher suite
    config_cipher_suite_and_tcps_action(target, auth, nist_value, valid=0)
    # Clean up configuration after testing
    clean_up_config_test(target, prep_target)
def L_RTOS_KTCPTLS_0005(target, prep_target):
    """TCP over TLS: Mutual authentication.
    Server Root CA loaded. Should not connect to server.
    """
    auth = 3
    nist = "Cipher suites"
    nist_value = get_NIST_value(mkey_algo=8, auth_algo=2, enc_algo=8192, mac_algo=4)
    root_ca_path = IPV4_ROOT_CA_PATH
    client_cert_path = ""
    client_key_path = ""
    # Provide certificates to target
    provision_certificates_to_target(
        target, auth, nist, root_ca_path, client_cert_path, client_key_path
    )
    # Session configuration
    config_session_connection(target, prep_target)
    # Verify TCPS operations by using specified cipher suite
    config_cipher_suite_and_tcps_action(target, auth, nist_value, valid=0)
    # Clean up configuration after testing
    clean_up_config_test(target, prep_target)
def L_RTOS_KTCPTLS_0006(target, prep_target):
    """TCP over TLS: Mutual authentication.
    Server Root CA loaded. Client root CA loaded. Should not connect to
    server.
    """
    auth = 3
    nist = "Cipher suites"
    nist_value = get_NIST_value(mkey_algo=8, auth_algo=2, enc_algo=8192, mac_algo=4)
    root_ca_path = IPV4_ROOT_CA_PATH
    client_cert_path = IPV4_CLIENT_CERT_PATH
    client_key_path = ""
    # Provide certificates to target
    provision_certificates_to_target(
        target, auth, nist, root_ca_path, client_cert_path, client_key_path
    )
    # Session configuration
    config_session_connection(target, prep_target)
    # Verify TCPS operations by using specified cipher suite
    config_cipher_suite_and_tcps_action(target, auth, nist_value, valid=0)
    # Clean up configuration after testing
    clean_up_config_test(target, prep_target)
def L_RTOS_KTCPTLS_0014(target, prep_target):
    """TCP over TLS: Mutual authentication.
    Server Root CA, Client root CA, Client key loaded. Connects to
    server. Use Cipher(NIST Name): TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256
    (AT+KSSLCRYPTO=0,8,1,8192,4,4,3).
    """
    auth = 3
    nist = "TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256"
    nist_value = get_NIST_value(mkey_algo=8, auth_algo=1, enc_algo=8192, mac_algo=4)
    root_ca_path = IPV4_ROOT_CA_PATH
    client_cert_path = IPV4_CLIENT_CERT_PATH
    client_key_path = IPV4_CLIENT_KEY_PATH
    # Provide certificates to target
    provision_certificates_to_target(
        target, auth, nist, root_ca_path, client_cert_path, client_key_path
    )
    # Session configuration
    config_session_connection(target, prep_target)
    # Verify TCPS operations by using specified cipher suite
    config_cipher_suite_and_tcps_action(target, auth, nist_value)
    # Clean up configuration after testing
    clean_up_config_test(target, prep_target)
def L_RTOS_KTCPTLS_0016(target, prep_target):
    """TCP over TLS: Mutual authentication.
    Server Root CA, Client root CA, Client key loaded. Connects to
    server. Use Cipher(NIST Name): TLS-ECDHE-ECDSA-WITH-AES-128-GCM-
    SHA256 (AT+KSSLCRYPTO=0,8,2,8192,4,4,3).
    """
    auth = 3
    nist = "TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256"
    nist_value = get_NIST_value(mkey_algo=8, auth_algo=2, enc_algo=8192, mac_algo=4)
    root_ca_path = IPV4_ROOT_CA_PATH
    client_cert_path = IPV4_CLIENT_CERT_PATH
    client_key_path = IPV4_CLIENT_KEY_PATH
    # Provide certificates to target
    provision_certificates_to_target(
        target, auth, nist, root_ca_path, client_cert_path, client_key_path
    )
    # Session configuration
    config_session_connection(target, prep_target)
    # Verify TCPS operations by using specified cipher suite
    config_cipher_suite_and_tcps_action(target, auth, nist_value)
    # Clean up configuration after testing
    clean_up_config_test(target, prep_target)
def L_RTOS_KTCPTLS_0017(target, prep_target):
    """TCP over TLS: Mutual authentication.
    Server Root CA, Client root CA, Client key loaded. Connects to
    server. Use Cipher(NIST Name): TLS-ECDHE-ECDSA-WITH-AES-256-GCM-
    SHA384 (AT+KSSLCRYPTO=0,8,2,16384,8,4,3).
    """
    auth = 3
    nist = "TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384"
    nist_value = get_NIST_value(mkey_algo=8, auth_algo=2, enc_algo=16384, mac_algo=8)
    root_ca_path = IPV4_ROOT_CA_PATH
    client_cert_path = IPV4_CLIENT_CERT_PATH
    client_key_path = IPV4_CLIENT_KEY_PATH
    # Provide certificates to target
    provision_certificates_to_target(
        target, auth, nist, root_ca_path, client_cert_path, client_key_path
    )
    # Session configuration
    config_session_connection(target, prep_target)
    # Verify TCPS operations by using specified cipher suite
    config_cipher_suite_and_tcps_action(target, auth, nist_value)
    # Clean up configuration after testing
    clean_up_config_test(target, prep_target)
def L_RTOS_KTCPTLS_0018(target, prep_target):
    """TCP over TLS: Mutual authentication.
    Server Root CA, Client root CA, Client key loaded. Connects to
    server. Use Cipher(NIST Name): TLS-ECDHE-ECDSA-WITH-AES-128-CCM
    (AT+KSSLCRYPTO=0,8,2,16,0,4,3).
    """
    auth = 3
    nist = "TLS-ECDHE-ECDSA-WITH-AES-128-CCM"
    nist_value = get_NIST_value(mkey_algo=8, auth_algo=2, enc_algo=16, mac_algo=0)
    root_ca_path = IPV4_ROOT_CA_PATH
    client_cert_path = IPV4_CLIENT_CERT_PATH
    client_key_path = IPV4_CLIENT_KEY_PATH
    # Provide certificates to target
    provision_certificates_to_target(
        target, auth, nist, root_ca_path, client_cert_path, client_key_path
    )
    # Session configuration
    config_session_connection(target, prep_target)
    # Verify TCPS operations by using specified cipher suite
    config_cipher_suite_and_tcps_action(target, auth, nist_value)
    # Clean up configuration after testing
    clean_up_config_test(target, prep_target)
def L_RTOS_KTCPTLS_0019(target, prep_target):
    """TCP over TLS: Mutual authentication.
    Server Root CA, Client root CA, Client key loaded. Connects to
    server. Use Cipher(NIST Name): TLS-ECDHE-ECDSA-WITH-AES-256-CCM
    (AT+KSSLCRYPTO=0,8,2,32,0,4,3).
    """
    auth = 3
    nist = "TLS-ECDHE-ECDSA-WITH-AES-256-CCM"
    nist_value = get_NIST_value(mkey_algo=8, auth_algo=2, enc_algo=32, mac_algo=0)
    root_ca_path = IPV4_ROOT_CA_PATH
    client_cert_path = IPV4_CLIENT_CERT_PATH
    client_key_path = IPV4_CLIENT_KEY_PATH
    # Provide certificates to target
    provision_certificates_to_target(
        target, auth, nist, root_ca_path, client_cert_path, client_key_path
    )
    # Session configuration
    config_session_connection(target, prep_target)
    # Verify TCPS operations by using specified cipher suite
    config_cipher_suite_and_tcps_action(target, auth, nist_value)
    # Clean up configuration after testing
    clean_up_config_test(target, prep_target)
def L_RTOS_KTCPTLS_0020(target, prep_target):
    """TCP over TLS: Mutual authentication.
    Server Root CA, Client root CA, Client key loaded. Connects to
    server. Use Cipher(NIST Name): TLS-ECDHE-ECDSA-WITH-AES-128-CCM-8
    (AT+KSSLCRYPTO=0,8,2,256,0,4,3).
    """
    auth = 3
    nist = "TLS-ECDHE-ECDSA-WITH-AES-128-CCM-8"
    nist_value = get_NIST_value(mkey_algo=8, auth_algo=2, enc_algo=256, mac_algo=0)
    root_ca_path = IPV4_ROOT_CA_PATH
    client_cert_path = IPV4_CLIENT_CERT_PATH
    client_key_path = IPV4_CLIENT_KEY_PATH
    # Provide certificates to target
    provision_certificates_to_target(
        target, auth, nist, root_ca_path, client_cert_path, client_key_path
    )
    # Session configuration
    config_session_connection(target, prep_target)
    # Verify TCPS operations by using specified cipher suite
    config_cipher_suite_and_tcps_action(target, auth, nist_value)
    # Clean up configuration after testing
    clean_up_config_test(target, prep_target)
def L_RTOS_KTCPTLS_0021(target, prep_target):
    """TCP over TLS: Mutual authentication.
    Server Root CA, Client root CA, Client key loaded. Connects to
    server. Use Cipher(NIST Name): TLS-ECDHE-ECDSA-WITH-AES-256-CCM-8
    (AT+KSSLCRYPTO=0,8,2,512,0,4,3).
    """
    auth = 3
    nist = "TLS-ECDHE-ECDSA-WITH-AES-256-CCM-8"
    nist_value = get_NIST_value(mkey_algo=8, auth_algo=2, enc_algo=512, mac_algo=0)
    root_ca_path = IPV4_ROOT_CA_PATH
    client_cert_path = IPV4_CLIENT_CERT_PATH
    client_key_path = IPV4_CLIENT_KEY_PATH
    # Provide certificates to target
    provision_certificates_to_target(
        target, auth, nist, root_ca_path, client_cert_path, client_key_path
    )
    # Session configuration
    config_session_connection(target, prep_target)
    # Verify TCPS operations by using specified cipher suite
    config_cipher_suite_and_tcps_action(target, auth, nist_value)
    # Clean up configuration after testing
    clean_up_config_test(target, prep_target)
def L_RTOS_KTCPTLS_0022(target, prep_target):
    """TCP over TLS: Module as Server.
    Server certicate, Server key loaded.
    """
    sid = 1
    port = 443
    client_cert_path = IPV4_SERVER_CERT_PATH
    client_key_path = IPV4_SERVER_KEY_PATH
    # Provide server key and certificate to target
    provision_client_cert_to_target(target, client_cert_path)
    provision_client_key_to_target(target, client_key_path)
    session_config(target, prep_target=prep_target)
    target.run_at_cmd("AT+KCNXPROFILE=%d" % sid, 10, "OK")
    tcps_cfg_at_cmd = "AT+KTCPCFG=%d,4,,%d" % (sid, port)
    tcps_lib.start_TCP_cfg(target, tcps_cfg_at_cmd)
    # Get ip
    server_addr = get_config_addr(target)
    swilog.info(server_addr)
    cmd = "openssl s_client -tls1_2 -CAfile %s -connect %s:%d -debug" % (
        client_cert_path,
        server_addr,
        port,
    )
    swilog.info(cmd)
    child = pexpect.spawn(cmd, encoding="utf-8")
    pattern = r"\+KTCP_SRVREQ: %d,2,.*" % sid
    rsp = target.at.expect([pattern, pexpect.TIMEOUT], 20)
    assert rsp == 0, "[FAILED] Connection is unsuccessful"
    child.sendline(DATA)
    swilog.info("lentgh DATA: %d" % len(DATA))
    rsp = target.at.expect(
        [pexpect.TIMEOUT, r"\+KTCP_DATA: %d,%d" % (sid + 1, len(DATA) + 1)], 30
    )
    assert rsp == 1, "[FAILED] Do not receive DATA from target"
    target.run_at_cmd(
        "AT+KTCPRCV=%d,%d" % (sid + 1, len(DATA) + 1),
        30,
        ["CONNECT", DATA + "\n" + END_PATTERN, "OK"],
    )
    cmd = "AT+KTCPCLOSE=%d" % sid
    target.run_at_cmd(cmd, 30, ["OK", r"\+KTCP_NOTIF: 2,4"])
    child.expect("closed")
    pattern = r"\+KTCPCFG: (?P<sid>\d+),(?P<status>\d)"
    config_lst = target.run_at_cmd("AT+KTCPCFG?")
    match_lst = re.findall(pattern, config_lst)
    assert len(match_lst) == 1, "[FAILED] Session of the client child is not removed"
    for sid, status in match_lst:
        if sid == "1" and status == "0":
            swilog.info("Connection is closed")
        else:
            assert 0, "[FAILED] Connection is not closed after issuing AT+KTCPCLOSE"
    # Clean up configuration after testing
    clean_up_config_test(target, prep_target)


def _new_function(asd:str=None,
                    zxc="asdad"):
    print("asdadadas")

def _new_2():
    pass


# test multi line
def test_function_multiL_lines(test:float,
                                multi: str="asd",
                                line: int=12):
    pass

# test
def test_special_chars(test: str= "Hello, World!", 
                        interger: int = 0,
                        true = True):
    pass

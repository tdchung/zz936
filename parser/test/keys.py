import binascii

from . import ecdsa
from . import der
from . import rfc6979
from .curves import NIST192p, find_curve
from .ecdsa import RSZeroError
from .util import string_to_number, number_to_string, randrange
from .util import sigencode_string, sigdecode_string
from .util import oid_ecPublicKey, encoded_oid_ecPublicKey
from hashlib import sha1


class BadSignatureError(Exception):
    pass


class BadDigestError(Exception):
    pass


class VerifyingKey:
    def __init__(self, _error__please_use_generate=None):
        if not _error__please_use_generate:
            raise TypeError("Please use VerifyingKey.generate() to "
                            "construct me")

    @classmethod
    def from_public_point(klass, point, curve=NIST192p, hashfunc=sha1):
        self = klass(_error__please_use_generate=True)
        self.curve = curve
        self.default_hashfunc = hashfunc
        self.pubkey = ecdsa.Public_key(curve.generator, point)
        self.pubkey.order = curve.order
        return self

    @classmethod
    def from_string(klass, string, curve=NIST192p, hashfunc=sha1,
                    validate_point=True):
        order = curve.order
        assert (len(string) == curve.verifying_key_length), \
               (len(string), curve.verifying_key_length)
        xs = string[:curve.baselen]
        ys = string[curve.baselen:]
        assert len(xs) == curve.baselen, (len(xs), curve.baselen)
        assert len(ys) == curve.baselen, (len(ys), curve.baselen)
        x = string_to_number(xs)
        y = string_to_number(ys)
        if validate_point:
            assert ecdsa.point_is_valid(curve.generator, x, y)
        from . import ellipticcurve
        point = ellipticcurve.Point(curve.curve, x, y, order)
        return klass.from_public_point(point, curve, hashfunc)

    @classmethod
    def from_pem(klass, string):
        return klass.from_der(der.unpem(string))

    @classmethod
    def from_der(klass, string):
        # [[oid_ecPublicKey,oid_curve], point_str_bitstring]
        s1, empty = der.remove_sequence(string)
        if empty != b'':
            raise der.UnexpectedDER("trailing junk after DER pubkey: %s" %
                                    binascii.hexlify(empty))
        s2, point_str_bitstring = der.remove_sequence(s1)
        # s2 = oid_ecPublicKey,oid_curve
        oid_pk, rest = der.remove_object(s2)
        oid_curve, empty = der.remove_object(rest)
        if empty != b'':
            raise der.UnexpectedDER("trailing junk after DER pubkey objects: %s" %
                                    binascii.hexlify(empty))
        assert oid_pk == oid_ecPublicKey, (oid_pk, oid_ecPublicKey)
        curve = find_curve(oid_curve)
        point_str, empty = der.remove_bitstring(point_str_bitstring)
        if empty != b'':
            raise der.UnexpectedDER("trailing junk after pubkey pointstring: %s" %
                                    binascii.hexlify(empty))
        assert point_str.startswith(b'\x00\x04')
        return klass.from_string(point_str[2:], curve)

    @classmethod
    def from_public_key_recovery(klass, signature, data, curve, hashfunc=sha1, sigdecode=sigdecode_string):
        # Given a signature and corresponding message this function
        # returns a list of verifying keys for this signature and message

        digest = hashfunc(data).digest()
        return klass.from_public_key_recovery_with_digest(signature, digest, curve, hashfunc=sha1, sigdecode=sigdecode)

    @classmethod
    def from_public_key_recovery_with_digest(klass, signature, digest, curve, hashfunc=sha1, sigdecode=sigdecode_string):
        # Given a signature and corresponding digest this function
        # returns a list of verifying keys for this signature and message

        generator = curve.generator
        r, s = sigdecode(signature, generator.order())
        sig = ecdsa.Signature(r, s)

        digest_as_number = string_to_number(digest)
        pks = sig.recover_public_keys(digest_as_number, generator)

        # Transforms the ecdsa.Public_key object into a VerifyingKey
        verifying_keys = [klass.from_public_point(pk.point, curve, hashfunc) for pk in pks]
        return verifying_keys

    def to_string(self):
        # VerifyingKey.from_string(vk.to_string()) == vk as long as the
        # curves are the same: the curve itself is not included in the
        # serialized form
        order = self.pubkey.order
        x_str = number_to_string(self.pubkey.point.x(), order)
        y_str = number_to_string(self.pubkey.point.y(), order)
        return x_str + y_str

    def to_pem(self):
        return der.topem(self.to_der(), "PUBLIC KEY")

    def to_der(self):
        order = self.pubkey.order
        x_str = number_to_string(self.pubkey.point.x(), order)
        y_str = number_to_string(self.pubkey.point.y(), order)
        point_str = b'\x00\x04' + x_str + y_str
        return der.encode_sequence(der.encode_sequence(encoded_oid_ecPublicKey,
                                                       self.curve.encoded_oid),
                                   der.encode_bitstring(point_str))

    def verify(self, signature, data, hashfunc=None, sigdecode=sigdecode_string):
        hashfunc = hashfunc or self.default_hashfunc
        digest = hashfunc(data).digest()
        return self.verify_digest(signature, digest, sigdecode)

    def verify_digest(self, signature, digest, sigdecode=sigdecode_string):
        if len(digest) > self.curve.baselen:
            raise BadDigestError("this curve (%s) is too short "
                                 "for your digest (%d)" % (self.curve.name,
                                                           8 * len(digest)))
        number = string_to_number(digest)
        r, s = sigdecode(signature, self.pubkey.order)
        sig = ecdsa.Signature(r, s)
        if self.pubkey.verifies(number, sig):
            return True
        raise BadSignatureError


class SigningKey:
    def __init__(self, _error__please_use_generate=None):
        if not _error__please_use_generate:
            raise TypeError("Please use SigningKey.generate() to construct me")

    @classmethod
    def generate(klass, curve=NIST192p, entropy=None, hashfunc=sha1):
        secexp = randrange(curve.order, entropy)
        return klass.from_secret_exponent(secexp, curve, hashfunc)

    # to create a signing key from a short (arbitrary-length) seed, convert
    # that seed into an integer with something like
    # secexp=util.randrange_from_seed__X(seed, curve.order), and then pass
    # that integer into SigningKey.from_secret_exponent(secexp, curve)

    @classmethod
    def from_secret_exponent(klass, secexp, curve=NIST192p, hashfunc=sha1):
        self = klass(_error__please_use_generate=True)
        self.curve = curve
        self.default_hashfunc = hashfunc
        self.baselen = curve.baselen
        n = curve.order
        assert 1 <= secexp < n
        pubkey_point = curve.generator * secexp
        pubkey = ecdsa.Public_key(curve.generator, pubkey_point)
        pubkey.order = n
        self.verifying_key = VerifyingKey.from_public_point(pubkey_point, curve,
                                                            hashfunc)
        self.privkey = ecdsa.Private_key(pubkey, secexp)
        self.privkey.order = n
        return self

    @classmethod
    def from_string(klass, string, curve=NIST192p, hashfunc=sha1):
        assert len(string) == curve.baselen, (len(string), curve.baselen)
        secexp = string_to_number(string)
        return klass.from_secret_exponent(secexp, curve, hashfunc)

    @classmethod
    def from_pem(klass, string, hashfunc=sha1):
        # the privkey pem file has two sections: "EC PARAMETERS" and "EC
        # PRIVATE KEY". The first is redundant.
        if isinstance(string, str):
            string = string.encode()
        privkey_pem = string[string.index(b'-----BEGIN EC PRIVATE KEY-----'):]
        return klass.from_der(der.unpem(privkey_pem), hashfunc)

    @classmethod
    def from_der(klass, string, hashfunc=sha1):
        # SEQ([int(1), octetstring(privkey),cont[0], oid(secp224r1),
        #      cont[1],bitstring])
        s, empty = der.remove_sequence(string)
        if empty != b'':
            raise der.UnexpectedDER("trailing junk after DER privkey: %s" %
                                    binascii.hexlify(empty))
        one, s = der.remove_integer(s)
        if one != 1:
            raise der.UnexpectedDER("expected '1' at start of DER privkey,"
                                    " got %d" % one)
        privkey_str, s = der.remove_octet_string(s)
        tag, curve_oid_str, s = der.remove_constructed(s)
        if tag != 0:
            raise der.UnexpectedDER("expected tag 0 in DER privkey,"
                                    " got %d" % tag)
        curve_oid, empty = der.remove_object(curve_oid_str)
        if empty != b'':
            raise der.UnexpectedDER("trailing junk after DER privkey "
                                    "curve_oid: %s" % binascii.hexlify(empty))
        curve = find_curve(curve_oid)

        # we don't actually care about the following fields
        #
        # tag, pubkey_bitstring, s = der.remove_constructed(s)
        # if tag != 1:
        #     raise der.UnexpectedDER("expected tag 1 in DER privkey, got %d"
        #                             % tag)
        # pubkey_str = der.remove_bitstring(pubkey_bitstring)
        # if empty != "":
        #     raise der.UnexpectedDER("trailing junk after DER privkey "
        #                             "pubkeystr: %s" % binascii.hexlify(empty))

        # our from_string method likes fixed-length privkey strings
        if len(privkey_str) < curve.baselen:
            privkey_str = b'\x00' * (curve.baselen - len(privkey_str)) + privkey_str
        return klass.from_string(privkey_str, curve, hashfunc)

    def to_string(self):
        secexp = self.privkey.secret_multiplier
        s = number_to_string(secexp, self.privkey.order)
        return s

    def to_pem(self):
        # TODO: "BEGIN ECPARAMETERS"
        return der.topem(self.to_der(), "EC PRIVATE KEY")

    def to_der(self):
        # SEQ([int(1), octetstring(privkey),cont[0], oid(secp224r1),
        #      cont[1],bitstring])
        encoded_vk = b'\x00\x04' + self.get_verifying_key().to_string()
        return der.encode_sequence(der.encode_integer(1),
                                   der.encode_octet_string(self.to_string()),
                                   der.encode_constructed(0, self.curve.encoded_oid),
                                   der.encode_constructed(1, der.encode_bitstring(encoded_vk)),
                                   )

    def get_verifying_key(self):
        return self.verifying_key

    def sign_deterministic(self, data, hashfunc=None,
                           sigencode=sigencode_string,
                           extra_entropy=b''):
        hashfunc = hashfunc or self.default_hashfunc
        digest = hashfunc(data).digest()

        return self.sign_digest_deterministic(
            digest, hashfunc=hashfunc, sigencode=sigencode,
            extra_entropy=extra_entropy)

    def sign_digest_deterministic(self, digest, hashfunc=None,
                                  sigencode=sigencode_string,
                                  extra_entropy=b''):
        """
        Calculates 'k' from data itself, removing the need for strong
        random generator and producing deterministic (reproducible) signatures.
        See RFC 6979 for more details.
        """
        secexp = self.privkey.secret_multiplier

        def simple_r_s(r, s, order, v):
            return r, s, order, v

        retry_gen = 0
        while True:
            k = rfc6979.generate_k(
                self.curve.generator.order(), secexp, hashfunc, digest,
                retry_gen=retry_gen, extra_entropy=extra_entropy)
            try:
                r, s, order, v = self.sign_digest(digest, sigencode=simple_r_s, k=k)
                break
            except RSZeroError:
                retry_gen += 1

        return sigencode(r, s, order, v)

    def sign(self, data, entropy=None, hashfunc=None, sigencode=sigencode_string, k=None):
        """
        hashfunc= should behave like hashlib.sha1 . The output length of the
        hash (in bytes) must not be longer than the length of the curve order
        (rounded up to the nearest byte), so using SHA256 with nist256p is
        ok, but SHA256 with nist192p is not. (In the 2**-96ish unlikely event
        of a hash output larger than the curve order, the hash will
        effectively be wrapped mod n).

        Use hashfunc=hashlib.sha1 to match openssl's -ecdsa-with-SHA1 mode,
        or hashfunc=hashlib.sha256 for openssl-1.0.0's -ecdsa-with-SHA256.
        """

        hashfunc = hashfunc or self.default_hashfunc
        h = hashfunc(data).digest()
        return self.sign_digest(h, entropy, sigencode, k)

    def sign_digest(self, digest, entropy=None, sigencode=sigencode_string, k=None):
        if len(digest) > self.curve.baselen:
            raise BadDigestError("this curve (%s) is too short "
                                 "for your digest (%d)" % (self.curve.name,
                                                           8 * len(digest)))
        number = string_to_number(digest)
        r, s, v = self.sign_number(number, entropy, k)
        return sigencode(r, s, self.privkey.order, v)

    def sign_number(self, number, entropy=None, k=None):
        # returns a pair of numbers
        order = self.privkey.order
        # privkey.sign() may raise RuntimeError in the amazingly unlikely
        # (2**-192) event that r=0 or s=0, because that would leak the key.
        # We could re-try with a different 'k', but we couldn't test that
        # code, so I choose to allow the signature to fail instead.

        # If k is set, it is used directly. In other cases
        # it is generated using entropy function
        if k is not None:
            _k = k
        else:
            _k = randrange(order, entropy)

        assert 1 <= _k < order
        sig = self.privkey.sign(number, _k)
        return sig.r, sig.s, sig.recovery_param
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
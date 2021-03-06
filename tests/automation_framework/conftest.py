import pytest
import json
import os
import sys
import logging
import config.config as pconfig
TCFHOME = os.environ.get("TCF_HOME", "../../")
logger = logging.getLogger(__name__)
sys.path.append(os.getcwd())
import globals
import utility.logger as plogger

@pytest.fixture(scope="session", autouse=True)
def setup_config(args=None):
    """ Fixture to setup initial config for pytest session. """

    # parse out the configuration file first
    conffiles = ["tcs_config.toml"]
    confpaths = [".", TCFHOME + "/config"]

    try:
        config = pconfig.parse_configuration_files(conffiles, confpaths)
        config_json_str = json.dumps(config, indent=4)
    except pconfig.ConfigurationException as e:
        logger.error(str(e))
        sys.exit(-1)

    plogger.setup_loggers(config.get("Logging", {}))
    sys.stdout = plogger.stream_to_logger((logging.getLogger("STDOUT"),
                                           logging.DEBUG))
    sys.stderr = plogger.stream_to_logger((logging.getLogger("STDERR"),
                                           logging.WARN))

    logger.info("configuration for the session: %s", config)

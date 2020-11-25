import logging

import pytest

from lingpy import log
from lingpy.log import info, warning, debug, error, deprecated, missing_module, file_written


@pytest.fixture
def fresh_logger():
    yield log
    log._logger = None


def test_Logging_context_manager(capsys, tmppath, fresh_logger):
    # Note: We must make sure to acquire a fresh logger *within* the capture
    # all context, because otherwise, stderr redirection won't work. Thus,
    # we have to initialize the logger and call one of its logging methods
    # within one function which we will then pass to capture_all.
    def _log(method='debug', with_context_manager=False, level=logging.DEBUG):
        logger = log.get_logger(test=True, force_default_config=True, config_dir=tmppath)
        method = getattr(logger, method)

        if with_context_manager:
            with log.Logging(logger=logger, level=level):
                method('')
        else:
            method('')
        return capsys.readouterr().err

    assert 'DEBUG' not in _log()
    assert 'DEBUG' in _log(with_context_manager=True)
    assert 'DEBUG' not in _log(with_context_manager=True, level=logging.WARN)
    assert 'WARN' in _log(method='warning', with_context_manager=True, level=logging.WARN)


def test_new_config(fresh_logger, tmppath):
    new_cfg = log.get_logger(config_dir=tmppath, test=True)
    assert hasattr(new_cfg, 'info')


def test_default_config(fresh_logger, tmppath):
    default_cfg = log.get_logger(config_dir=tmppath, force_default_config=True)
    assert hasattr(default_cfg, 'info')


def test_convenience():
    info('m')
    warning('m')
    debug('m')
    error('m')
    deprecated('o', 'n')
    missing_module('m')
    file_written('f')

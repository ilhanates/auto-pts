from autopts.bot.iut_config.zephyr import iut_config

BotProjects = []

z = zephyr_nrf52 = {
    'name': 'zephyr'
}

# ****************************************************************************
# AutoPTS configuration
# ****************************************************************************
z['auto_pts'] = {
    'server_ip': ['10.250.15.146'],
    'local_ip' : ['10.250.15.149'],
    'cli_port': [65001],
    'srv_port': [65000],
    'project_path': '/work/zephyr',
    'workspace': 'softdevice',
    # 'database_file': 'path/to/zephyrTestCase.db',
    # 'store': True,
    'tty_file': '/dev/ttyACM14',
    'board': 'nrf52',
    'debugger_snr': '683066667',
    'enable_max_logs': True,
    'retry': 0,
    'bd_addr': '',
    'rtt_log': True,
    'recovery': False,
    'superguard': 15,  # minutes,
    'no_build': True
}

z['git'] = {
    'zephyr': {
        'path': '.',
        'remote': 'ncs',
        'branch': 'master',
        'stash_changes': False,
        'update_repo': False
    },
}


z['iut_config'] = {
    "prj.conf": {
        "test_cases": {'GAP/ADV/BV-01-C'}
    },}

BotProjects.append(zephyr_nrf52)

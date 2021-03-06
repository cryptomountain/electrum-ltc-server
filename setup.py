from setuptools import setup

setup(
    name="electrum-ltc-server",
    version="1.0",
    scripts=['run_electrum_ltc_server.py','electrum-ltc-server'],
    install_requires=['plyvel','jsonrpclib', 'irc >= 11, <=14.0'],
    package_dir={
        'electrumltcserver':'src'
        },
    py_modules=[
        'electrumltcserver.__init__',
        'electrumltcserver.utils',
        'electrumltcserver.storage',
        'electrumltcserver.deserialize',
        'electrumltcserver.networks',
        'electrumltcserver.blockchain_processor',
        'electrumltcserver.server_processor',
        'electrumltcserver.processor',
        'electrumltcserver.version',
        'electrumltcserver.ircthread',
        'electrumltcserver.stratum_tcp'
    ],
    description="Litecoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv@electrum.org",
    license="MIT Licence",
    url="https://github.com/pooler/electrum-ltc-server/",
    long_description="""Server for the Electrum Lightweight Litecoin Wallet"""
)

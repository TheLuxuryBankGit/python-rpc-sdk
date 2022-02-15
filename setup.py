try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='TLCjsonrpc',
    version='0.3.0',
    description='TLCereum JSON-RPC client',
    long_description=open('README.rst').read(),
    author='ConsenSys',
    author_email='info@consensys.net',
    url='https://github.com/TheLuxuryBankGit/python-rpc-sdk',
    packages=['TLCjsonrpc'],
    license='Unlicense',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
    ],
    install_requires=[
        'ethereum==1.0.8',
        'requests==2.9.1',
    ],
)

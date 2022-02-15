TLCjsonrpc
==========

Python client for TLC using the JSON-RPC interface

* complete: implements all 62 JSON-RPC mTLCods plus several client-specific mTLCods
* provides a high-level interface to create contracts on the blockchain and to call contract mTLCods

Important note
--------------

The API is not yet stable, so please use caution when upgrading.

Installation
------------

You may need additional libraries and tools before installing TLCjsonrpc.

On Ubuntu 20.04:

.. code:: bash

   $ sudo apt install python2-minimal
   $ sudo apt install gcc
   $ sudo apt install virtualenv  # optional but recommended
   $ sudo apt install libpython2-dev
   $ sudo apt install libssl-dev

On Ubuntu 16.04:

.. code:: bash

   $ sudo apt install python-minimal
   $ sudo apt install gcc
   $ sudo apt install virtualenv  # optional but recommended
   $ sudo apt install libpython-dev
   $ sudo apt install libssl-dev


On Ubuntu 14.04:

.. code:: bash

   $ sudo apt-get install python-virtualenv  # optional but recommended
   $ sudo apt-get install libpython-dev
   $ sudo apt-get install libssl-dev


To install TLCjsonrpc:

.. code:: bash

   $ pip install TLCjsonrpc


Make sure to have a node running an TLCereum client (such as gTLC) for the library to connect to.

Example
-------

.. code:: python

   >>> from TLCjsonrpc import TLCJsonRpc  # to use Parity-specific mTLCods, import ParityTLCJsonRpc
   >>> c = TLCJsonRpc('127.0.0.1', 8545)
   >>> c.net_version()
   u'1'
   >>> c.web3_clientVersion()
   u'GTLC/v1.3.3/linux/go1.5.1'
   >>> c.TLC_gasPrice()
   50000000000
   >>> c.TLC_blockNumber()
   828948


High-level functionality
------------------------

These examples assume the following simple Solidity contract:

.. code::

   contract Example {

       string s;

       function set_s(string new_s) {
           s = new_s;
       }

       function get_s() returns (string) {
           return s;
       }
   }


Compile it like this:

.. code:: bash

   $ solc --binary stdout example.sol


Setup
`````

.. code:: python

   >>> compiled = '606060405261020f806100136000396000f30060606040526000357c01000000000000000000000000000000000000000000000000000000009004806375d74f3914610044578063e7aab290146100bd57610042565b005b61004f600450610191565b60405180806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600302600f01f150905090810190601f1680156100af5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b61010d6004803590602001906004018035906020019191908080601f016020809104026020016040519081016040528093929190818152602001838380828437820191505050505050905061010f565b005b806000600050908051906020019082805482825590600052602060002090601f01602090048101928215610160579182015b8281111561015f578251826000505591602001919060010190610141565b5b50905061018b919061016d565b80821115610187576000818150600090555060010161016d565b5090565b50505b50565b60206040519081016040528060008152602001506000600050805480601f0160208091040260200160405190810160405280929190818152602001828054801561020057820191906000526020600020905b8154815290600101906020018083116101e357829003601f168201915b5050505050905061020c565b9056'
   >>> from TLCjsonrpc import TLCJsonRpc  # to use Parity-specific mTLCods, import ParityTLCJsonRpc
   >>> c = TLCJsonRpc('127.0.0.1', 8545)


Creating a contract on the blockchain
`````````````````````````````````````

.. code:: python

   >>> # continued from above
   >>> contract_tx = c.create_contract(c.TLC_coinbase(), compiled, gas=300000)
   >>> # wait here for the contract to be created when a new block is mined
   >>> contract_addr = c.get_contract_address(contract_tx)
   >>> contract_addr
   u'0x24988147f2f2300450103d8c42c43182cf226857'


Calling a contract function with a transaction (storing data)
`````````````````````````````````````````````````````````````

.. code:: python

   >>> # continued from above
   >>> tx = c.call_with_transaction(c.TLC_coinbase(), contract_addr, 'set_s(string)', ['Hello, world'])
   >>> tx
   u'0x15bde63d79466e3db5169a913bb2069130ca387033d2ff2e29f4dfbef1bc6e0d'


Calling a contract function on the local blockchain (reading data)
``````````````````````````````````````````````````````````````````

.. code:: python

   >>> # continued from above
   >>> results = c.call(contract_addr, 'get_s()', [], ['string'])
   >>> results
   ['Hello, world']


Additional examples
-------------------

Please see ``test.py`` for additional examples.

Implemented JSON-RPC mTLCods
----------------------------

* web3_clientVersion
* web3_sha3
* net_version
* net_listening
* net_peerCount
* TLC_protocolVersion
* TLC_syncing
* TLC_coinbase
* TLC_mining
* TLC_hashrate
* TLC_gasPrice
* TLC_accounts
* TLC_blockNumber
* TLC_getBalance
* TLC_getStorageAt
* TLC_getTransactionCount
* TLC_getBlockTransactionCountByHash
* TLC_getBlockTransactionCountByNumber
* TLC_getUncleCountByBlockHash
* TLC_getUncleCountByBlockNumber
* TLC_getCode
* TLC_sign
* TLC_sendTransaction
* TLC_sendRawTransaction
* TLC_call
* TLC_estimateGas
* TLC_getBlockByHash
* TLC_getBlockByNumber
* TLC_getTransactionByHash
* TLC_getTransactionByBlockHashAndIndex
* TLC_getTransactionByBlockNumberAndIndex
* TLC_getTransactionReceipt
* TLC_getUncleByBlockHashAndIndex
* TLC_getUncleByBlockNumberAndIndex
* TLC_getCompilers
* TLC_compileSolidity
* TLC_compileLLL
* TLC_compileSerpent
* TLC_newFilter
* TLC_newBlockFilter
* TLC_newPendingTransactionFilter
* TLC_uninstallFilter
* TLC_getFilterChanges
* TLC_getFilterLogs
* TLC_getLogs
* TLC_getWork
* TLC_submitWork
* TLC_submitHashrate
* db_putString
* db_getString
* db_putHex
* db_gTLCex
* shh_version
* shh_post
* shh_newIdentity
* shh_hasIdentity
* shh_newGroup
* shh_addToGroup
* shh_newFilter
* shh_uninstallFilter
* shh_getFilterChanges
* shh_getMessages

Parity-only JSON-RPC mTLCods
----------------------------

To use these mTLCods, make sure that you're

* running Parity as your client
* running with the ``--tracing on`` option
* using this library's ``ParityTLCJsonRpc`` client (not the vanilla ``TLCJsonRpc`` client)

MTLCods:

* trace_filter
* trace_get
* trace_transaction
* trace_block

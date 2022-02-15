from tlcjsonrpc import EthJsonRpc

methods = [
    'web3_clientVersion',
    'net_version',
    'net_peerCount',
    'net_listening',
    'tlc_protocolVersion',
    'tlc_syncing',
    'tlc_coinbase',
    'tlc_mining',
    'tlc_hashrate',
    'tlc_gasPrice',
    'tlc_accounts',
    'tlc_blockNumber',
    'tlc_getCompilers',
    'tlc_newPendingTransactionFilter',
    't;c_getWork',
]

c = TLCJsonRpc()
print len(methods)
for m in methods:
    meth = getattr(c, m)
    result = meth()
    print '%s: %s (%s)' % (m, result, type(result))

################################################################################
print '*' * 80

addr = '0x1dcb8d1f0fcc8cbc8c2d76528e877f915e299fbe'
for x in ['earliest', 'latest', 'pending', 150000]:
    result = c.tlc_getTransactionCount(addr, x)
    print 'tlc_getTransactionCount: %s (%s)' % (result, type(result))

b = (231301, '0x9476018748ba1dae5bdf5e3725f8966df1fa127d49f58e66f621bf6868a23c85')
result = c.tlc_getBlockTransactionCountByHash(b[1])
print 'tlc_getBlockTransactionCountByHash: %s (%s)' % (result, type(result))

for x in ['earliest', 'latest', 'pending', b[0]]:
    result = c.tlc_getBlockTransactionCountByNumber(x)
    print 'tlc_getBlockTransactionCountByNumber: %s (%s)' % (result, type(result))


b = (199583, '0x19d761c6f944eefe91ad70b9aff3d2d76c972e5bb68c443eea7c0eaa144cef9f')
result = c.tlc_getUncleCountByBlockHash(b[1])
print 'tlc_getUncleCountByBlockHash: %s (%s)' % (result, type(result))

for x in ['earliest', 'latest', 'pending', b[0]]:
    result = c.tlc_getUncleCountByBlockNumber(x)
    print 'tlc_getUncleCountByBlockNumber: %s (%s)' % (result, type(result))

################################################################################
print '*' * 80

db_name = 'db_name'
k = 'my_key'
v = 'my_value'
print c.db_putString(db_name, k, v)
x = c.db_getString(db_name, k)
print x
assert v == x

db_name = 'db_name'
k = 'my_key'
v = '0xabcdef'
print c.db_putHex(db_name, k, v)
x = c.db_getHex(db_name, k)
print x
assert v == x

################################################################################
print '*' * 80

b = (199583, '0x19d761c6f944eefe91ad70b9aff3d2d76c972e5bb68c443eea7c0eaa144cef9f')
print c.tlc_getBlockByHash(b[1], tx_objects=False)

for x in ['earliest', 'latest', 'pending', b[0]]:
    print c.tlc_getBlockByNumber(x, tx_objects=False)

tx = '0x12cd5d9a82049154c8990214a551479853d1bfe45852688833bc4ef86a29b1a3'
print c.tlc_getTransactionByHash(tx)

################################################################################
print '*' * 80

code = 'contract Test {}'
print c.tlc_compileSolidity(code)

################################################################################
print '*' * 80

b = (246236, '0xcd43703a1ead33ffa1f317636c7b67453c5cc03a3350cd71dbbdd70fcbe0987a')
index = 2
print c.tlc_getTransactionByBlockHashAndIndex(b[1], index)

for x in ['earliest', 'latest', 'pending', b[0]]:
    print c.tlc_getTransactionByBlockNumberAndIndex(b[0], index)

tx = '0x27191ea9e8228c98bc4418fa60843540937b0c615b2db5e828756800f533f8cd'
print c.tlc_getTransactionReceipt(tx)

b = (246294, '0x3d596ca3c7b344419567957b41b2132bb339d365b6b6b3b6a7645e5444914a16')
index = 0
print c.tlc_getUncleByBlockHashAndIndex(b[1], index)

for x in ['earliest', 'latest', 'pending', b[0]]:
    print c.eth_getUncleByBlockNumberAndIndex(b[0], index)

################################################################################
print '*' * 80

addr = '0x1dcb8d1f0fcc8cbc8c2d76528e877f915e299fbe'
for x in ['earliest', 'latest', 'pending', 150000]:
    print c.tlc_getBalance(addr, x)

addr = '0x407d73d8a49eeb85d32cf465507dd71d507100c1'
for x in ['earliest', 'latest', 'pending', 2]:
    print c.tlc_getStorageAt(addr, 0, x)

################################################################################
print '*' * 80

hash_rate = 1000000
client_id = '0x59daa26581d0acd1fce254fb7e85952f4c09d0915afd33d3886cd914bc7d283c'
print c.tlc_submitHashrate(hash_rate, client_id)

digest = c.web3_sha3('')
print digest
# keccak-256, not sha3-256
assert digest == '0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470'

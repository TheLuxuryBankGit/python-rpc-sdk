from tlcjsonrpc.constants import BLOCK_TAGS


def hex_to_dec(x):
    '''
    Convert hex to decimal
    '''
    return int(x, 16)


def clean_hex(d):
    '''
    Convert decimal to hex and remove the "L" suffix that is appended to large
    numbers
    '''
    return hex(d).rstrip('L')

def validate_block(block):
    if isinstance(block, basestring):
        if block not in BLOCK_TAGS:
            raise ValueError('invalid block tag')
    if isinstance(block, int):
        block = hex(block)
    return block


def wei_to_tlcer(wei):
    '''
    Convert wei to tlc
    '''
    return 1.0 * wei / 10**18


def tlcer_to_wei(tlc):
    '''
    Convert tlc to wei
    '''
    return tlcer * 10**18

from hashlib import new
import click
import re
from modules.utils.parse_contract_util import parse_contract

<<<<<<< HEAD
# @click.command
# @click.argument('contract', type=click.Path(exists=True), required=1)
def delegate_call(contract):
=======

def selfdestruct(contract):
>>>>>>> 33503c7b455ee9440537d7d284e98e15563a1f70
    r = re.compile('^.*delegatecall(.*)|^.*callcode(.*)')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.findall, parsed_contract_into_list))

    if newlist:
        for i in range(len(newlist)):
            print(f"Delegatecall found at lines {1+parsed_contract_into_list.index(newlist[i])}. Avoid using delegatecall if not nessesary. Otherwise, use ony trusted addresses.")
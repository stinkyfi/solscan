import click
import re
from modules.utils.parse_contract_util import parse_contract
from modules.utils.printer import *
from vulnerabilities_descriptions.reentrancy_desc import *


def reentrancy(contract):
    r = re.compile('^.*call\.value\(.*\).*')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.match, parsed_contract_into_list))
    if newlist:
        for i in range(len(newlist)):
            #print(f"Re-entrancy found at line {1+parsed_contract_into_list.index(newlist[i])}")
            #linijka ponizej musi zostac dodana (wprowadza numer lini wystpujcej podatnosci):
            line_number = 1+parsed_contract_into_list.index(newlist[i])
            printer_vuln(line_number, vulnerability_name, vulnerability_description, vulnerability_more_info_links, vulnerability_recommendation, vulnerability__description_more_info_links)



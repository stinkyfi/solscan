import click
import re
from modules.utils.parse_contract_util import parse_contract
from modules.utils.printer import *
from vulnerabilities_descriptions.insecrandoms_desc import *

def randomsource(contract):
    r = re.compile('^.*blockhash.*|^.*block\.timestamp.*|^.*block\.difficulty.*')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.search, parsed_contract_into_list))
    #if newlist:
    #    for i in range(len(newlist)):
    #        print(f"Are you sure these functions aren't used as randomness source at line {1+parsed_contract_into_list.index(newlist[i])}?")
    #make newlist printable 
    newlist_to_print = []
    #=====
    if newlist:
        for i in range(len(newlist)):
            line_number = 1+parsed_contract_into_list.index(newlist[i]) #line number
            line_number_as_str = str(line_number) #line number to string
            newlist_to_print.append(line_number_as_str) #new list without []
        newlist_printable = ', '.join(newlist_to_print) #new list without []
        #Use printer
        printer_vuln(newlist_printable, vulnerability_name, vulnerability_description, vulnerability_recommendation, more_info)
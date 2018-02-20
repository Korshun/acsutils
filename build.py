#!/usr/bin/python3

import sys
import re
from os import path, makedirs

files = [
    "acsversion.acs",
    "acsretval.acs",
    "acshudlibdef.acs",
    "acserror.acs",
    "acsmath.acs",
    "acsctype.acs",
    "acsstr.acs",
    "acszdoom.acs",
    "acspack.acs",
    "acsinput.acs",
    "acsunits.acs",
    "acsparse.acs",
    "acsaprop.acs",
    "acsplayer.acs",
    "acscursor.acs",
    "acsinfo.acs",
    "acswidescreen.acs",
	"acssort.acs",
    "acshudlib.acs",
]

TYPE_ALIASES_ACC = {
    # 'int': 'int',
    'num': 'int',
    'fixed': 'int',
    'ang': 'int',
    'raw': 'int',
    
    # 'bool': 'bool',
    
    # 'str': 'str',
}

TYPE_ALIASES_BCC = {
    # 'int': 'int',
    # 'fixed': 'fixed',
    # 'bool': 'bool',
    'ang': 'fixed',
    'num': 'raw',
    # 'raw': 'raw',
    'str': 'str',
}


def readfile(*args, **kwargs):
    with open(*args, **kwargs) as file:
        return file.read()


def error(string):
    print(string, file=sys.stderr)
    sys.exit(1)

# Global variable stuff
PRIVCONST_DECLARATION = \
    re.compile(r'@privconst\s+(\w+)\s+(\w+)(\s*=\s*([^;]+))?\s*;',
               flags=re.IGNORECASE)

CONST_DECLARATION = \
    re.compile(r'@const\s+(\w+)\s+(\w+)(\s*=\s*([^;]+))?\s*;',
               flags=re.IGNORECASE)

VAR_DECLARATION = \
    re.compile(r'@(\w+)\s+(\w+)(\s*=\s*([^;]+))?\s*;',
               flags=re.IGNORECASE)

VAR_USE = re.compile(r'\$(\w+)', flags=re.IGNORECASE)


class Var:
    pass


def find_global_vars():
    global_variables = {}
    
    for filename in files:
        file_content = readfile('src/' + filename, 'r', encoding='utf-8')
        for match in VAR_DECLARATION.finditer(file_content):
            var = Var()
            var.type = match.group(1).lower()
            var.name = match.group(2)
            var.value = match.group(4).strip()
            
            if var.name.lower() in global_variables:
                error('%s already declared' % var.name)    
            global_variables[var.name.lower()] = var
            
    return global_variables


def allocate_global_vars(global_variables):
    ints = []
    strs = []
    for var in global_variables.values():
        if var.type == 'str':
            var.index = len(strs)
            strs.append(var)
        else:
            var.index = len(ints)
            ints.append(var)
            
    return ints, strs


def write_global_vars(out, ints, strs, var_type):
    out.write('%s ACSUtils_Ints[%d] = {\n' % (var_type, len(ints)))
    for var in ints:
        if var.type != 'str':
            out.write('\t%s, // %s\n' % (var.value, var.name))
    out.write('};\n\n')
    
    out.write('str ACSUtils_Strings[%d] = {\n' % len(strs))
    for var in strs:
        if var.type == 'str':
            out.write('\t%s, // %s\n' % (var.value, var.name))
    out.write('};\n\n')


def replace_var_uses(file_content, global_variables):
    def repl(match):
        name = match.group(1)
        var = global_variables.get(name.lower())
        if not var:
            error('$%s not found' % name)
        
        if var.type == 'str':
            return 'ACSUtils_Strings[%d]' % var.index
        else:
            return 'ACSUtils_Ints[%d]' % var.index

    return VAR_USE.sub(repl, file_content)
   
   
def remove_variable_declarations(file_content):
    file_content = VAR_DECLARATION.sub('', file_content)
    return file_content


def replace_constants_acc(file_content):
    file_content = CONST_DECLARATION.sub(r'#libdefine \2 \4', file_content)
    file_content = PRIVCONST_DECLARATION.sub(r'#define \2 \4', file_content)
    return file_content


def replace_constants_bcc(file_content):
    file_content = CONST_DECLARATION.sub(r'enum : \1 { \2 = \4 };',
                                         file_content)
    file_content = PRIVCONST_DECLARATION.sub(r'private enum : \1 { \2 = \4 };',
                                             file_content)
    return file_content


# Type replacement
def remove_casts(file_content):
    return re.sub(r'\b(int|fixed|str|bool|ang)\(', '(', file_content)


def replace_casts(file_content):
    return re.sub(r'\b(int|fixed|str|bool|ang)\(', r'(\1)(', file_content)


def replace_types_acc(file_content):
    for a, b in TYPE_ALIASES_ACC.items():
        file_content = re.sub(r'\b' + a + r'\b', b, file_content)
    return file_content


def replace_types_bcc(file_content):
    for a, b in TYPE_ALIASES_BCC.items():
        file_content = re.sub(r'\b' + a + r'\b', b, file_content)
    return file_content


def main():
    global_vars = find_global_vars()
    ints, strs = allocate_global_vars(global_vars)

    # generate output file
    if not path.isdir('dist'):
        makedirs('dist')

    acsutils = open('dist/acsutils.acs', 'w', encoding='utf-8')
    bcsutils = open('dist/bcsutils.bcs', 'w', encoding='utf-8')
    
    header = readfile('src/header.acs')
    acsutils.write(header)
    bcsutils.write(header)

    bcsutils.write('strict namespace BCSUtils {\n')
    
    # write ACSUtils code
    for filename in files:
        file_content = readfile('src/' + filename, 'r', encoding='utf-8')
        file_content = replace_var_uses(file_content, global_vars)
        
        acc_input = file_content
        acc_input = remove_casts(acc_input)
        acc_input = replace_constants_acc(acc_input)
        acc_input = remove_variable_declarations(acc_input)
        acc_input = replace_types_acc(acc_input)
        acsutils.write(acc_input)
        acsutils.write('\n')
        
        bcc_input = file_content
        bcc_input = replace_casts(bcc_input)
        bcc_input = replace_constants_bcc(bcc_input)
        bcc_input = remove_variable_declarations(bcc_input)
        bcc_input = replace_types_bcc(bcc_input)
        bcsutils.write(bcc_input)
        bcsutils.write('\n')
        
        if filename == 'acshudlibdef.acs':
            write_global_vars(acsutils, ints, strs, 'int')
            write_global_vars(bcsutils, ints, strs, 'raw')
        
    bcsutils.write('} // strict namespace BCSUtils\n')
    acsutils.close()
    bcsutils.close()

if __name__ == '__main__':
    main()

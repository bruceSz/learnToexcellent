def replace(s,d):
    length = len(s)
    output = ''
    for i in range(length):
        if not s[i] in d:
            output += s[i]
        else:
            output +=d[s[i]]

    return output

if __name__ == '__main__':
    s='''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''

    d={'k':'m','o':'q','e':'g'}
    print replace(s,d)


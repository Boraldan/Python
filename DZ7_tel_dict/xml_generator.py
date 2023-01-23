
def create(data):
    f =''
    s =''
    t = ''
    d = ''
    f, s, t, d = data

    xml = '<xml>\n'
    xml += '    <first_name units = "fn">{}</first_name>\n'\
        .format(f)
    xml += '    <second_name units = "sn">{}</second_name>\n'\
        .format(s)
    xml += '    <phone units = "t">{}</phone>\n'\
        .format(t)
    xml += '    <describe units = "d">{}</describe>\n'\
        .format(d)
    xml += '</xml>'

    with open('xml_data.xml', 'w', encoding='utf-8') as file:
        file.write(xml)

    return data
    
import logger as lr

def create():
    id = int(input("Введите id студента."))
    data = lr.get_students()
    s, f, p, bd, t, cl = data[id]

    xml = '<xml>\n'
    xml += '    <second_name units = "sn">{}</second_name>\n'\
        .format(s)
    xml += '    <first_name units = "fn">{}</first_name>\n'\
        .format(f)
    xml += '    <patro_name units = "fn">{}</patro_name>\n'\
        .format(p)
    xml += '    <birthday units = "fn">{}</birthday>\n'\
        .format(bd)
    xml += '    <phone units = "t">{}</phone>\n'\
        .format(t)
    xml += '    <class units = "d">{}</class>\n'\
        .format(cl)
    xml += '</xml>'

    with open('DZ8_data_base\\xml_data.xml', 'w', encoding='utf-8') as file:
        file.write(xml)

 
    
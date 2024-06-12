'''
生成 HTML 文件中的表格
'''

def run(conditions, versions, machines):
    str_table = '''
        <table>
            <tr>
                <td rowspan="2" colspan="2"> </td>
                <td colspan="{CONDITIONS_NUM}"> 不同条件 </td>
            </tr>
            <tr>
                {CONDITIONS}
            </tr>
            {TABLE_INFOS}
        </table>
    '''

    str_one_machine_row_first = '''
            <tr>
                <td rowspan="{VERSION_NUM}"> {MACHINE} </td>
                <td> {VERSION} </td>
                {CHECKBOXES}
            </tr>
    '''

    str_one_machine_row_other = '''
            <tr>
                <td> {VERSION} </td>
                {CHECKBOXES}
            </tr>
    '''

    str_checkbox = '''
                <td> <input type="checkbox"> </td>
    '''
    str_condition = '''
                <td> {CONDITION} </td>
    '''

    def gen_one_machine(machine_name, version_names, conditions_num):
        dict_infos = {
            'VERSION_NUM': len(version_names),
            'MACHINE': machine_name,
            'VERSION': version_names[0],
            'CHECKBOXES': ''.join([str_checkbox] * conditions_num)
        }
        result = str_one_machine_row_first.format(**dict_infos) 

        for i in range(1, len(version_names)):
            dict_infos['VERSION'] = version_names[i]
            result += str_one_machine_row_other.format(**dict_infos) 

        return result

    str_table_infos = ''
    for now_machine in machines:
        str_table_infos += gen_one_machine(now_machine, versions, len(conditions))

    str_condition_info = ''
    for now_condition in conditions:
        str_condition_info += str_condition.format(CONDITION=now_condition)

    dict_info = {
        'CONDITIONS_NUM': len(conditions),
        'CONDITIONS': str_condition_info,
        'TABLE_INFOS': str_table_infos,
    }
    return str_table.format(**dict_info)

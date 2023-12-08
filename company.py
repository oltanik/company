"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов. +
2. Вывести имена всех сотрудников компании. +
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают. +
4. Вывести имена всех сотрудников компании, которые получают больше 100к. +
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями). +
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела +
Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём. +
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём. +
9. Вывести среднюю зарплату по всей компании. +
10. Вывести названия должностей, которые получают больше 90к без повторений. +
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин). +
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.+
Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.
13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

'13. Вывести список отделов со средним налогом на сотрудников этого отдела.'

def average_tax(departments, taxes):
    aver_tax_company = {}
    for department in departments:
        tax_dep = taxes[0]['value_percents']
        sum_salary = 0 # сумма всех зарплат отдела
        count_employers = len(department['employers']) # количество сотрудников в отделе
        department_name = department['title']
        for employers_info in department['employers']:
            salary = employers_info['salary_rub'] # зарплата каждого сотрудника
            sum_salary += salary # считаем сумму всех зарплат отдела
        try:
            for tax in taxes:
                if department_name in tax['department'] and tax['department'] is not None:
        except TypeError:
                    tax_dep += tax['value_percents']
        aver_tax = (sum_salary * (tax_dep/100))/ count_employers # средня сумма налога на отдел
        aver_tax_company[department_name] = aver_tax
    return aver_tax_company



print(average_tax(departments, taxes))


def last_name_vowel(departments):
    last_name_vowel_final = set()
    for department in departments:
        for employers_info in department['employers']:
            if employers_info['last_name'][-1] in 'aeiouy':
                last_name_vowel_final.add(employers_info['first_name'])
    return last_name_vowel_final

def salary_women(departments):
    salary_women_dep = []
    name_women = ("Michelle","Nicole", "Christina", "Caitlin")
    for departmen in departments:
        dep = None
        count_women = 0
        salary_women = 0
        for employers_info in departmen['employers']:
            if employers_info['first_name'] in name_women:
                count_women += 1
                salary_women += employers_info['salary_rub']
                dep = departmen['title']
        if count_women > 0:
            salary_women_dep.append((dep, int(salary_women/count_women) ))
    return salary_women_dep


def position_ninety(departments):
    list_pos_ninety = set()
    for employers in departments:
        for employers_info in employers['employers']:
            if employers_info['salary_rub'] > 90000:
                list_pos_ninety.add(employers_info['position'])
    return list_pos_ninety

def aver_salary_company(departments):
    money_sum = 0
    count_employers = 0
    for employers in departments:
        count_employers += len(employers['employers'])
        for employers_info in employers['employers']:
            money_sum += employers_info['salary_rub']
    return int(money_sum/count_employers)

def min_aver_max_salary(departments):
    dep_money = []
    for employers in departments:
        title = employers['title']
        money_min = 0
        money_all = 0
        money_max = 0
        count_employers = len(employers['employers'])
        for employers_info in employers['employers']:
            employer_salary = employers_info['salary_rub']
            if money_min == 0 or money_min > employer_salary:
                money_min = employer_salary
            if money_max == 0 or money_max < employer_salary:
                money_max = employer_salary
            money_all += employer_salary
        dep_money.append(f'{title}: минимальная зарплата в отделе: {money_min}, средняя зарплата по отделу: {int(money_all/count_employers)}, максимальная зарплата в отделе: {money_max}.')
    return dep_money    

def min_salary(departments):
    dep_money = []
    for employers in departments:
        title = employers['title']
        money = 0
        for employers_info in employers['employers']:
            if money == 0 or money > employers_info['salary_rub']:
                money = employers_info['salary_rub']
        dep_money.append(f'{title}: {money}')
    return dep_money

def money_position(departments):
    dep_money = []
    for employers in departments:
        title = employers['title']
        money = 0
        for employers_info in employers['employers']:
            money += employers_info['salary_rub']
        dep_money.append((title, money))
    return dep_money

def position(departments):
    job_title = set()
    for employers in departments:
        for employers_info in employers['employers']:
            if employers_info['salary_rub'] < 80000:
                job_title.add(employers_info['position'])
    return job_title

def dearest_employrs(departments):
    name_dearest_employrs = []
    for employers in departments:
        for employers_info in employers['employers']:
            if employers_info['salary_rub'] > 100000:
                name_dearest_employrs.append(employers_info['first_name'])
    return (name_dearest_employrs)

def names_departmens_employ(departments):
    name_dep_empl = []
    for department in departments:
        depart = department['title']
        for employers_info in department['employers']:
            name = employers_info['first_name']
            name_dep_empl.append(f'{depart} - {name}')
    return name_dep_empl
        
def names_employees(departments):
    names = [employers_info['first_name'] for department in departments for employers_info in department['employers']]
    return names
    

def names_dep(departments):
    name_departments = [department['title'] for department in departments]
    return name_departments

#if __name__=='__main__':
    #print('В нашей компании есть отделы:',', '.join(names_dep(departments)))
    #print('В нашей компании работают сотрудники с именами:', ', '.join(names_employees(departments)))
    #print('Сторудники деляться по отделам:', ', '.join(names_departmens_employ(departments)))
    #print('Имена сотрудников с зарплатой больше 100000:', ', '.join(dearest_employrs(departments)))
    #print('Должности у которых зарплата меньше 80000:', ', '.join(position(departments)))
    #print(f'Общая сумма зарплат по отделам в месяц:\n', '\n'.join(f'{res[0]!r} salary: {res[1]}' for res in money_position(departments)))
    #print('Минимальная зарплата в отдела:', ', '.join(min_salary(departments)))
    #print(*min_aver_max_salary(departments))
    #print(f'Средняя зарплата по всей компании: {aver_salary_company(departments)}')
    #print('Должности у которых зарплата больше 90000:', ', '.join(position_ninety(departments)))
    #print(f'Средняя заплата девушек по отделам компании:\n', '\n'.join(f'Отдел: {res[0]!r}, средняя зарплата: {res[1]}' for res in salary_women(departments)))
    #print(', '.join(last_name_vowel(departments)))
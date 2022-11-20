from pprint import pprint
import re
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

  for сontacts in contacts_list:
    pattern = "(\+7|8)(\W+)?(\d{3})(\W+)?(\d{3})(\W+)?(\d{2})(\W+)?(\d{2})(\W+)?((доб.).(\d{4}))?"
    сontacts[-2] = re.sub(pattern, r"+7(\3)\5-\7-\9 \12\13", str(сontacts[-2]))
    pattern = "(\S+)"
    сontacts[0] = re.findall(pattern, str(сontacts[0]))
    if len(сontacts[0]) > 1:
       сontacts[1] = сontacts[0][1]
       if len(сontacts[0]) == 3:
          сontacts[2] = сontacts[0][2]
    сontacts[0] = сontacts[0][0]
    if len(сontacts[1].split(" "))>1 :
      firstname = сontacts[1].split(" ")
      сontacts[1] = firstname[0]
      сontacts[2] = firstname[1]
  cont_list = []
  cont_list_1 = []
  contacts_list_res  = []
  for i, сontacts in enumerate(contacts_list):
    for j in range(len(contacts_list)):
      if сontacts[0] == contacts_list[j][0] and i!=j:
         cont_list_1 = []
         cont_list = zip(сontacts, contacts_list[j])
         for cont in cont_list:
           if '' in cont:
             cont = list(cont)
             cont.remove("")
           cont = list(set(cont))
           cont_list_1.append(cont[0])
         contacts_list[i] = cont_list_1
  for contacts in contacts_list:
    if contacts not in contacts_list_res:
      contacts_list_res.append(contacts)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list_res)
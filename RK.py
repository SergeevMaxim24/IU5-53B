class Language:
    def __init__(self, id, name, usability):
        self.id = id
        self.name = name
        self.usability = usability

    def values(self):
        return (self.id, self.name)

class Operator:
    def __init__(self, id, name, frequency, lan_id):
        self.id = id
        self.name = name
        self.frequency = frequency
        self.lan_id = lan_id

class Oper_Lang:
    def __init__(self, lan_id, oper_id):
        self.lan_id = lan_id
        self.oper_id = oper_id

#Языки программирования
languages = [Language(1, 'JavaScript', 18.4),
              Language(2, 'Java', 15.4),
              Language(3, 'C#', 13.7),
              Language(4, 'Python', 13.2),
              Language(5, 'PHP', 10.8),
              Language(6, 'C++', 5.8)]

#Операторы
operators = [Operator(1, '=', 10.5, 5),
              Operator(2, '*=', 5.4, 2),
              Operator(3, '/=', 5.1, 4),
              Operator(4, '+=', 8.9, 5),
              Operator(5, '++', 7.7, 6),
              Operator(6, '--', 3.6, 3)]

#Операторы в языках программирования (много-ко-многим)
oper_in_lang = [Oper_Lang(2, 3),
                Oper_Lang(1, 3),
                Oper_Lang(4, 1),
                Oper_Lang(5, 1),
                Oper_Lang(6, 1),
                Oper_Lang(2, 6),
                Oper_Lang(6, 2),
                Oper_Lang(2, 4),
                Oper_Lang(1, 5),
                Oper_Lang(3, 5)]

def main():
    one_to_many = [(lan.id, lan.name, lan.usability, op.name , op.frequency)
        for lan in languages
        for op in operators
        if op.lan_id == lan.id]

    #Задание А1
    print('Задание В1')
    a1 = list(filter(lambda x : (str)(x[3]).startswith('+'), one_to_many))
    a1 = [(el[3], el[1]) for el in a1]
    print(a1)

    #Задание В2
    print('Задание В2')
    a2 = []
    for lan in languages:
        lan_oper = list(filter(lambda x: x.lan_id == lan.id, operators))
        if len(lan_oper) > 0:
            min_frequency = min([op.frequency for op in lan_oper])
            a2.append((*lan.values(), min_frequency))
    
    a2 = sorted(a2, key= lambda x: x[2])
    print(a2)

    #Задание В3
    print('Задание B3')
    a3 = {}
    for op in operators:
        operlan = list(filter(lambda x: x.oper_id == op.id, oper_in_lang))
        a3[op.name] = [
            l.name for l in languages 
            for bl in operlan
            if bl.lan_id == l.id]
    a3 = {i[0]: i[1] for i in sorted(a3.items(), key=lambda x: x[0])}
    print(a3)

if __name__ == "__main__":
    main()
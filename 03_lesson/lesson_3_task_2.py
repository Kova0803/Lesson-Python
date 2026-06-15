from smartphone import Smartphone
catalog = {
    Smartphone('iPhone', '12', '+7-989-999-99-99'),
    Smartphone('Samsung', 'T55', '+7-555-555-99-99'),
    Smartphone('Nokia', 'C20', '+7-888-888-88-88'),
    Smartphone('Alcatel', 'A60', '+7-222-222-22-22'),
    Smartphone('Motorolla', 'E90', '+7-144-444-45-45')

}
for smartphone in catalog:
    print (f'{smartphone.brand} {smartphone.model} {smartphone.number}')

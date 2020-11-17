from faker import Faker
import names
import random

faker = Faker()
MIN_RENT = 500
MAX_RENT = 7000000

NUM_PARTNERS = 2

ID_START = 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mode = 2
    times = int(input("How many lines?\n"))

    for i in range(ID_START, times + 1):
        f_name = names.get_first_name()
        l_name = names.get_last_name()

        street = faker.street_address()
        city = faker.city()
        state = faker.state()
        zip_code = faker.postcode()
        unit = faker.building_number()

        work = random.randint(1111111111, 9999999999)
        mobile = random.randint(1111111111, 9999999999)
        home = random.randint(1111111111, 9999999999)

        max_rent = random.randint(MIN_RENT, MAX_RENT)

        pref_switch = random.randint(1, 3)
        if pref_switch == 1:
            preference = 'commercial'
        elif pref_switch == 2:
            preference = 'industrial'
        else:
            preference = 'residential'

        primary_email = faker.company_email()
        secondary_email = faker.ascii_free_email()

        company = faker.company()

        partner_id = random.randint(1, NUM_PARTNERS)

        if mode == 1:
            print("INSERT INTO clnt values(" + str(i) + ',\'' + f_name + '\',\'' + l_name + '\',\'' + street + '\',\'' + city + '\',\'' + state + '\',\'' + zip_code + '\',\'' + unit
                  + '\',' + str(work) + ',' + str(mobile) + ',' + str(home) + ',' + str(max_rent) + ',\'' + preference + '\');')
            print("INSERT INTO clnt_email values(" + str(i) + ',\'' + primary_email + '\');')
            if random.randint(0, 1):
                print("INSERT INTO clnt_email values(" + str(i) + ',\'' + secondary_email + '\');')

        elif mode == 2:
            print("INSERT INTO ownr values(" + str(
                i) + ',\'' + f_name + '\',\'' + l_name + '\',\'' + street + '\',\'' + city + '\',\'' + state + '\',\'' + zip_code + '\',\'' + unit
                  + '\',' + str(work) + ',' + str(mobile) + ',' + str(home) + ',' + str(partner_id) + ',\'' + company + '\');')
            print("INSERT INTO ownr_email values(" + str(i) + ',\'' + primary_email + '\');')
            if random.randint(0, 1):
                print("INSERT INTO ownr_email values(" + str(i) + ',\'' + secondary_email + '\');')

from faker import Faker
import names
import random

faker = Faker()
MIN_RENT = 500
MAX_RENT = 7000000

NUM_PARTNERS = 2
NUM_ASSOCIATES = 4
NUM_OWNERS = 6
NUM_CLIENTS = 12
NUM_PROPERTIES = 18

ID_START = 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mode = 4
    times = int(input("How many lines?\n"))
    count = 1

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

        primary_email = faker.company_email()
        secondary_email = faker.ascii_free_email()

        company = faker.company()

        partner_id = random.randint(1, NUM_PARTNERS)

        # clients
        if mode == 1:
            pref_switch = random.randint(1, 3)
            if pref_switch == 1:
                preference = 'commercial'
            elif pref_switch == 2:
                preference = 'industrial'
            else:
                preference = 'residential'

            print("INSERT INTO clnt values(" + str(i) + ',\'' + f_name + '\',\'' + l_name + '\',\'' + street + '\',\'' + city + '\',\'' + state + '\',\'' + zip_code + '\',\'' + unit
                  + '\',' + str(work) + ',' + str(mobile) + ',' + str(home) + ',' + str(max_rent) + ',\'' + preference + '\');')
            print("INSERT INTO clnt_email values(" + str(i) + ',\'' + primary_email + '\');')
            if random.randint(0, 1):
                print("INSERT INTO clnt_email values(" + str(i) + ',\'' + secondary_email + '\');')
        # owners
        elif mode == 2:
            print("INSERT INTO ownr values(" + str(
                i) + ',\'' + f_name + '\',\'' + l_name + '\',\'' + street + '\',\'' + city + '\',\'' + state + '\',\'' + zip_code + '\',\'' + unit
                  + '\',' + str(work) + ',' + str(mobile) + ',' + str(home) + ',' + str(partner_id) + ',\'' + company + '\');')
            print("INSERT INTO ownr_email values(" + str(i) + ',\'' + primary_email + '\');')
            if random.randint(0, 1):
                print("INSERT INTO ownr_email values(" + str(i) + ',\'' + secondary_email + '\');')

        # properties
        elif mode == 3:
            for j in range(3):
                street = faker.street_address()
                city = faker.city()
                state = faker.state()
                zip_code = faker.postcode()
                unit = faker.building_number()

                manager_id = random.randint(1, NUM_ASSOCIATES)
                ownr_id = random.randint(1, NUM_OWNERS)
                rent = random.randint(0, 6000)
                fee = float(random.randint(0, 99)) / 100.0
                bedrooms = random.randint(1, 10)
                bathrooms = random.randint(1, 10)

                if count <= times:
                    preference = 'residential'
                    sq_ft = random.randint(200, 5000)
                    print("INSERT INTO property values(" + str(
                        count) + ',\'' + street + '\',\'' + city + '\',\'' + state + '\',\'' + zip_code + '\',\'' + unit + '\',\'' +
                        preference + '\',' + str(sq_ft) +',' + str(rent) + ',' + str(fee) + ',' + str(0) + ',' + str(ownr_id) + ',' + str(manager_id) + ',' +
                          str(bedrooms) + ',' + str(bathrooms) + ');')
                elif times < count <= times*2:
                    preference = 'commercial'
                    sq_ft = random.randint(1000, 2000000)
                    print("INSERT INTO property values(" + str(
                        count) + ',\'' + street + '\',\'' + city + '\',\'' + state + '\',\'' + zip_code + '\',\'' + unit + '\',\'' +
                          preference + '\',' + str(sq_ft) + ',' + str(rent) + ',' + str(fee) + ',' + str(0) + ',' + str(
                        ownr_id) + ',' + str(manager_id) + ',' + 'NULL' + ',' + 'NULL' + ');')
                else:
                    preference = 'industrial'
                    sq_ft = random.randint(1000, 2000000)
                    print("INSERT INTO property values(" + str(
                        count) + ',\'' + street + '\',\'' + city + '\',\'' + state + '\',\'' + zip_code + '\',\'' + unit + '\',\'' +
                          preference + '\',' + str(sq_ft) + ',' + str(rent) + ',' + str(fee) + ',' + str(0) + ',' + str(
                        ownr_id) + ',' + str(manager_id) + ',' + 'NULL' + ',' + 'NULL' + ');')

                count += 1
                # print(count)

        # viewings
        elif mode == 4:
            associate_id = random.randint(1, NUM_ASSOCIATES)
            clnt_id = random.randint(1, NUM_CLIENTS)
            property_id = random.randint(1, NUM_PROPERTIES)

            date = faker.date()
            time = faker.time_object()
            str_time = time.strftime('%H:%M:%S')

            print("INSERT INTO viewing values(" + str(associate_id) + ',' + str(clnt_id) + ',' + str(property_id) + ',\'' + date + '\',\'' + str_time + '\');')


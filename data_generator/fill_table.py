import csv
import string
import random
from randomtimestamp import randomtimestamp, random_date, random_time


## general functions
def random_national_code_generator():
    length = 10
    letters = string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def random_name_generator():
    length = random.randint(1, 15)
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def random_text_generator():
    length = random.randint(10, 100)
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def random_phone_generator():
    length = 9
    letters = string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    result_str = '09' + result_str
    return result_str


## HOST
filename = 'host.csv'
header = ['national_code', 'national_card_picture', 'verified', 'personal_information']
host = []
count = 10000
for i in range(count):
    nc = random_national_code_generator()
    if nc in [i[0] for i in host]:
        continue
    temp = [nc, list(random.randbytes(100)), random.choice([True, False]),
            (random_name_generator(), random_name_generator(), random_name_generator())]
    host.append(temp)
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(host)
print("1 ended")

## GUEST
filename = 'guest.csv'
header = ['national_code', 'phone', 'personal_information']
guest = []
count = 10000
for i in range(count):
    nc = random_national_code_generator()
    if nc in [i[0] for i in guest]:
        continue
    temp = [nc, random_phone_generator(), (random_name_generator(), random_name_generator(), random_name_generator())]
    guest.append(temp)
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(guest)
print("2 ended")

## RESIDENCE
filename = 'residence.csv'
header = ['residence_id', 'host_id', 'arrival_time', 'departure_time', 'repair_fee_per_rent',
          'base_price', 'max_capacity', 'number_of_rooms', 'area', 'residence_type', 'accepted', 'ownership_document',
          'TITLE']
residence = []
count = 5000
id = 1
for i in range(count):
    temp = [id, random.choice([i[0] for i in host]), random_time(), random_time(),
            round(random.uniform(0.00, 1000.00), 2)
        , round(random.uniform(0.00, 1000.00), 2), random.randint(1, 10), random.randint(0, 4),
            round(random.uniform(0.00, 1000.00), 2)
        , random.choice(['APARTMENT', 'VILLA', 'HOTEL', 'ECOTOURISM']), random.choice([True, False]),
            (random_name_generator(), random.randint(0, 1 << 80)), random_name_generator()]
    id += 1
    residence.append(temp)
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(residence)
print("3 ended")

## NON_RENTABLE_PERIOD
filename = 'non_rentalbe_period.csv'
header = ['BEGIN', 'END', 'residence_id']
non_rentable_period = []
count = 5000
for i in range(count):
    temp = [random_date(), random_date(), random.choice([i[0] for i in residence])]
    non_rentable_period.append(temp)
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(non_rentable_period)
print("4 ended")

## DISCOUNTED_PERIOD
filename = 'discounted_period.csv'
header = ['BEGIN', 'END', 'residence_id', 'discount_percent']
discounted_period = []
count = 5000
for i in range(count):
    p = round(random.uniform(0.01, 10.00), 2)
    if p == 1.00:
        continue
    temp = [random_date(), random_date(), random.choice([i[0] for i in residence]), p]
    discounted_period.append(temp)
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(discounted_period)
print("5 ended")

## MESSAGE
filename = 'message.csv'
header = ['host_id', 'guest_id', 'ID', 'TEXT', 'TIME', 'direction']
message = []
count = 50000
id = 1
for i in range(count):
    temp = [random.choice([i[0] for i in host]), random.choice([i[0] for i in guest]), id, random_name_generator(),
            randomtimestamp(), random.choice(['TO GUEST', 'TO HOST'])]
    id += 1
    message.append(temp)
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(message)
print("6 ended")

## PICTURES
filename = 'pictures.csv'
header = ['image_id', 'image', 'residence_id']
pictures = []
for i in range(len(residence)):
    c = random.randint(0, 5)
    for j in range(c):
        temp = [j + 1, (random_name_generator(), random.randint(0, 1 << 80)), residence[i][0]]
        pictures.append(temp)
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(pictures)
print("7 ended")

## BEDS
filename = 'beds.csv'
header = ['residence_id', 'capacity', 'number_of_beds']
beds = []
count = 5000
pk_check = []
for i in range(count):
    rid = random.choice([i[0] for i in residence])
    cap = random.randint(1, 4)
    if (rid, cap) in pk_check:
        continue
    pk_check.append((rid, cap))
    temp = [rid, cap, random.randint(1, 5)]
    beds.append(temp)
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(beds)
print("8 ended")

## AMENITIES
filename = 'amenities.csv'
header = ['amenity', 'residence_id', 'COMMENT']
amenities = []
count = 50000
pk_check = []
for i in range(count):
    rid = random.choice([i[0] for i in residence])
    am = random.choice(['KITCHENWARE', 'INTERNET', 'WASHING MACHINE', 'PARKING'])
    if (rid, am) in pk_check:
        continue
    pk_check.append((rid, am))
    temp = [am, rid, random_name_generator()]
    amenities.append(temp)
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(amenities)
print("9 ended")

## CANCELLATION_POLICIES
filename = 'cancellation_policies.csv'
header = ['TYPE', 'penalty', 'COMMENT', 'residence_id']
cancellation_policies = []
count = 5000
pk_check = []
for i in range(count):
    rid = random.choice([i[0] for i in residence])
    type = random_name_generator()
    if (type, rid) in pk_check:
        continue
    pk_check.append((type, rid))
    temp = [type, round(random.uniform(0.00, 1000.00), 2), random_name_generator(), rid]
    cancellation_policies.append(temp)
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(cancellation_policies)
print("10 ended")

## ADDRESS
filename = 'address.csv'
header = ['residence_id', 'LOCATION', 'TYPE', 'province', 'city', 'full_addres']
address = []
count = 5000
cities = ['Tehran',
          'Kashan',
          'Mashhad',
          'Esfahan',
          'Karaj',
          'Shiraz',
          'Tabriz',
          'Ahvaz',
          'Qom',
          'Kermanshah',
          'Kerman',
          'Orumiyeh',
          'Rasht',
          'Bahar',
          'Zahedan',
          'Hamadan',
          'Yazd',
          'Ardabil',
          'Bandar Abbas',
          'Arak',
          'Eslamshahr',
          'Zanjan',
          'Sanandaj',
          'Qazvin',
          'Khoramabad',
          'Madan',
          'Gorgan',
          'Shahriar',
          'Shahre Qods',
          'Malard',
          'Sarta',
          'Dezful',
          'Babol',
          'Qaem Shahr',
          'Khomeyni Shahr',
          'Sabzevar',
          'Amol',
          'Pakdasht',
          'Najafabad',
          'Borujerd'
          ]
provinces = ['Tehran',
             'Esfahan',
             'Khorasan-e Razavi',
             'Esfahan',
             'Alborz',
             'Fars',
             'azarbayjan-e Sharqi',
             'Khuzestan',
             'Qom',
             'Kermanshah',
             'Kerman',
             'azarbayjan-e Gharbi',
             'Gilan',
             'Hamadan',
             'Sistan va Baluchestan',
             'Hamadan',
             'Yazd',
             'Ardabil',
             'Hormozgan',
             'Markazi',
             'Tehran',
             'Zanjan',
             'Kordestan',
             'Qazvin',
             'Lorestan',
             'Khuzestan',
             'Golestan',
             'Tehran',
             'Tehran',
             'Tehran',
             'Mazandaran',
             'Khuzestan',
             'Mazandaran',
             'Mazandaran',
             'Esfahan',
             'Khorasan-e Razavi',
             'Mazandaran',
             'Tehran',
             'Esfahan',
             'Lorestan']
for i in range(count):
    rid = residence[i][0]
    ind = random.randint(0, 39)
    temp = [rid, (random.uniform(0.00, 100.00), random.uniform(0.00, 100.00)), random.choice(['CITY', 'SUBURB']),
            provinces[ind], cities[ind],
            (random.randint(1, 200), random.randint(0, 200), random_name_generator(), random_name_generator())]
    address.append(temp)
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(address)
print("11 ended")

## Rent REQUEST
filename = 'rent_request.csv'
header = ['START_DATE', 'END_DATE', 'PEOPLE_COUNT', 'REQUEST_STATUS', 'GUEST_ID', 'RID']
rent_request = []
rent = []
count = 10000
statuses = ['Pending', 'Cancelled', 'Rejected', 'Accepted']
for _ in range(count):
    guest_id = random.choice([i[0] for i in guest])
    residence_id = random.choice([i[0] for i in residence])
    begin_date = random_date()
    end_date = random_date()

    while end_date < begin_date:
        end_date = random_date()

    people_count = random.randint(1, 5)
    status = random.choice(statuses)

    temp = [begin_date, end_date, people_count, status, guest_id, residence_id]
    repeat = False
    for rr in rent_request:
        if rr[4] == guest_id and rr[5] == residence_id and rr[0] == begin_date and rr[1] == end_date:
            repeat = True
            break
    if not repeat:
        if status == 'Accepted':
            price = round(random.uniform(0.00, 1000.00), 2)
            rent_status = random.choice(['Completed', 'Ongoing'])
            cancelation_penalty = round(random.uniform(0.00, 1000.00), 2)
            while cancelation_penalty > price:
                cancelation_penalty = round(random.uniform(0.00, 1000.00), 2)
            rent.append([price, rent_status, cancelation_penalty, begin_date, end_date, guest_id, residence_id])
        if status == 'Cancelled':
            price = round(random.uniform(0.00, 1000.00), 2)
            rent_status = 'Cancelled'
            cancelation_penalty = round(random.uniform(0.00, 1000.00), 2)
            while cancelation_penalty > price:
                cancelation_penalty = round(random.uniform(0.00, 1000.00), 2)
            rent.append([price, rent_status, cancelation_penalty, begin_date, end_date, guest_id, residence_id])
        rent_request.append(temp)

with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(rent_request)
print("12 ended")

## RENT
filename = 'rent.csv'
header = ['PRICE', 'RENT_STATUS', 'CANCELATION_PENALTY', 'START_DATE', 'END_DATE', 'GUEST_ID', 'RID']

count = 5000
pk_check = []
for i in rent:
    tp = (i[3], i[4], i[5], i[6])
    if tp in pk_check:
        print("ERRORRRRRRR")
    pk_check.append(tp)

for i in range(count):
    price = round(random.uniform(0.00, 1000.00), 2)
    rent_status = random.choice(['Completed', 'Ongoing'])
    cancelation_penalty = round(random.uniform(0.00, 1000.00), 2)
    while cancelation_penalty > price:
        cancelation_penalty = round(random.uniform(0.00, 1000.00), 2)
    random_valid_fk = random.choice(rent_request)

    fk_stat = random_valid_fk[3]
    if fk_stat == 'Cancelled':
        rent_status = 'Cancelled'
    if fk_stat == 'Pending':
        continue
    if fk_stat == 'Rejected':
        continue

    guest_id = random_valid_fk[4]
    residence_id = random_valid_fk[5]
    begin_date = random_valid_fk[0]
    end_date = random_valid_fk[1]

    fk = (begin_date, end_date, guest_id, residence_id)

    if fk in pk_check:
        continue
    pk_check.append(fk)
    temp = [price, rent_status, cancelation_penalty, begin_date, end_date, guest_id, residence_id]
    rent.append(temp)

with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(rent)
print("13 ended")

# COMPLAINT
filename = 'complaint.csv'
header = ['COMPLAINT_ID', 'ACCEPTED', 'EXPLANATION', 'START_DATE', 'END_DATE', 'GUEST_ID', 'RID']
complaint = []
count = 10000
complaint_id = 1

for i in range(count):
    accepted = random.choice([True, False])
    explanation = random_text_generator()

    random_valid_fk = random.choice(rent)

    guest_id = random_valid_fk[5]
    residence_id = random_valid_fk[6]
    begin_date = random_valid_fk[3]
    end_date = random_valid_fk[4]

    temp = [complaint_id, accepted, explanation, begin_date, end_date, guest_id, residence_id]

    complaint.append(temp)
    complaint_id += 1

with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(complaint)
print("14 ended")

# DAMAGE_REPORT
filename = 'damage_report.csv'
header = ['REPORT_ID', 'ACCEPTED', 'EXPLANATION', 'PENALTY', 'START_DATE', 'END_DATE', 'GUEST_ID', 'RID']
damage_report = []
count = 5000
damage_report_id = 1
pk_check = []

for i in range(count):
    accepted = random.choice([True, False])
    explanation = random_text_generator()
    penalty = round(random.uniform(0.00, 1000.00), 2)

    random_valid_fk = random.choice(rent)

    guest_id = random_valid_fk[5]
    residence_id = random_valid_fk[6]
    begin_date = random_valid_fk[3]
    end_date = random_valid_fk[4]

    fk = (begin_date, end_date, guest_id, residence_id)
    if fk in pk_check:
        continue
    pk_check.append(fk)

    temp = [damage_report_id, accepted, explanation, penalty, begin_date, end_date, guest_id, residence_id]

    damage_report.append(temp)
    damage_report_id += 1

with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(damage_report)
print("15 ended")

# GUEST_COMMENT_ON_HOST
filename = 'guest_comment_on_host.csv'
header = ['SCORE', 'EXPLANATION', 'START_DATE', 'END_DATE', 'GUEST_ID', 'RID', 'SCORED_DATE']
guest_comment_on_host = []
ref_rents = [l for l in set([(i[3], i[4], i[5], i[6]) for i in rent])]
count = 10000

for i in range(count):
    score = random.randint(0, 5)
    explanation = random_text_generator()
    if len(ref_rents) == 0:
        break
    ref_rent = random.choice(ref_rents)
    start_date = ref_rent[0]
    end_date = ref_rent[1]
    rid = ref_rent[3]
    guest_id = ref_rent[2]

    tmp_date = random_date()
    while tmp_date < end_date:
        tmp_date = random_date()

    temp = [score, explanation, start_date, end_date, guest_id, rid, tmp_date]
    repeat = False
    guest_comment_on_host.append(temp)
    ref_rents.remove(ref_rent)

with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(guest_comment_on_host)
print("16 ended")

## HOST_COMMENT_ON_GUEST
filename = 'host_comment_on_guest.csv'
header = ['EXPLANATION', 'START_DATE', 'END_DATE', 'GUEST_ID', 'RID']
host_comment_on_guest = []
ref_rents = [l for l in set([(i[3], i[4], i[5], i[6]) for i in rent])]
count = 10000

for i in range(count):
    explanation = random_text_generator()
    if len(ref_rents) == 0:
        break
    ref_rent = random.choice(ref_rents)
    start_date = ref_rent[0]
    end_date = ref_rent[1]
    rid = ref_rent[3]
    guest_id = ref_rent[2]
    temp = [explanation, start_date, end_date, guest_id, rid]
    host_comment_on_guest.append(temp)
    ref_rents.remove(ref_rent)

with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(host_comment_on_guest)
print("17 ended")

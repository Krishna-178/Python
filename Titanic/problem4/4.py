def process_passengers(file_path):
    def is_child(age):
        return age < 10

    def is_male(gender):
        return gender == 'male'

    def is_female(gender):
        return gender == 'female'

    survivors = {'children': [], 'male': [], 'female': []}
    non_survivors = {'children': [], 'male': [], 'female': []}

    with open(file_path, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            parts = line.split(',')
            name = parts[4]
            age = int(float(parts[6])) if parts[6] else 40
            gender = parts[5]
            survived = parts[1] == '1'

            if survived:
                if is_child(age):
                    survivors['children'].append((name, age, gender))
                elif is_male(gender):
                    survivors['male'].append((name, age))
                elif is_female(gender):
                    survivors['female'].append((name, age))
            else:
                if is_child(age):
                    non_survivors['children'].append((name, age, gender))
                elif is_male(gender):
                    non_survivors['male'].append((name, age))
                elif is_female(gender):
                    non_survivors['female'].append((name, age))

    return survivors, non_survivors

def count_total(passenger_groups):
    return sum(len(group) for group in passenger_groups.values())

survivors, non_survivors = process_passengers('titanic.csv')

#print("Survivors:")
print("Total survivors are", count_total(survivors),"and they are classified as follows")
for group, passengers in survivors.items():
    print(f"{group.capitalize()}: {len(passengers)}")

#print("\nNon-survivors:")
print("\nTotal non-survivors are", count_total(non_survivors),"and they are classified as follows")
for group, passengers in non_survivors.items():
    print(f"{group.capitalize()}: {len(passengers)}")

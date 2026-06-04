## to run this in terminAL TYPE ( python test.py Yuvaraj 24 cbe )


import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "name"
)

parser.add_argument(
    "age",
    type=int
)

parser.add_argument(
    "city",
)

args = parser.parse_args()


print(args)
print(
    f"Name : {args.name}"
)

print(
    f"Age : {args.age}"
)

print(
    f"city : {args.city}"
)

if args.age >= 18:

    print(
        "Eligible to Vote"
    )

else:

    print(
        "Not Eligible to Vote"
    )
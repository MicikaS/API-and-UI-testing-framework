from pydantic import BaseModel
from faker import Faker

faker = Faker()


class Geo(BaseModel):
    lat: str
    lng: str


class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo


class Company(BaseModel):
    name: str
    catchPhrase: str
    bs: str


class User(BaseModel):
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company

    @classmethod
    def get_invalid_user(cls):
        return cls(cls="invalid", name="invalid_user")


class UserOut(User):
    @classmethod
    def get_valid_user(cls):
        name = faker.name()
        username = faker.user_name()
        email = faker.email()
        geo = Geo(lat=faker.latitude(), lng=faker.longitude())
        address = Address(
            street=faker.street_name(),
            suite=faker.secondary_address(),
            city=faker.city(),
            zipcode=faker.zipcode(),
            geo=geo,
        )
        phone = faker.phone_number()
        website = faker.hostname()
        company = Company(
            name=faker.name(), catchPhrase=faker.catch_phrase(), bs=faker.bs()
        )

        return cls(
            name=name,
            username=username,
            email=email,
            address=address,
            phone=phone,
            website=website,
            company=company,
        )


class UserIn(User):
    @classmethod
    def get_valid_user(cls):
        user_id = faker.random_int()
        name = faker.name()
        username = faker.user_name()
        email = faker.email()
        geo = Geo(lat=faker.latitude(), lng=faker.longitude())
        address = Address(
            street=faker.street_name(),
            suite=faker.secondary_address(),
            city=faker.city(),
            zipcode=faker.zipcode(),
            geo=geo,
        )
        phone = faker.phone_number()
        website = faker.hostname()
        company = Company(
            name=faker.name(), catchPhrase=faker.catch_phrase(), bs=faker.bs()
        )

        return cls(
            id=user_id,
            name=name,
            username=username,
            email=email,
            address=address,
            phone=phone,
            website=website,
            company=company,
        )

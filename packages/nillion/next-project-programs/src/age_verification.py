from nada_dsl import *
import random

def nada_main():

    party1 = Party(name="Party1")

    secret_age1 = SecretInteger(Input(name="secret_age1", party=party1)) # Individual
    secret_age2 = SecretInteger(Input(name="secret_age2", party=party1)) # Trusted 3rd-party, e.g. Governemnt Agent

    random_int1 = Integer(random.randint(1, 1000000000000000000))
    random_int2 = Integer(random.randint(1, 1000000000000000000))

    secret_result = (secret_age1 - Integer(17)) * random_int1 + (secret_age2 - Integer(18)) * random_int2

    return [Output(secret_result, "secret_result", party1)]
from nada_dsl import *
import random

def nada_main():

    party1 = Party(name="Party1")

    secret_int1 = SecretInteger(Input(name="secret_int1", party=party1))

    secret_int2 = SecretInteger(Input(name="secret_int2", party=party1))

    secret_result = secret_int1 + secret_int2 - Integer(random.randint(1, 1000))

    return [Output(secret_result, "secret_result", party1)]
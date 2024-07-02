# Age Verification with Nillion

## How this app works

- An individual wants to prove she/he is of legal age (defined as 18+ years) without revealing the age. The age is provided as a secret using Nillion.
- A trusted party (e.g. government body) also provides the secret age using Nillion.
- A Nillion computation is done, whereby it results in a random positive integer if the individual is of legal age, and a negative random integer if not.
- If at least one of them provides an age lower than 18, the whole verification will give a negative response (see code below for details). Thus, the verification fails if there is any disagreement on whether the individual is of legal age, implying that at least one party is lying.
- Finally, the frontend app takes the random input and displays the result based on whether it was positive (= of legal age) or negative (less than 18y old).

## How to install & run

- Install the Nillion client using Nillion's [quickstart guide](https://docs.nillion.com/js-quickstart)
- Enter the scaffold-nillion-age-verification folder and run `yarn install`
- Open another terminal to run the Nillion devnet using `yarn nillion-devnet`
- Optional: run `yarn chain` to run a local hardhat blockchain and connect with MetaMask
- Spin up the app using `yarn start`

## Limitations

- The app currently only works with one Nillion Party.
- The app makes use of python's random library

## Resources

- [Nillion quickstart docs](https://docs.nillion.com/js-quickstart)
- [Nillion user key snap UI](https://nillion-snap-site.vercel.app/)
- [nada tool for creating & managing nada projects](https://docs.nillion.com/nada)
- [Nada data types](https://docs.nillion.com/nada-lang-types)

## Contact

- azommerfelds@gmail.com

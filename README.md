# Aevo Airdrop Farm

## The Idea

Up until this point in early January 2024, I had some experience writing a airdrop farm for zksync. However, for that project, there was a lot more complexity as eligibility requirements can vary significantly. However, after research into the Aevo Protocol, I realized it was inevitebly going to have an airdrop and volume would be a significant factor.

## My Code

I created a Wallet class that has the ability to open and close trades with its own unique properties for the given wallet. This is then loaded with each of the wallet data that I use, and a continuous loop opening and closing trades and random intervals is run within the main.py file. I was also aware that location could sometimes be a signal to protocols of a sybil, so I used proxy servers when interacting with the API to avoid this detection.

## The outcome

I ran the program across 3 wallets with proxy in 3 different IP addresses. Each wallet was funded with roughly $120 and using this bot there was roughly $2000+ volume built per wallet per day. In total during TGE, I sold my position immedietely and generated $2100 at a 500% return using this automated strategy with only $360 total capital invested.

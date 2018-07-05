Idea for project: Telegram bot which will send out alerts regarding trading opportunities on cryptocurrency exchanges. I have some skin in trading cryptocurrencies, and would like to build something to help me identify opportunities. 

Breakdown of solution:
1) Periodically request data from Bitfinex/Bitmex, such as open long/short positions, open-high-low-close data, trading volume. The program will have to run in the cloud as I do not want to keep my own PC running 24/7. Will look into free solutions such as AWS Lambda.
2) Run the data through ML models to identify potential opportunities to open short-term highly leveraged positions (I have some hypotheses that I would like to test).
3) Make use of Telegram API to build a bot for me to easily receive alerts when opportunities, as defined according to conditions that I will determine, arise.

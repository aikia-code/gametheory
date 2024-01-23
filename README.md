# Game theory collection

The scenario set is there is a pile of coins to be collected. Each player has to make a choice against his opponent to receive coins. There is a total of 6 coins to be had in a given session or nothing. Players can only **COOPERATE** or **DEFECT**. Choices can only result in PUNISHMENT, REWARD, TEMPTATION, and **SUCKER**'S PAYOFF.Rules are as follows:

* if both players **COOPERATE** each get a **REWARD** amounting to 3 coins
* if one player **DEFECT** and the other **COOPERATE** player one gets 6 coins as **TEMPTATION** and the other gets nothing for being a **SUCKER**
* if both **DEFECT** then each player gets a coin as **PUNISHMENT**

|CHOICE A|CHOICE B|SCORE A|SCORE B|
|--|--|--|--|
|**COOPERATE**|**COOPERATE**|3|3|
|**DEFECT**|**COOPERATE**|5|0|
|**COOPERATE**|**DEFECT**|0|5|
|**DEFECT**|**DEFECT**|1|1|

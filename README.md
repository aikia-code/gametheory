# "Game theory" simulations 🕹️

Interactively simulate and engage with game theory

Game theory is a key tool for analyzing strategic interactions and decision-making across diverse areas. It enhances our comprehension of human behavior in real-world situations, encompassing both cooperation and competition.

> *"if you are going to interact once you are better off defect otherwise you should consider cooperating"* *--- Unknown*

Inspired by [Robert Axelrod's 1984 The Evolution of Cooperation](https://www.researchgate.net/publication/316766066_Robert_Axelrod's_1984_The_Evolution_of_Cooperation) and [Veritasium's take on the topic](https://youtu.be/mScpHTIi-kM?si=15H8lTjRfC2YoQHG)

<!-- USAGE EXAMPLES -->

## Usage

### Dilemma

1. clone the repo: `git clone https://github.com/ProsperoKay/gametheory.git`
2. run `dilemma` with `python -m dilemma`
3. interact with simulation

<!-- Strategies -->

## Strategies

**Statuses** - Added[✔️]   |   To Be Added[❌]

|No.|Strategy|Description|Status|
|--|--|--|--|
|1| AlwaysCooperate|Strategy always cooperates with opponent in every matchup|✔️|
|2| AlwaysDefect|Strategy always defects in every matchup|✔️|
|3| RandomDefect|Strategy defects at random|✔️|
|4| TitForTat|Strategy always cooperates but defects only after opponent defects once then goes back to cooperate after opponent cooperates|✔️|
|5| TitFor2Tat|Strategy always cooperates but defects once after opponent defects twice in a row then goes back to cooperate after opponent cooperates|✔️|
|6| Historian|Strategy defects if opponent historically defects more than cooperates|✔️|
|7| Unforgiving|Strategy defects the rest of the game if opponent defects even once|✔️|
|8| PrimeDefector|Strategy defects at every prime numbered stage|❌|




<!-- DEFINITIONS -->

[email]: prosperokay@gmail.com
[profile]: https://github.com/ProsperoKay

<!-- CONTRIBUTING -->
## Contributing

So you've got an improvement, just send in a pull request!

### 1. Fork this repository

### 2. Create your feature branch

```bash
git checkout -b new_feature
```

### 3. Commit your changes

> When you are ready to generate a pull request, either for preliminary review, or for consideration of merging into the project you must first push your local topic branch back up to GitHub:

```bash
git push origin new_feature
```

### 4. Create new Pull Request

> Once you've committed and pushed all of your changes to GitHub, go to the page for your fork on GitHub, select your development branch, and click the pull request button. If you need to make any adjustments to your pull request, just push the updates to your branch. Your pull request will automatically track the changes on your development branch and update.

**If you've got feature ideas ✨, or wish to report a bug 🐛 simply open a new issues!**

**Remember to ⭐ star this repository to receive updates.**

<!-- LICENSE -->
## License

MIT

---
GitHub [@prosperokay][profile] • Email[@prosperokay][email]

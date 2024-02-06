# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

### 0.4.1 (2024-02-06)


### Features

* :sparkles: add `get_action_pattern ([1cf553b](https://github.com/ProsperoKay/gametheory/commit/1cf553b65cd3c89729a88dcb85ec4769abe6be90))
* :sparkles: add tit for tat strategy ([#7](https://github.com/ProsperoKay/gametheory/issues/7)) ([0ba3487](https://github.com/ProsperoKay/gametheory/commit/0ba3487aac5e50efa7d06de42a47b635e8808616))
* :zap: use `summarize_simulation_table` in main ([84a4090](https://github.com/ProsperoKay/gametheory/commit/84a4090666bc974903856e9de4e941c445607909))
* add payoff type and action type ([84d270f](https://github.com/ProsperoKay/gametheory/commit/84d270f02c50719e66c3b0c634149aa216ceae83))
* add tit for tat strategy ([ca38b36](https://github.com/ProsperoKay/gametheory/commit/ca38b361d120a0eb144f4c6411e8e00e090f5b74))
* **main:** :lipstick: add simple console ui for users to interact with ([917b2cc](https://github.com/ProsperoKay/gametheory/commit/917b2cc13202fe4ec547cdbb597bd80f767626e9))
* **main:** :triangular_flag_on_post: add full simulation + summarize simulation information display ([8150e2e](https://github.com/ProsperoKay/gametheory/commit/8150e2eabeee8b6a664835288f27c15848754abf))
* **models:** :sparkles: add `opponent_action_history` and `no_mercy` triger to strategy ([fcf8849](https://github.com/ProsperoKay/gametheory/commit/fcf884952743e7cb5384256302bcbcc3b25a4970))
* **simulation:** :alembic: debug print simulation ([e739cab](https://github.com/ProsperoKay/gametheory/commit/e739cabdf15ab4577f06b3a846d5d8e331dbca8f))
* **simulation:** :sparkles: add `historian` and `tit for two tat` to simulation match up ([fe835fb](https://github.com/ProsperoKay/gametheory/commit/fe835fbb10cb8f46a7b2973cb280d8fcde8190a4))
* **simulation:** :sparkles: add method to tabulate and print summary after simulation ([951368b](https://github.com/ProsperoKay/gametheory/commit/951368bf2182a6993ef5fd6a0db44033de62869b))
* **simulation:** :sparkles: add run simulation process ([4cfcdc2](https://github.com/ProsperoKay/gametheory/commit/4cfcdc208684c5713aec812b8f1a0feaf6f1677a))
* **simulation:** :sparkles: add setup simulation process ([51fc392](https://github.com/ProsperoKay/gametheory/commit/51fc39269eb21f77d203ec0063a18933b7d0d6ba))
* **simulation:** :sparkles: debug print simulations + summarize population data ([2511f41](https://github.com/ProsperoKay/gametheory/commit/2511f41c485cd56ea2ae581784c5038b6c294bd8))
* **simulation:** :sparkles: update `simulate` to update population attribute of strategies ([7ea7615](https://github.com/ProsperoKay/gametheory/commit/7ea7615511e68f1e2049031087e75e2017bf9b87))
* **strategy:** :sparkles: add `population` attribute to store population data ([9711594](https://github.com/ProsperoKay/gametheory/commit/97115948d3c19db9bd6c388dee2f0315e7d7a649))
* **strategy:** :sparkles: add `titfor2tat`, `historian`, and `unforgiving` strategies ([df2bb17](https://github.com/ProsperoKay/gametheory/commit/df2bb1779779304db38af039a54c6bb490caf336))
* **strategy:** :sparkles: add get strategy name ([d179643](https://github.com/ProsperoKay/gametheory/commit/d1796438414e612806b0f04a3a859ef74beac4ac))
* **utils:** :sparkles: add tabulate summary ([76e21ea](https://github.com/ProsperoKay/gametheory/commit/76e21ea85083c61baf4b249d190634d22c9eefb3))


### Bug Fixes

* :green_heart: lint warning ([e13efa8](https://github.com/ProsperoKay/gametheory/commit/e13efa81b25b04bbd8044982556a91bceba4ccdb))
* include `create` just incase + to pass linting ([9e71771](https://github.com/ProsperoKay/gametheory/commit/9e717713e30609861f601412a572abcc2754439d))
* **main:** :rotating_light: fix lint error ([f8d2cfb](https://github.com/ProsperoKay/gametheory/commit/f8d2cfbc754c1fe4633c3e448cbb9011fec1bd40))
* **models:** attribute bug. move attributes to the instance level ([9e65c8d](https://github.com/ProsperoKay/gametheory/commit/9e65c8d8765551a2ee15bbe738ab6d9445a9c26a))
* **simulation:** :ambulance: fix attribute bug. instantiate strategies ([fcad4b3](https://github.com/ProsperoKay/gametheory/commit/fcad4b33b7e51695e1120ac71b11de1a633a8841))
* **strategy:** :bug: fix attribute bug. keep on name attribute at the class level ([476717d](https://github.com/ProsperoKay/gametheory/commit/476717dcfc37b839632d0064c49d02344abc0426))
* **strategy:** :goal_net: raise value error if strategy is not provided ([24b3c5d](https://github.com/ProsperoKay/gametheory/commit/24b3c5d6a4301332ce7380a3f50e2cb96ed667dc))
* **utils:** :ambulance: attribute bug: use strategy instances ([c5ebe3c](https://github.com/ProsperoKay/gametheory/commit/c5ebe3c7700220fc5cb258a30cca6879164fdc15))

## 0.4.0 (2024-02-04)


### Features

* :sparkles: add `get_action_pattern ([1cf553b](https://github.com/ProsperoKay/gametheory/commit/1cf553b65cd3c89729a88dcb85ec4769abe6be90))
* :sparkles: add tit for tat strategy ([#7](https://github.com/ProsperoKay/gametheory/issues/7)) ([0ba3487](https://github.com/ProsperoKay/gametheory/commit/0ba3487aac5e50efa7d06de42a47b635e8808616))
* add payoff type and action type ([84d270f](https://github.com/ProsperoKay/gametheory/commit/84d270f02c50719e66c3b0c634149aa216ceae83))
* add tit for tat strategy ([ca38b36](https://github.com/ProsperoKay/gametheory/commit/ca38b361d120a0eb144f4c6411e8e00e090f5b74))
* **main:** :lipstick: add simple console ui for users to interact with ([917b2cc](https://github.com/ProsperoKay/gametheory/commit/917b2cc13202fe4ec547cdbb597bd80f767626e9))
* **main:** :triangular_flag_on_post: add full simulation + summarize simulation information display ([8150e2e](https://github.com/ProsperoKay/gametheory/commit/8150e2eabeee8b6a664835288f27c15848754abf))
* **simulation:** :alembic: debug print simulation ([e739cab](https://github.com/ProsperoKay/gametheory/commit/e739cabdf15ab4577f06b3a846d5d8e331dbca8f))
* **simulation:** :sparkles: add method to tabulate and print summary after simulation ([951368b](https://github.com/ProsperoKay/gametheory/commit/951368bf2182a6993ef5fd6a0db44033de62869b))
* **simulation:** :sparkles: add run simulation process ([4cfcdc2](https://github.com/ProsperoKay/gametheory/commit/4cfcdc208684c5713aec812b8f1a0feaf6f1677a))
* **simulation:** :sparkles: add setup simulation process ([51fc392](https://github.com/ProsperoKay/gametheory/commit/51fc39269eb21f77d203ec0063a18933b7d0d6ba))
* **strategy:** :sparkles: add get strategy name ([d179643](https://github.com/ProsperoKay/gametheory/commit/d1796438414e612806b0f04a3a859ef74beac4ac))
* **utils:** :sparkles: add tabulate summary ([76e21ea](https://github.com/ProsperoKay/gametheory/commit/76e21ea85083c61baf4b249d190634d22c9eefb3))


### Bug Fixes

* :green_heart: lint warning ([e13efa8](https://github.com/ProsperoKay/gametheory/commit/e13efa81b25b04bbd8044982556a91bceba4ccdb))
* include `create` just incase + to pass linting ([9e71771](https://github.com/ProsperoKay/gametheory/commit/9e717713e30609861f601412a572abcc2754439d))
* **main:** :rotating_light: fix lint error ([f8d2cfb](https://github.com/ProsperoKay/gametheory/commit/f8d2cfbc754c1fe4633c3e448cbb9011fec1bd40))
* **strategy:** :goal_net: raise value error if strategy is not provided ([24b3c5d](https://github.com/ProsperoKay/gametheory/commit/24b3c5d6a4301332ce7380a3f50e2cb96ed667dc))

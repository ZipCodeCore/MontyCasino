# Casino Simulation

* **Objective** - To create an casino simulation
* **Purpose** - To gain familiarity with general object orientation and design principles

* **Description**
    * The starter project lives in [python/](python/); see [python/README.md](python/README.md) to become oriented with its design.
    * Create a casino simulation by extending or removing the pre-built implementations.
    * It is advised that you create additional methods and classes to mediate any foreseen shortcomings of the prebuilt assets. 
    * Enforce the following features in your system:
        * Ensure a console-based interface is available to allow input from and output to the users
        * Ensure the `Casino` has a selection of at least 6 implementation of `Game`.
        * Ensure `Player` is garbage collected upon completing a respective `Game`
            * `SlotsPlayer` should be garbage collected when `SlotsGame` is garbage collected.
            * `BlackJackPlayer` should be garbage collected when `BlackJackGame` is garbage collected.
        * Ensure all implementation of `Player` have reference to a `CasinoAccount`
            * `CasinoAccount` should not be garbage collected when a `Game` is garbage collected.
        * Ensure at least 6 different implementations of `Game` and a respective `Player` are defined.
        * Ensure at least 1 implementation of `Game` does not involve gambling.
        * Ensure at least 3 implementations of `Game` involve gambling.
           * Enable the player to wager a `balance` that can be persisted throughout different games; when a `Game` is garbage collected, the owner of the `balance` should be able to play a new game with their new `balance`.
        * Ensure all games which should support more than 1 player, have the ability to do so.
        * Ensure there are at least 80% line coverage from testing the application.
* Begin by implementing the `SlotsGame`, `SlotsPlayer` as well as `NumberGuessGame` and `NumberGuessPlayer` provided in the `montycasino.games` package. 

<img src="./casino.gif">

## How to Download

#### Part 1 - Forking the Project
* To _fork_ the project, click the `Fork` button located at the top right of the project.


#### Part 2 - Navigating to _forked_ Repository
* Navigate to your github profile to find the _newly forked repository_.
* Copy the URL of the project to the clipboard.

#### Part 3 - Cloning _forked_ repository
* Clone the repository from **your account** into the `~/dev` directory.
  * if you do not have a `~/dev` directory, make one by executing the following command:
    * `mkdir ~/dev`
  * navigate to the `~/dev` directory by executing the following command:
    * `cd ~/dev`
  * clone the project by executing the following command:
    * `git clone https://github.com/MYUSERNAME/NAMEOFPROJECT`
 
#### Part 4 - Check Build
* From the `python/` directory, create a virtual environment and install the project:
    * `python3 -m venv .venv && source .venv/bin/activate`
    * `pip install -e '.[dev]'`
* Ensure that the tests run.
    * You should see some tests pass and the tests for unimplemented features reported as `xfailed`.
* Execute the command below to run the tests, with line coverage, from the command line.
    * `pytest --cov=montycasino`

## How to Submit

#### Part 1 -  _Pushing_ local changes to remote repository
* from a _terminal_ navigate to the root directory of the _cloned_ project.
* from the root directory of the project, execute the following commands:
    * add all changes
      * `git add .`
    * commit changes to be pushed
      * `git commit -m 'I have added changes'`
    * push changes to your repository
      * `git push -u origin master`

#### Part 2 - Submitting assignment
* from the browser, navigate to the _forked_ project from **your** github account.
* click the `Pull Requests` tab.
* select `New Pull Request`

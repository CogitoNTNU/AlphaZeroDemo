# AlphaZero
AlphaZero is a computer program developed by artificial intelligence research company DeepMind. The program is generalized to work on all two-player complete information games such as tic tac toe, four in a row, chess and go. It is only given the rules of the game, and learns to master the game solely by playing against itself.

## About us
We are a project group within the student organization Cogito at NTNU (Norwegian University of Science and Technology). The group of eight has worked on this through the fall of 2019.

## Motivation
This project was created to achieve a greater understanding of the workings of one of the hottest reinforcement learning algorithms, as well as to have fun in the process. Optimization and introduction of parallel training was motivated by the desire of being able to train a network in reasonable time. This is espacially important for games with large action- and state spaces, as convergence will take a long time. The visualization was fueled by the quest to see how the network is thinking.

## Installation
Clone the repository
```
git clone https://github.com/CogitoNTNU/AlphaZero.git
```
Navigate into the project folder
```
cd AlphaZero
```
Install the dependencies
```
pip3 install -r requirements.txt
```
If everything went well, you can now play against AZ!
```
python3 Play.py
```

## Acknowledgments
* The [AlphaZero-](https://deepmind.com/documents/260/alphazero_preprint.pdf "AlphaZero paper by D. Silver et al.") and [AphaGo Zero paper](https://deepmind.com/documents/119/agz_unformatted_nature.pdf "AlphaGo Zero paper by D. Silver et al.") are essential to read to achieve a thorough understanding of the algorithm. 
* For a brief walkthrough of the algorithm and a more "hands on approach", I recommend reading through [this article](https://medium.com/oracledevs/lessons-from-implementing-alphazero-7e36e9054191 "Lessons From Implementing AlphaZero") on Medium about an implementation of the AlpaZero algorithm.
* To get a gentle introduction to the algorithm, [this video](https://www.youtube.com/watch?v=2ciR6rA85tg "AlphaZero: DeepMind's New Chess AI ") by Two Minute Papers might be a nice place to start.
* David Silver also [explains AlphaZero](https://www.youtube.com/watch?v=Wujy7OzvdJk=0s "Deepmind AlphaZero - Mastering Games Without Human Knowledge") himself.


## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

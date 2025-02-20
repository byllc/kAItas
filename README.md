# kAItas
Katas are exercises or practice routines used to improve skills through repetition and refinement. You may recognize the term from martial arts, where it refers to a sequence of movements practiced to perfect technique. 

kAItas is a project aimed at providing some basic practice in python, but along the way we are going build a rudimentary understanding of how Large Language Models work. 

This project uses a Docker container with the enviroment requirements prestaged. 

## Getting Started

### Prerequisites

- Docker installed on your machine

### Running the Project

First build the project:
```sh
docker build -t kaitas .
```

Then run with: 

```sh
docker run -v .:/home/kaitas -it kaitas
``` 

Navigate to the directory for a specfic kata. We suggest doing them in order the first time since it build ups an understanding of LLM's from scratch. 

```sh 
cd 001_tokenizer 
python -m unittest tests.py
``` 

You'll find each task stubbed out with a working example in the filed caled examples.py. The tests should pass. To try the Kata, delete or comment out the return statment in the task you would like to try. See the tests fail, now make the tests pass on your own. 

## The Katas 
| #    | Kata                                       |
|------|--------------------------------------------|
| 1 | [Tokenization](001_tokenization/README.md) | 
| 2 | [Math](002_math/README.md)                 | 
| 3  | TBD |
| 4  | TBD |
| 5 | [Decision Trees](005_decision_trees/README.md)|


## Create a new Kata
```bash 
./bin/create_task.sh {{name_of_task_folder}}
```
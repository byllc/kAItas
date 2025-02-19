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

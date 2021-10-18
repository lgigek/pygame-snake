# pygame-snake

A pygame lab with a simple snake game. 

## TO-DOs
There are some TO-DOs, related to the game features:
- collisions that may cause game over (snake head with other body parts and screen's boundaries);

And others related to improve code architecture (comments, methods, modules, etc).

## Running the project
In order to run the project I used pyenv. 

Create a new virtualenv (via pyenv):
```
pyenv virtualenv 3.9.0 pygame-snake-3.9.0
```

Activate virtualenv:
```
pyenv activate pygame-snake-3.9.0
```

Install necessary dependencies (needed just once): 
```
./setup.sh
```

Finally, run the game: 
```
python main.py
```

## References
- [Criando um Snake do Zero com PyGame em 5 Minutos (ou mais)](https://www.youtube.com/watch?v=H4TXHI9BRCQ);
- [pygame-lab](https://github.com/IgooorGP/pygame-lab) (from @IgooorGP);
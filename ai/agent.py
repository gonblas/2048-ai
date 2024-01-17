from collections import deque
from typing import List
import numpy as np
import random
import torch 
import time

from ai.model import FNN_Model, Trainer
from ai.ai_settings import *
from game.game import Game
from ai.plot import Plot


class Agent():
    def __init__(self, size) -> None:
        self.n_games = 0
        self.epsilon = INITIAL_EPSILON
        self.gamma = INITIAL_GAMMA
        self.memory = deque(maxlen=MAX_MEMORY)
        self.size = size
        self.model = FNN_Model(self.size**2, self.size**2 + 16, 4)
        self.trainer = Trainer(model=self.model, lr=LR, gamma=self.gamma)


    #quizas podria pasarle si hay posiciones en las cuales pierde
    def get_status(self, board: List[List[float]]) -> torch.Tensor:
        # Especifica las dimensiones al crear el tensor
        return torch.Tensor(board).view(1, -1)



    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))



    def train_long_memory(self):
        if(len(self.memory) >= BATCH_SIZE):
            mini_sample = random.sample(self.memory, BATCH_SIZE) # LIST OF TUPLES
        else:
            mini_sample = self.memory

        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)



    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)



    def get_action(self, state):
        self.epsilon = 40 - self.n_games
        final_move = [0, 0, 0, 0] # [up [1,0,0,0], right [0,1,0,0], down [0,0,1,0], left [0,0,0,1]]
        if(random.randint(0,100) < self.epsilon): #Exploration
            move = random.randint(0, 3)
            final_move[move] = 1
        else: #Explotation
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_move[move] = 1
        return final_move


def train(board_size):
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    game = Game(board_size, user_mode=False)
    agent = Agent(game.size)
    while(True):
        old_state = agent.get_status(game.matrix)
        final_move = agent.get_action(old_state)
        reward, done, score = game.play_step(final_move)
        new_state = agent.get_status(game.matrix)
        agent.train_short_memory(old_state, final_move, reward, new_state, done)
        agent.remember(old_state, final_move, reward, new_state, done)
        time.sleep(0.1)

        if(done): #If game finished
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()
            
            if(score > record):
                record = score
                agent.model.save()
            
            print("Game", agent.n_games, "Score", score, "Record", record)
            
            #TODO: plot 
            plot_scores.append(score)
            total_score += score
            mean_score = total_score / agent.n_games
            plot_mean_scores.append(mean_score)
            Plot(plot_scores, plot_mean_scores)


if __name__ == "__main__":
    train()
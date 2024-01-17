import torch.nn.functional as F
import torch.optim as optim
import torch.nn as nn
import torch 
import os


class FNN_Model(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(FNN_Model, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)


    # Forward Propagation
    def forward(self, x): #Al hacer self.fcx(x) se pasa de la capa X, se multiplican los pesos, etc.
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x)) 
        x = self.fc2(x)
        return x



    def summary(self):
        print(self)



    def save(self, file_name="model.pth"):
        model_folder_path = "./model"
        os.makedirs(model_folder_path, exist_ok=True)
        file_name = os.path.join(model_folder_path, file_name)
        torch.save(self.state_dict(), file_name)





class Trainer:
    def __init__(self, model, lr, gamma):
        self.lr = lr
        self.gamma = gamma
        # device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        # model = FNN_Model(input_size, hidden_size, output_size).to(device)
        self.model = model
        self.optimizer = optim.Adam(model.parameters(), lr=self.lr)
        self.criterion = nn.CrossEntropyLoss() # función de pérdida, que mide cuán lejos están las predicciones del modelo, OBJETIVO: MINIMIZARLO
    
    
    def train_step(self, state, action, reward, next_state, done):
        # Convertir los datos a tensores de PyTorch
        state = torch.tensor(state, dtype=torch.float)
        next_state = torch.tensor(next_state, dtype=torch.float)
        action = torch.tensor(action, dtype=torch.long)
        reward = torch.tensor(reward, dtype=torch.float)

        if done is not None:
            done = torch.tensor(done, dtype=torch.bool) if isinstance(done, bool) else torch.tensor(done, dtype=torch.bool)
        else:
            done = torch.tensor(False, dtype=torch.bool)

        # Si la dimensión de state es 1, agregar una dimensión adicional
        if len(state.shape) == 1:
            state = torch.unsqueeze(state, 0)
            next_state = torch.unsqueeze(next_state, 0)
            action = torch.unsqueeze(action, 0)
            reward = torch.unsqueeze(reward, 0)
            done = torch.unsqueeze(done, 0)

        # 1: Obtener las predicciones Q con el estado actual
        pred = self.model(state)

        # 2: Calcular los objetivos Q (target) para cada transición
        targets = pred.clone()
        for idx in range(len(done)):
            Q_new = reward[idx]
            if not done[idx].item():
                Q_new = reward[idx] + self.gamma * torch.max(self.model(next_state[idx]))

            targets[idx][torch.argmax(action[idx]).item()] = Q_new

        # 3: Calcular la pérdida y realizar la retropropagación
        self.optimizer.zero_grad()
        loss = self.criterion(targets, pred)
        loss.backward()
        self.optimizer.step()

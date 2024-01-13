import torch 
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import os


class FNN_Model(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(FNN_Model, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)



    def forward(self, x):
        x = x.view(x.size(0), -1)  # Aplana la entrada
        x = self.fc1(x)             # Capa totalmente conectada sin activación
        x = self.relu(x)            # Función de activación ReLU aplicada a la salida de fc1
        x = self.fc2(x)             # Capa totalmente conectada después de aplicar ReLU
        return x



    def summary(self):
        print(self)



    def save(self, file_name="model.pth"):
        model_folder_path = "./model"
        if not os.path.exists(model_folder_path):
            os.makedirs(model_folder_path)
        file_name = os.path.join(model_folder_path, file_name)
        torch.save(self.state_dict(), file_name)






class Trainer:
    def __init__(self, model, lr, gamma):
        self.lr = lr
        self.gamma = gamma
        self.model = model
        self.optimizer = optim.Adam(model.parameters(), lr=self.lr)
        self.criterion = nn.MSELoss()
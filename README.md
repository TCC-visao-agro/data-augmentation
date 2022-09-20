# Data augmentation


## 📝Passo à passo
1)
```shell
pip install -r requirements.txt
```

2)
Download da [base de folhas segmentada do fundo](https://drive.google.com/drive/folders/1eFIoyx_mBawqu5DpRLgfudh26PAWPh-u?usp=sharing)

3)
Download da [rede u2net](https://drive.google.com/uc?id=1tCU5MM1LhRgGou5OpmpjBQbSrYIUoYab)
e colocar na pasta .u2net na raiz do usuário


4)
Criar dois diretórios na raiz do projeto: /images e /rotated_images


5)
Jogar todas as classes baixadas da base acima dentro do diretório /images


6)
```shell
python main.py
```

7)
Depois de muito tempo, o diretório /rotated_images terá todas as imagens aumentadas:



![augments](https://user-images.githubusercontent.com/56764133/186302666-49f81c97-e5df-4e39-824b-6aac90e96120.jpg)

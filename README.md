# 🎵 YouTube Converter – MP3 & MP4

Uma aplicação web simples e eficiente construída com **Django** e **yt-dlp** para converter vídeos do YouTube em **MP3** (apenas áudio) ou **MP4** (vídeo completo).

Permite aos usuários colar a URL do vídeo, escolher o formato desejado e baixar o arquivo processado **rapidamente**.

---

## 🚀 Funcionalidades

* Converter vídeos do YouTube para **MP3** (Áudio)
* Converter vídeos do YouTube para **MP4** (Vídeo)
* Interface intuitiva com design moderno
* Tratamento de erros robusto (URL inválida, falha na conversão etc.)
* Processo de download rápido

> 🎨 **Interface com Gradiente:**
> `background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);`

---

## 🛠 Tecnologias Utilizadas

O projeto é construído sobre as seguintes tecnologias:

* **Python 3**
* **Django** (Framework Web)
* **yt-dlp** (Para extração e download de vídeos)
* **ffmpeg** (Para processamento e conversão de mídia)
* **HTML, CSS e JavaScript** (Frontend)

---

## 📦 Instalação

Siga os passos abaixo para configurar e executar o projeto localmente.

### 1. Clonar o repositório

```bash
git clone [https://github.com/usuario/repositorio.git](https://github.com/usuario/repositorio.git)
cd repositorio
```

### 2. Criar ambiente virtual
É altamente recomendável usar um ambiente virtual para isolar as dependências.

```bash
python -m venv venv
```

### 3. Ativar o ambiente virtual
Windows:

```bash
venv\Scripts\activate
```

Linux:
```bash
source venv/bin/activate
```

### 4. Instalar dependências do Python

```bash
pip install -r requirements.txt
```

### 5. Instalar o ffmpeg
O ffmpeg é necessário para o processamento de áudio e vídeo.

Windows: Baixe e instale a partir do site oficial (https://ffmpeg.org/download.html) e certifique-se de adicioná-lo ao PATH do sistema.

Linux (Baseado em Debian):

```bash
sudo apt install ffmpeg
```

### 6. Executar o projeto

```bash
python manage.py runserver
```

---

## ⚠️ Aviso Legal
Este projeto foi desenvolvido apenas para fins educacionais.

O uso deste tipo de ferramenta para baixar conteúdo pode violar os termos de serviço do YouTube e/ou leis de direitos autorais. O desenvolvedor não se responsabiliza por qualquer uso indevido. Use com responsabilidade.

---

## 📬 Contato
Para quaisquer dúvidas, sugestões ou para relatar um bug, por favor, abra uma issue neste repositório.

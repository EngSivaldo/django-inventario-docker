# 1. Usa uma imagem oficial do Python
FROM python:3.11-slim

# 2. Define onde o código vai morar no Linux do Docker
WORKDIR /app

# 3. Instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copia o resto do código
COPY . .

# 5. Comando para ligar o Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
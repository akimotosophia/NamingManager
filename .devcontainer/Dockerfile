# ベースイメージ
FROM python:3.12-slim

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    zip \
    git \
    less \
    groff \
    bash-completion \
    npm \
    && apt-get clean

# AWS CLIのインストール
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf aws awscliv2.zip

# Node.js（LTS）インストール (create-react-app用)
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - && \
    apt-get install -y nodejs

# AWS SAM CLIのインストール
RUN curl -Lo sam-installation.zip https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip && \
    unzip sam-installation.zip -d sam-installation && \
    ./sam-installation/install && \
    rm -rf sam-installation sam-installation.zip

# 必要なPythonライブラリをグローバルインストール（任意）
RUN pip install --no-cache-dir boto3

# デフォルト作業ディレクトリ
WORKDIR /workspace

# 便利なbash設定（任意）
RUN echo "alias ll='ls -alF'" >> ~/.bashrc

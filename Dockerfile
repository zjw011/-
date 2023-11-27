# 使用基础镜像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 复制所需文件到镜像中
COPY . /app

# 安装依赖
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt


# 暴露端口
EXPOSE 5221

# 运行命令
CMD ["python3", "app.py"]

FROM python:buster

# Install rust compiler
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"
RUN rustc -V

# Install dependencies:
WORKDIR /app
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

#RUN app
ENTRYPOINT ["python"]
CMD ["main.py"]

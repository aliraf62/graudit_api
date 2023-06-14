FROM ubuntu:latest

# Install Python, pip, git, grep (needed in graudit)
RUN apt-get update \
    && apt-get install -y python3 python3-pip git grep \
    && rm -rf /var/lib/apt/lists/*  # Clean up APT cache

WORKDIR /app
COPY . /app

# Install Python dependencies that I put in a txt file for ease of access
RUN pip3 install -r python_requirements.txt

# Clone Graudit repo
RUN git clone https://github.com/wireghoul/graudit.git

# Adding Graudit to the PATH so it can be invoked from my api Python script
ENV PATH="/app/graudit:${PATH}"

ENTRYPOINT ["python3", "graudit_api_test_Ali.py"]
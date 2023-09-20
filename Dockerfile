FROM python:3.11.4-slim-buster AS builder
LABEL authors="issakha"

# Install required system packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    curl \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev \
    python-openssl \
    git \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Install pyenv
ENV PYENV_ROOT="/opt/pyenv"
RUN git clone https://github.com/pyenv/pyenv.git $PYENV_ROOT
ENV PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"

# Install specific Python version using pyenv
ENV PYTHON_VERSION="3.11.4"
RUN pyenv install $PYTHON_VERSION && pyenv global $PYTHON_VERSION

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /


# Install pipenv
RUN pip install --upgrade pip
RUN pip install pipenv

# Copy project files into the container
COPY . .


# Install project dependencies using pipenv
RUN pipenv install

#RUN pip install -r requirements.txt --no-cache-dir

# Expose port 8000 for the Django development server
EXPOSE 8000

# Start the Django development server
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
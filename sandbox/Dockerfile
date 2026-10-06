FROM gcc:14-bookworm

# Multi-language execution sandbox.
# gcc image already provides gcc + g++. Add Python and Java.
RUN apt-get update --fix-missing \
    && apt-get install -y --no-install-recommends --fix-missing \
        python3 \
        openjdk-17-jdk-headless \
        sqlite3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

WORKDIR /box

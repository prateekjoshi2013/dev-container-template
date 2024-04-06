# Use an Ubuntu base image
FROM ubuntu:latest

# Set the default shell to bash
ENV SHELL /bin/bash

# Set shell as bash
SHELL ["/bin/bash", "-c"]

# Install necessary packages and tools
RUN apt-get update && apt-get install -y

RUN apt-get install curl git unzip nano make locales -y 

# Run arch specificexpectations for specific arch (x86_64, arm64, aarch64)
COPY ./arch_spec_install_script.sh /scripts/

RUN chmod +x /scripts/arch_spec_install_script.sh

RUN /scripts/arch_spec_install_script.sh

# installing oh my bash - https://github.com/ohmybash/oh-my-bash
RUN curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh | bash

# customize the bash shell ans set vscode theme
RUN sed -i 's/^OSH_THEME=.*/OSH_THEME="vscode"/' ~/.bashrc

# locale generation is important to make bash 
# work properly with newlines and such
RUN locale-gen en_US.UTF-8

# installing language specific tools like nvm, node, python, go, cargo, rust 

#ARG image_openjdk
#FROM ${image_openjdk}:25-jre-alpine-3.23
from eclipse-temurin:25-jre-alpine-3.23
ARG TargetEnvironmentType
ARG Version
LABEL maintainer "marius.goecke@gmail.com"
LABEL description="PaperServer is a docker-image for simply running a Paper-server in a docker-container."
LABEL targetEnvironmentType="$TargetEnvironmentType"
LABEL version="$Version"

RUN mkdir /Workspace
RUN mkdir /Workspace/Application
RUN mkdir /Workspace/Configuration
RUN mkdir /Workspace/Data

# TODO redirect logs and crash-reports to /Workspace/Logs-folder

COPY PaperServer/EntryPointScript.sh /Workspace/Application/EntryPointScript.sh
RUN chmod +x /Workspace/Application/EntryPoint.sh
COPY Other/Resources/PaperServer/PaperServer.jar /Workspace/Application/PaperServer.jar

WORKDIR /Workspace/Configuration

ENTRYPOINT ["/Workspace/Application/EntryPointScript.sh"]

ARG image_debian
FROM ${image_debian}:stable-20251208-slim

ARG TargetEnvironmentType
ARG Version
LABEL maintainer "marius.goecke@gmail.com"
LABEL description="PaperServer is a docker-image for simply running a Paper-server in a docker-container."
LABEL targetEnvironmentType="$TargetEnvironmentType"
LABEL version="$Version"

RUN apt-get update && \
    apt-get install -y --no-install-recommends openjdk-25-jre curl ca-certificates && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir /Workspace && \
    mkdir /Workspace/Application && \
    mkdir /Workspace/Configuration && \
    mkdir /Workspace/Data && \
    useradd --base-dir /Workspace --home /Workspace user

# TODO redirect logs and crash-reports to /Workspace/Logs-folder

COPY PaperServer/EntryPointScript.sh /Workspace/Application/EntryPointScript.sh
COPY Other/Resources/PaperServer/PaperServer.jar /Workspace/Application/PaperServer.jar

COPY PaperServer/HealthCheck.sh /Workspace/Application
RUN chmod +x /Workspace/Application/HealthCheck.sh

HEALTHCHECK CMD /Workspace/Application/HealthCheck.sh

RUN chown -R user:user /Workspace && \
    chmod -R 700 /Workspace && \
    chmod +x /Workspace/Application/EntryPointScript.sh

USER user
WORKDIR /Workspace/Configuration

ENTRYPOINT ["/Workspace/Application/EntryPointScript.sh"]

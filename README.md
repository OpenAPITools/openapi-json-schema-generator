# Repo Location Update
On Oct 2nd 2022, Justin (@spacether), who's been leading this project with the goal to make the output 100% compliant with JSON schema as part of the OpenAPI 3.1 specification with a focus on complex cases (top-down approach), has decided to run this project in another organization account [new org](https://github.com/openapi-json-schema-tools) instead so that he can fine tune the pace of the projects to align with different goals and requirements. Please follow [the new repo here](https://github.com/openapi-json-schema-tools/openapi-json-schema-generator) if you would like to take advantage of the latest works (enhancements, bug fixes)  by Justin.


| **IMPORTANT: before the first release, one will need to build the project locally to use the enhancements, bug fixes in the latest master** |
| --- |

<div align="center">

[![CI Tests](https://circleci.com/gh/OpenAPITools/openapi-json-schema-generator.svg?style=shield)](https://circleci.com/gh/OpenAPITools/openapi-json-schema-generator) [![Apache 2.0 License](https://img.shields.io/badge/License-Apache%202.0-orange)](./LICENSE) 

</div>

<div align="center">

:star::star::star: If you would like to contribute, please refer to [guidelines](CONTRIBUTING.md) and a list of [open tasks](https://github.com/openapitools/openapi-json-schema-generator/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22).:star::star::star:

:warning: If the OpenAPI spec, templates or any input (e.g. options, environment variables) is obtained from an untrusted source or environment, please make sure you've reviewed these inputs before using this project to generate the API client, server stub or documentation to avoid potential security issues (e.g. [code injection](https://en.wikipedia.org/wiki/Code_injection)). For security vulnerabilities, please contact [team@openapitools.org](mailto:team@openapitools.org). :warning:

:bangbang: Both "OpenAPI Tools" (https://OpenAPITools.org - the parent organization of this project) and this repo are not affiliated with OpenAPI Initiative (OAI) :bangbang:

</div>

## Overview
This project allows auto-generation of API client libraries (SDK generation) with a focus on JSON Schema given an [OpenAPI Spec](https://github.com/OAI/OpenAPI-Specification) (3.0 are supported). Currently, the following languages/frameworks are supported:

- python


## Why this repo exists

This repo is based on v6.2.0 of OpenAPI Generator. This project focuses on making the output 100% compliant with JSON schema as part of the OpenAPI 3.1 specification with a focus on complex cases (top-down approach). The goal is to fully support everything defined in JSON schema so that developers can leverage JSON schema as well as OpenAPI specification in their API design. Building here allows for more rapid progress supporting new features in OpenAPI 3.X without having to support many older generators which don't use the new features.

## Table of contents

  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [1 - Installation](#1---installation)
    - [1.1 - Compatibility](#11---compatibility)
    - [1.2 - Build Projects](#14---build-projects)
    - [1.3 - Docker](#16---docker)
  - [2 - Getting Started](#2---getting-started)
  - [3 - Usage](#3---usage)
    - [3.1 - Customization](#31---customization)
    - [3.2 - Workflow Integration](#32---workflow-integration-maven-gradle-github-cicd)
    - [3.3 - Online Generator](#33---online-generator)
    - [3.4 - License Information on Generated Code](#34---license-information-on-generated-code)
  - [4 - About Us](#4---about-us)
    - [4.1 - History of this Project](#41---history-of-this-project)
  - [5 - License](#6---license)

## [1 - Installation](#table-of-contents)

### [1.1 - Compatibility](#table-of-contents)

The OpenAPI Specification has undergone 3 revisions since initial creation in 2010.  This project has the following compatibilities with the OpenAPI Specification:

| Project Version              | Release Date | Notes         |
|------------------------------|--------------| ------------- |
| 1.0.0 (first stable release) | TBD          | First release |

OpenAPI Spec compatibility: 3.0

### [1.2 - Build Projects](#table-of-contents)

To build from source, you need the following installed and available in your `$PATH:`

* [Java 8](https://www.oracle.com/technetwork/java/index.html)

* [Apache Maven 3.3.4 or greater](https://maven.apache.org/)

After cloning the project, you can build it from source with this command:
```sh
mvn clean install
```

If you don't have maven installed, you may directly use the included [maven wrapper](https://github.com/takari/maven-wrapper), and build with the command:
```sh
./mvnw clean install
```

The default build contains minimal static analysis (via CheckStyle). To run your build with PMD and Spotbugs, use the `static-analysis` profile:

```sh
mvn -Pstatic-analysis clean install
```

### [1.3 - Docker](#table-of-contents)

#### CLI Docker Image

The docker image acts as a standalone executable. It can be used as an alternative to installing via homebrew, or for developers who are unable to install Java or upgrade the installed version.

To generate code with this image, you'll need to mount a local location as a volume.

Example:

```sh
docker run --rm -v "${PWD}:/local" openapitools/openapi-json-schema-generator-cli generate \
    -i https://raw.githubusercontent.com/openapitools/openapi-json-schema-generator/master/modules/openapi-json-schema-generator/src/test/resources/3_0/petstore.yaml \
    -g python \
    -o /local/out/python
```

The generated code will be located under `./out/python` in the current directory.

#### Online Docker Image

The openapi-json-schema-generator-online image can act as a self-hosted web application and API for generating code. This container can be incorporated into a CI pipeline, and requires at least two HTTP requests and some docker orchestration to access generated code.

Example usage:

```sh
# Start container at port 8888 and save the container id
> CID=$(docker run -d -p 8888:8080 openapitools/openapi-json-schema-generator-online)

# allow for startup
> sleep 10

# Get the IP of the running container (optional)
GEN_IP=$(docker inspect --format '{{.NetworkSettings.IPAddress}}'  $CID)

# Execute an HTTP request to generate a Ruby client
> curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' \
-d '{"openAPIUrl": "https://raw.githubusercontent.com/openapitools/openapi-json-schema-generator/master/modules/openapi-json-schema-generator/src/test/resources/3_0/petstore.yaml"}' \
'http://localhost:8888/api/gen/clients/python'

{"code":"c2d483.3.4672-40e9-91df-b9ffd18d22b8","link":"http://localhost:8888/api/gen/download/c2d483.3.4672-40e9-91df-b9ffd18d22b8"}

# Download the generated zip file
> wget http://localhost:8888/api/gen/download/c2d483.3.4672-40e9-91df-b9ffd18d22b8

# Unzip the file
> unzip c2d483.3.4672-40e9-91df-b9ffd18d22b8

# Shutdown the openapi generator image
> docker stop $CID && docker rm $CID
```

#### Development in docker

You can use `run-in-docker.sh` to do all development. This script maps your local repository to `/gen`
in the docker container. It also maps `~/.m2/repository` to the appropriate container location.

To execute `mvn package`:

```sh
git clone https://github.com/openapitools/openapi-json-schema-generator
cd openapi-json-schema-generator
./run-in-docker.sh mvn package
```

Build artifacts are now accessible in your working directory.

Once built, `run-in-docker.sh` will act as an executable for the cli. To generate code, you'll need to output to a directory under `/gen` (e.g. `/gen/out`). For example:

```sh
./run-in-docker.sh help # Executes 'help' command for the cli
./run-in-docker.sh /gen/bin/python-petstore.sh  # Builds the Go client
./run-in-docker.sh generate -i modules/openapi-json-schema-generator/src/test/resources/3_0/petstore.yaml \
    -g go -o /gen/out/python-petstore -p packageName=petstore_api # generates python client, outputs locally to ./out/python-petstore
```

##### Troubleshooting

If an error like this occurs, just execute the **mvn clean install -U** command:

> org.apache.maven.lifecycle.LifecycleExecutionException: Failed to execute goal org.apache.maven.plugins:maven-surefire-plugin:2.19.1:test (default-test) on project: A type incompatibility occurred while executing org.apache.maven.plugins:maven-surefire-plugin:2.19.1:test: java.lang.ExceptionInInitializerError cannot be cast to java.io.IOException

```sh
./run-in-docker.sh mvn clean install -U
```

> Failed to execute goal org.fortasoft:gradle-maven-plugin:1.0.8:invoke (default) on project openapi-json-schema-generator-gradle-plugin-mvn-wrapper: org.gradle.tooling.BuildException: Could not execute build using Gradle distribution 'https://services.gradle.org/distributions/gradle-4.7-bin.zip'

Right now: no solution for this one :|

#### Run Docker in Vagrant
Prerequisite: install [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
 ```sh
git clone https://github.com/openapitools/openapi-json-schema-generator.git
cd openapi-json-schema-generator
vagrant up
vagrant ssh
cd /vagrant
./run-in-docker.sh mvn package
```

## [2 - Getting Started](#table-of-contents)

To generate a PHP client for [petstore.yaml](https://raw.githubusercontent.com/openapitools/openapi-json-schema-generator/master/modules/openapi-json-schema-generator/src/test/resources/3_0/petstore.yaml), please run the following
```sh
git clone https://github.com/openapitools/openapi-json-schema-generator
cd openapi-json-schema-generator
mvn clean package
java -jar modules/openapi-json-schema-generator-cli/target/openapi-json-schema-generator-cli.jar generate \
   -i https://raw.githubusercontent.com/openapitools/openapi-json-schema-generator/master/modules/openapi-json-schema-generator/src/test/resources/3_0/petstore.yaml \
   -g php \
   -o /var/tmp/php_api_client
```
(if you're on Windows, replace the last command with `java -jar modules\openapi-json-schema-generator-cli\target\openapi-json-schema-generator-cli.jar generate -i https://raw.githubusercontent.com/openapitools/openapi-json-schema-generator/master/modules/openapi-json-schema-generator/src/test/resources/3_0/petstore.yaml -g php -o c:\temp\php_api_client`)

To get a list of **general** options available, please run `java -jar modules/openapi-json-schema-generator-cli/target/openapi-json-schema-generator-cli.jar help generate`

To get a list of PHP specified options (which can be passed to the generator with a config file via the `-c` option), please run `java -jar modules/openapi-json-schema-generator-cli/target/openapi-json-schema-generator-cli.jar config-help -g php`

## [3 - Usage](#table-of-contents)

### To generate a sample client library
You can build a client against the [Petstore API](https://raw.githubusercontent.com/openapitools/openapi-json-schema-generator/master/modules/openapi-json-schema-generator/src/test/resources/3_0/petstore.yaml) as follows:

```sh
./bin/generate-samples.sh ./bin/configs/python.yaml
```

(On Windows, please install [GIT Bash for Windows](https://gitforwindows.org/) to run the command above)

This script will run the generator with this command:

```sh
java -jar modules/openapi-json-schema-generator-cli/target/openapi-json-schema-generator-cli.jar generate \
  -i https://raw.githubusercontent.com/openapitools/openapi-json-schema-generator/master/modules/openapi-json-schema-generator/src/test/resources/3_0/petstore.yaml \
  -g python \
  --additional-properties packageName=petstore_api \
  -o samples/openapi3/client/petstore/python
```

with a number of options. [The python options are documented here.](docs/generators/python.md)

You can also get the options with the `help generate` command (below only shows partial results):

```
NAME
        openapi-json-schema-generator-cli generate - Generate code with the specified
        generator.

SYNOPSIS
        openapi-json-schema-generator-cli generate
                [(-a <authorization> | --auth <authorization>)]
                [--api-name-suffix <api name suffix>] [--api-package <api package>]
                [--artifact-id <artifact id>] [--artifact-version <artifact version>]
                [(-c <configuration file> | --config <configuration file>)] [--dry-run]
                [(-e <templating engine> | --engine <templating engine>)]
                [--enable-post-process-file]
                [(-g <generator name> | --generator-name <generator name>)]
                [--generate-alias-as-model] [--git-host <git host>]
                [--git-repo-id <git repo id>] [--git-user-id <git user id>]
                [--global-property <global properties>...] [--group-id <group id>]
                [--http-user-agent <http user agent>]
                [(-i <spec file> | --input-spec <spec file>)]
                [--ignore-file-override <ignore file override location>]
                [--import-mappings <import mappings>...]
                [--instantiation-types <instantiation types>...]
                [--invoker-package <invoker package>]
                [--language-specific-primitives <language specific primitives>...]
                [--legacy-discriminator-behavior] [--library <library>]
                [--log-to-stderr] [--minimal-update]
                [--model-name-prefix <model name prefix>]
                [--model-name-suffix <model name suffix>]
                [--model-package <model package>]
                [(-o <output directory> | --output <output directory>)] [(-p <additional properties> | --additional-properties <additional properties>)...]
                [--package-name <package name>] [--release-note <release note>]
                [--remove-operation-id-prefix]
                [--reserved-words-mappings <reserved word mappings>...]
                [(-s | --skip-overwrite)] [--server-variables <server variables>...]
                [--skip-validate-spec] [--strict-spec <true/false strict behavior>]
                [(-t <template directory> | --template-dir <template directory>)]
                [--type-mappings <type mappings>...] [(-v | --verbose)]

OPTIONS
        -a <authorization>, --auth <authorization>
            adds authorization headers when fetching the OpenAPI definitions
            remotely. Pass in a URL-encoded string of name:header with a comma
            separating multiple values

...... (results omitted)

        -v, --verbose
            verbose mode

```

You can then use the auto-generated client. The README.md is a good starting point.

Other generators have [samples](https://github.com/OpenAPITools/openapi-json-schema-generator/tree/master/samples) too.

### [3.1 - Customization](#table-of-contents)

Please refer to [customization.md](docs/customization.md) on how to customize the output (e.g. package name, version)

### [3.2 - Workflow Integration (Maven, Gradle, Github, CI/CD)](#table-of-contents)

Please refer to [integration.md](docs/integration.md) on how to integrate OpenAPI generator with Maven, Gradle,  Github and CI/CD.

### [3.3 - Online Generator](#table-of-contents)

Please refer to [online.md](docs/online.md) on how to run and use the `openapi-json-schema-generator-online` - a web service for this project.

### [3.4 - License information on Generated Code](#table-of-contents)

This project is intended as a benefit for users of the Open API Specification.  The project itself has the [License](#license) as specified. In addition, please understand the following points:

* The templates included with this project are subject to the [License](#license).
* Generated code is intentionally _not_ subject to the parent project license

When code is generated from this project, it shall be considered **AS IS** and owned by the user of the software.  There are no warranties--expressed or implied--for generated code.  You can do what you wish with it, and once generated, the code is your responsibility and subject to the licensing terms that you deem appropriate.

### [4 - History of this Project](#table-of-contents)

This project is based on OpenAPI Generator v6.2.0. It focuses on JSON schema support and the output is designed to be 100% compliance with JSON Schema.

## [5 - License](#table-of-contents)
-------

Copyright 2018 OpenAPI-Generator Contributors (https://openapi-generator.tech)
Copyright 2018 SmartBear Software

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at [apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

---

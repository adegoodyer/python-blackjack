# Welcome to Blackjack!
- [Welcome to Blackjack!](#welcome-to-blackjack)
  - [Overview](#overview)
    - [Rules](#rules)
    - [Gameplay](#gameplay)
  - [Development](#development)
    - [Testing](#testing)
    - [Production Build](#production-build)
    - [Scanning](#scanning)
    - [Publish Image](#publish-image)
    - [Cleanup](#cleanup)

## Overview

```bash
d run --rm -it --name python_blackjack adegoodyer/python_blackjack:latest
```

### Rules
- Try to get as close to 21 without going over!
- Kings, Queens, and Jacks are worth 10 points
- Aces are worth 1 or 11 points
- Cards 2 through 10 are worth their face value

### Gameplay
- (H)it to take another card
- (S)tand to stop taking cards
- on your first play, you can (D)ouble down to increase your bet
but must hit exactly one more time before standing
- in case of a tie, the bet is returned to the player
- dealer stops hitting at 17

## Development

```bash
# build and run dev container
# (bind mounted - changes in container dir and host dir are synced)
d build --target dev -t adegoodyer/python_blackjack:dev . && \
d run -itd -v "$(pwd)":/app --name python_blackjack_dev adegoodyer/python_blackjack:dev

# attach to dev container via VSCode

# manually ssh into dev container (optional)
# (changes in container and host directory are also synced)
d exec -it python_blackjack_dev bash

# stop and remove container
d stop python_blackjack_dev && d rm python_blackjack_dev
```

### Testing
```bash
# build test container and execute tests
d build --target testing -t adegoodyer/python_blackjack:testing . && \
d run -it --rm --name python_blackjack_testing adegoodyer/python_blackjack:testing
```

### Production Build
```bash
# build and run production container
d build -t adegoodyer/python_blackjack:runtime . && \
d run -it --rm --name python_blackjack_runtime adegoodyer/python_blackjack:runtime bash
```

### Scanning
```bash
# scan container
grype adegoodyer/python_blackjack:runtime
d scan adegoodyer/python_blackjack:runtime # uses snyk

# generate SBOM
syft adegoodyer/python_blackjack:runtime
```

### Publish Image
```bash
# login and push image (via pipeline)
git tag -a v0.0.1 -m "v0.0.1"
d logout && d login --username=adegoodyer
d push username/repo --all-tags

# login and push image (locally)
d logout && d login --username=adegoodyer
d push -t username/repo:0.0.1 adegoodyer/python_flask_sqlite_form:latest .
```

### Cleanup
```bash
# stop and remove dev, testing, and runtime containers
# clear unused volumes, networks, images and data
d stop python_blackjack_dev && d rm python_blackjack_dev && \
d stop python_blackjack_testing && d rm python_blackjack_testing && \
d stop python_blackjack_runtime && d rm python_blackjack_runtime && \
d system prune -f
```

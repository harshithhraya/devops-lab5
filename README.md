# Lab 5 - Docker Security with AppArmor

## Objective
To configure an AppArmor security profile for a Flask application running in a Docker container and test restricted actions using Python.

## Tools and Technologies
- GitHub Codespaces
- Docker
- AppArmor
- Python
- Flask
- Python Docker SDK

## Implementation
1. Verified that AppArmor is enabled in the kernel.
2. Checked Docker's AppArmor support.
3. Created and loaded a custom AppArmor profile named `my-apparmor-profile`.
4. Created a Flask web application and Dockerfile.
5. Built the Docker image `flask-apparmor`.
6. Started the container with the custom AppArmor profile requested.
7. Tested the Flask application using `curl`.
8. Used the Python Docker SDK to create and inspect a container.
9. Tested restricted actions using `test_restricted_actions.py`.

## Results

| Test | Result |
|---|---|
| AppArmor kernel enabled | Passed |
| Docker AppArmor support detected | Passed |
| Custom profile loaded | Passed |
| Direct `/etc/passwd` access restriction using `aa-exec` | Passed |
| Flask application response | Passed |
| Python Docker SDK script | Passed |
| Custom profile enforcement inside Docker container | Not confirmed |

## Important Observation
Docker accepted the security option `apparmor=my-apparmor-profile`, and the container's configuration showed that option. However, `/proc/self/attr/current` returned `unconfined`, and the container tests could read `/etc/passwd` and run Bash successfully.

Therefore, the custom profile's direct restriction test succeeded, but enforcement of the custom profile inside the Docker container was not demonstrated.

## Conclusion
The Flask application, custom AppArmor profile, and Python Docker SDK scripts were configured and tested. Direct testing confirmed that the profile denies reading `/etc/passwd`. However, further investigation is required to establish why the Docker container process was reported as unconfined.

## Cleanup
The test scripts stop and remove their temporary containers after execution.
import docker

client = docker.from_env()

container = client.containers.run(
    "flask-apparmor",
    detach=True,
    security_opt=["apparmor=my-apparmor-profile"],
)

try:
    result = container.exec_run("cat /etc/passwd")
    print("Read /etc/passwd exit code:", result.exit_code)
    print("Output:", result.output.decode(errors="replace")[:300])

    result = container.exec_run("/bin/bash")
    print("Run /bin/bash exit code:", result.exit_code)
    print("Output:", result.output.decode(errors="replace")[:300])
finally:
    container.stop()
    container.remove()
    print("Container stopped and removed.")

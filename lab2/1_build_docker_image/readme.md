# Introduction to Automated Building of Docker Images

In this exercise, we will automatically build a Docker image after each commit from exercise 1.1 and publish it to https://hub.docker.com by using the workflows from Github.

1. Register at hub.docker.com and create a public (and free) repository
2. Have a look at `.github/workflows/docker-image.yml`
3. We defined to events to react on: push and pull_request
4. I created an environment `dockerhub` in the Github settings for the dockerhub secrets and refer to it
5. Next, we specified the steps to do in this job:
6. check out the repo
7. login to Dockerhub
8. build the image
9. push the image to Dockerhub

TODO: use tags from git to tag our image.

---

A cool tool I discovered:
- https://github.com/nektos/act

act runs the CI pipeline on your local machine (faster than pushing it to the repo and debug it there).

First, create a secrets file containing your dockerhub credentials (do **not** commit/publish it to your public git repo):

`$ cat my.secrets`:
```
DOCKER_USER="dockerhub username"
DOCKER_PASSWORD="dockerhub password"
``` 

The run `act` in your repo and refer to the secrets file:
`act --secret-file my.secrets`

On success, you will find a new/an updated image in your dockerhub.

# Docker example running Selenium with Python 3.10



Just build and run locally for testing.
```
docker build -t docker_selenium .
docker run --rm -p 8080:8080 -e PORT=8080 docker_selenium
```

This app must return the description string from Docker repository:<br>
https://github.com/docker
>![Captura de tela de 2023-08-24 17-06-13](https://github.com/williamfalinski/docker-selenium-python/assets/26746287/42473e66-8520-4000-a9ed-59d2463d7469)

Result:<br>
>![Captura de tela de 2023-08-24 17-07-30](https://github.com/williamfalinski/docker-selenium-python/assets/26746287/5b8c8024-3377-4c40-a06b-32845c1332b0)

Credits:
- Original code, python 3.7:
https://dev.to/googlecloud/using-headless-chrome-with-cloud-run-3fdp
- Correct driver issue:
https://stackoverflow.com/questions/76913935/selenium-common-exceptions-sessionnotcreatedexception-this-version-of-chromedri




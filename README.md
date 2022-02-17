## dependencies
  - [docker](https://docs.docker.com/get-docker/)
## installation
### 1) get a clone from repo or just download it 
### 2) run docker compose : 
  - run the following commnand to build images and run containers
      ```sh 
      docker-composer up
      ```

### 3) make migrations :
  - after building docker images and running container , follow this command to make migrations :
    - open CMD for backend container in diractory of repo :
      ```sh 
      docker-compose exec backend sh
      ```
    - then make migrations :
      ```sh 
      python manage.py makemigrations
      ```
    - then migrate : 
      ```sh 
      python manage.py migrate 
      ```
### 4) create super user :
  - after making  migrations,create super user  to login to admin panel  :
    - create super user :
      ```sh 
      python manage.py createsuperuser
      ```
## API documentations
  ### How to use app 
  - just open your browser to `http://127.0.0.1:8000/` , you will get all documentation about the API 
  ### notes :
  - Base url for API : `http://127.0.0.1:8000/api/`
  - to exexute API requests in the broweser :
    - you have to login by the login url(exists in the documentation)
    - then click on `Atherize` button (on the top of the page),popup will open , in the value input add the access token which will gotten after you login .
      - add the access token in value field  like  this: 
      ```sh 
      Bearer access_token 
      ``` 
## to access admin panel 
   - just open your browser to `http://127.0.0.1:8000/admin` 

## Testing
### you can run test cases by the following commands :
   - run the following commnand
      ```sh 
      docker-compose exec backend sh
      ```
  - then run
    ```sh 
    python manage.py test
    ```

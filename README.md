# Django Quickstarter

*Boilerplate for django 4.x*

The goal here is to provide a django starter kit with a complete authentication system, and canvas for docker / docker-compose ready for
deployment.

## First

Rename 'project_' into something more apropriate, then search and change
 the word 'project_' in a few files:
- manage.py
- settings.py
- prod_config/entrypoint.sh (the gunicorn command)

Use `dependencies_pip.txt` to create the environment, and then pip freeze it
to `requirements.txt`.

## Environment variables

Environment variables are stored in the `.env` file, override them on the
server in production.

### General settings

When switching from dev to prod, this are the settings you want to change
 in `.env`:
```
# simple django debug option
DEBUG=1
# if DB is not postges, it will be sqlite by default
DB_IS_POSTGRESQL=0
# set 1: when you have properly configured an email to be
# used by your web site like a "no-replay@my_site.com"
# set 0: the emails sent will be emulated in console
EMAIL_IS_CONFIGURED=0
```
**About DEBUG**: when ON, the statics are served by django itself, not suitable
for production. when OFF, the statics are served by Nginx, then, on the port
used by nginx (here by default 80). So, when testing your app with DEBUG=0,
no static will appear on port 8000, just change the port in the browser to 80.


The other settings are quite self-explainatory.

## Tests

`coverage run ./manage.py test -v 2` # [-v 2 ] is for verbose

`coverage report` to see the report

## Reminders

Delete all 'none' tagged docker images:
```sh
docker rmi $(docker images -f "dangling=true" -q)
```

# Deployment on DigitalOcean droplet

Be sure you have registered an ssh public key in your account

### Droplet
- choose docker instead of an OS
- choose whatever plan is needed
- create the droplet

### Create a non-root user

- connect with SSH:
`ssh root@IP_OF_THE_DROPLET`
- then:
```
adduser <username>
# then fill the answered fields
usermod -aG docker <username>
usermod -aG sudo <username>
cp -r /root/.ssh /home/<username>/.ssh
cd /home/<username>
chown -R <username>:<username> .
exit
```
Now you should be able to connect with: `ssh <username>@IP_OF_THE_DROPLET`,
do it.

Then you will need new ssh keys to connect to github from this server
```
cd /home/<username>
ssh-keygen -t ed25519 -C <email_used_for_your_github_account@example.com>
cat id_ed25519.pub

# some output...
```
Copy this output and add it in your github account as a new ssh key.
 Now the server is allowed to access github to clone (SSH) your repos.

```
cd /home/<username>
git clone git@github.com:<your/project>.git
cd <project>
nano .env
# modify the settings, change the passwords, etc... Save and exit nano
sudo apt install docker-compose   # if not already installed
docker-compose up --build

# once it is up, you can check in your browser at the
# site's IP, it works !
# then stop that with ctrl+c, wait until it is all stoped

docker-compose up -d
```

Done ! Your site is online ! Congratz !

## Import Environment and FileSystemLoader so we can load in our template.
## Import yaml as our config is yaml.
from jinja2 import Environment, FileSystemLoader
import yaml

def get_template(env):

    ## Open up our yaml file which will map any services depending on the environment.
    with open('service-discovery.yaml', 'r') as file:
        svc_conf = yaml.safe_load(file)
    
    ## Pulling the values from the service discovery yaml and assigning them to variables.
    monitoringserver = svc_conf[env]['monitoring-server']
    keystore = svc_conf[env]['key-store']
    webservicefrontend = svc_conf[env]['web-service-frontend']
    dbservicebackend = svc_conf[env]['db-service-backend']

    ## Load the templates directory.
    file_loader = FileSystemLoader('templates')
    ## Create our Jinja environment
    jinja_env = Environment(loader=file_loader)
    ## Get our template config file.
    template = jinja_env.get_template("config.yaml")
    ## Create the config file using are variables from the service-discovery yaml.
    outputText = template.render(
        monitoringserver = monitoringserver,
        keystore = keystore,
        webservicefrontend = webservicefrontend,
        dbservicebackend = dbservicebackend
    )

    ## Write the new file
    f = open(f"output/{env}Config.yaml", "w")
    f.write(outputText)
    f.close()